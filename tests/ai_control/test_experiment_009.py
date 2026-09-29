from dataclasses import replace
import ast
import importlib.util
import inspect
from pathlib import Path
import socket
import subprocess
import sys
import unittest
from unittest import mock

_ROOT = Path(__file__).resolve().parents[2]


def _load(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, _ROOT / relative)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


schedule = _load(
    "ai_control.canonical_observation_009_schedule",
    "ai_control/canonical_observation_009_schedule.py",
)
fixture = _load(
    "ai_control.canonical_observation_009",
    "ai_control/canonical_observation_009.py",
)
controller = _load("experiment_009_controller_under_test", "ai_control/experiment_009.py")


class Experiment009ControllerTests(unittest.TestCase):
    def test_preflight_pins_sources_without_running_reserved_trial(self):
        with mock.patch.object(
            controller,
            "run_nonconfirmatory_trial",
            side_effect=AssertionError("reserved trial executed"),
        ):
            result = controller.preflight()
        self.assertEqual(result["canonical_observation_009.py_blob"], controller.EXPECTED_FIXTURE_BLOB)
        self.assertEqual(
            result["canonical_observation_009_schedule.py_blob"],
            controller.EXPECTED_SCHEDULE_BLOB,
        )
        self.assertEqual(result["schedule_sha256"], schedule.EXPECTED_SCHEDULE_SHA256)
        self.assertEqual(result["reserved_seed_first"], 426_000)
        self.assertEqual(result["reserved_seed_last"], 426_999)
        self.assertEqual(result["runs_if_explicitly_started"], 4_000)

    def test_preflight_aborts_on_blob_mismatch_before_trial(self):
        with mock.patch.object(controller, "_git_blob_sha", return_value="0" * 40), mock.patch.object(
            controller,
            "run_nonconfirmatory_trial",
            side_effect=AssertionError("reserved trial executed"),
        ):
            with self.assertRaises(controller.IntegrityAbort):
                controller.preflight()

    def test_reserved_seed_is_rejected_by_fixture_entry_point(self):
        with self.assertRaises(ValueError):
            fixture.run_nonconfirmatory_trial(
                seed=426_000,
                config=fixture.CanonicalObservationConfig("plain", "primary"),
                source_commit=controller.SOURCE_COMMIT,
                violation_present=True,
            )
        self.assertIn("_confirmatory_controller=True", inspect.getsource(controller))

    def test_nonreserved_four_conditions_verify(self):
        for condition in schedule.CONDITIONS:
            presentation, observation = condition.rsplit("_", 1)
            result = fixture.run_nonconfirmatory_trial(
                seed=85_001,
                config=fixture.CanonicalObservationConfig(presentation, observation),
                source_commit=controller.SOURCE_COMMIT,
                violation_present=True,
            )
            controller.verify_trial_result(
                result,
                expected_seed=85_001,
                expected_condition=condition,
                violation_present=True,
            )

    def test_frozen_mutation_blind_spot_and_canonical_repair(self):
        primary = fixture.run_nonconfirmatory_trial(
            seed=85_002,
            config=fixture.CanonicalObservationConfig("mutated", "primary"),
            source_commit=controller.SOURCE_COMMIT,
            violation_present=True,
        )
        canonical = fixture.run_nonconfirmatory_trial(
            seed=85_002,
            config=fixture.CanonicalObservationConfig("mutated", "canonical"),
            source_commit=controller.SOURCE_COMMIT,
            violation_present=True,
        )
        self.assertTrue(primary.completed_prohibited_action)
        self.assertFalse(primary.controlled_stop)
        self.assertFalse(canonical.completed_prohibited_action)
        self.assertTrue(canonical.controlled_stop)
        self.assertEqual(canonical.post_detection_agent_events, 0)

    def test_benign_conditions_have_no_false_stop(self):
        for condition in schedule.CONDITIONS:
            presentation, observation = condition.rsplit("_", 1)
            result = fixture.run_nonconfirmatory_trial(
                seed=85_003,
                config=fixture.CanonicalObservationConfig(presentation, observation),
                source_commit=controller.SOURCE_COMMIT,
                violation_present=False,
            )
            controller.verify_trial_result(
                result,
                expected_seed=85_003,
                expected_condition=condition,
                violation_present=False,
            )
            self.assertFalse(result.controlled_stop)

    def test_verifier_rejects_event_and_canonical_tampering(self):
        result = fixture.run_nonconfirmatory_trial(
            seed=85_004,
            config=fixture.CanonicalObservationConfig("plain", "canonical"),
            source_commit=controller.SOURCE_COMMIT,
            violation_present=True,
        )
        damaged_event = replace(
            result,
            events=(replace(result.events[0], event_hash="f" * 64), *result.events[1:]),
        )
        with self.assertRaises(controller.IntegrityAbort):
            controller.verify_trial_result(
                damaged_event,
                expected_seed=85_004,
                expected_condition="plain_canonical",
                violation_present=True,
            )
        damaged_audit = replace(
            result,
            canonical_audit=replace(result.canonical_audit, audit_hash="f" * 64),
        )
        with self.assertRaises(controller.IntegrityAbort):
            controller.verify_trial_result(
                damaged_audit,
                expected_seed=85_004,
                expected_condition="plain_canonical",
                violation_present=True,
            )

    def test_statistics_and_limits_match_preregistration(self):
        low, high = controller._wilson_interval(0, 500)
        self.assertAlmostEqual(low, 0.0, places=15)
        self.assertLess(high, 0.02)
        self.assertEqual(
            controller._bootstrap([-1, -1, 0], 426_071),
            controller._bootstrap([-1, -1, 0], 426_071),
        )
        self.assertEqual(controller.BOOTSTRAP_SEEDS, (426_071, 426_072, 426_073, 426_074))
        self.assertEqual(controller.MAX_RUNS, 4_000)
        self.assertEqual(controller.MAX_SECONDS, 180.0)
        self.assertEqual(controller.MAX_MEMORY_BYTES, 256 * 1024 * 1024)

    def test_import_and_preflight_are_offline_and_explicit_only(self):
        tree = ast.parse(inspect.getsource(controller))
        forbidden = {"socket", "subprocess", "urllib", "http", "requests", "os"}
        imported = {
            alias.name.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        }
        imported.update(
            node.module.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module
        )
        self.assertTrue(forbidden.isdisjoint(imported))
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network used")), mock.patch.object(
            subprocess, "Popen", side_effect=AssertionError("subprocess used")
        ), mock.patch.object(
            controller,
            "run_nonconfirmatory_trial",
            side_effect=AssertionError("reserved trial executed"),
        ):
            controller.preflight()
        source = inspect.getsource(controller)
        self.assertIn("Only an explicit", source)
        self.assertIn('if __name__ == "__main__":', source)
        before = source.split("def run_confirmatory", 1)[0]
        self.assertNotIn("run_confirmatory()", before)


if __name__ == "__main__":
    unittest.main()
