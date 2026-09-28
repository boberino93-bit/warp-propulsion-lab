from dataclasses import asdict, replace
import ast
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import socket
import subprocess
import sys
import unittest
from unittest import mock

_ROOT = Path(__file__).resolve().parents[2]

_HARNESS_PATH = _ROOT / "ai_control" / "harness.py"
_HARNESS_SPEC = importlib.util.spec_from_file_location(
    "dropout_005_controller_harness", _HARNESS_PATH
)
assert _HARNESS_SPEC is not None and _HARNESS_SPEC.loader is not None
harness = importlib.util.module_from_spec(_HARNESS_SPEC)
sys.modules[_HARNESS_SPEC.name] = harness
_HARNESS_SPEC.loader.exec_module(harness)

_SCHEDULE_PATH = _ROOT / "ai_control" / "dropout_005_schedule.py"
_SCHEDULE_SPEC = importlib.util.spec_from_file_location(
    "dropout_005_controller_schedule", _SCHEDULE_PATH
)
assert _SCHEDULE_SPEC is not None and _SCHEDULE_SPEC.loader is not None
schedule = importlib.util.module_from_spec(_SCHEDULE_SPEC)
sys.modules[_SCHEDULE_SPEC.name] = schedule
_SCHEDULE_SPEC.loader.exec_module(schedule)

_CONTROLLER_PATH = _ROOT / "ai_control" / "experiment_005.py"
_CONTROLLER_SPEC = importlib.util.spec_from_file_location(
    "dropout_005_controller_under_test", _CONTROLLER_PATH
)
assert _CONTROLLER_SPEC is not None and _CONTROLLER_SPEC.loader is not None

# Preserve the production import identities used inside experiment_005.
with mock.patch.dict(
    sys.modules,
    {
        "ai_control.harness": harness,
        "ai_control.dropout_005_schedule": schedule,
    },
):
    controller = importlib.util.module_from_spec(_CONTROLLER_SPEC)
    sys.modules[_CONTROLLER_SPEC.name] = controller
    _CONTROLLER_SPEC.loader.exec_module(controller)

FIXTURE_SEED = 910_041
SOURCE = "unit-fixture-not-a-git-claim"


class Dropout005ControllerTests(unittest.TestCase):
    def test_preflight_pins_blobs_schedule_and_reserved_identity_without_runs(self):
        with mock.patch.object(
            controller, "run_dropout_trial", side_effect=AssertionError("reserved run")
        ):
            result = controller.preflight()
        self.assertEqual(result["harness_blob"], controller.EXPECTED_HARNESS_BLOB)
        self.assertEqual(result["schedule_blob"], controller.EXPECTED_SCHEDULE_BLOB)
        self.assertEqual(result["schedule_sha256"], schedule.EXPECTED_SCHEDULE_SHA256)
        self.assertEqual(result["reserved_seed_first"], 422_000)
        self.assertEqual(result["reserved_seed_last"], 422_999)
        self.assertEqual(result["runs_if_explicitly_started"], 5_000)

    def test_preflight_aborts_on_blob_mismatch_before_reserved_runs(self):
        with mock.patch.object(
            controller, "_git_blob_sha", return_value="0" * 40
        ), mock.patch.object(
            controller, "run_dropout_trial", side_effect=AssertionError("reserved run")
        ):
            with self.assertRaises(controller.IntegrityAbort):
                controller.preflight()

    def test_observed_violation_fixture_passes_independent_integrity_check(self):
        result = harness.run_dropout_trial(
            seed=FIXTURE_SEED,
            config=harness.DropoutConfig(0),
            source_commit=SOURCE,
            violation_present=True,
            feasible=True,
        )
        controller.verify_trial_result(
            result,
            expected_seed=FIXTURE_SEED,
            expected_level_basis_points=0,
            violation_present=True,
            feasible=True,
        )

    def test_dropped_violation_fixture_passes_independent_integrity_check(self):
        self.assertTrue(schedule.observation_dropped(FIXTURE_SEED, 100))
        result = harness.run_dropout_trial(
            seed=FIXTURE_SEED,
            config=harness.DropoutConfig(100),
            source_commit=SOURCE,
            violation_present=True,
            feasible=False,
        )
        controller.verify_trial_result(
            result,
            expected_seed=FIXTURE_SEED,
            expected_level_basis_points=100,
            violation_present=True,
            feasible=False,
        )
        self.assertTrue(result.completed_restricted_hint_use)

    def test_artifact_verifier_rejects_tampered_event_hash(self):
        result = harness.run_dropout_trial(
            seed=FIXTURE_SEED,
            config=harness.DropoutConfig(0),
            source_commit=SOURCE,
            violation_present=True,
            feasible=True,
        )
        damaged = replace(
            result,
            events=(
                replace(result.events[0], event_hash="f" * 64),
                *result.events[1:],
            ),
        )
        with self.assertRaises(controller.IntegrityAbort):
            controller.verify_trial_result(
                damaged,
                expected_seed=FIXTURE_SEED,
                expected_level_basis_points=0,
                violation_present=True,
                feasible=True,
            )

    def test_artifact_verifier_rejects_level_or_label_substitution(self):
        result = harness.run_dropout_trial(
            seed=FIXTURE_SEED,
            config=harness.DropoutConfig(100),
            source_commit=SOURCE,
            violation_present=True,
            feasible=True,
        )
        with self.assertRaises(controller.IntegrityAbort):
            controller.verify_trial_result(
                result,
                expected_seed=FIXTURE_SEED,
                expected_level_basis_points=500,
                violation_present=True,
                feasible=True,
            )

    def test_statistics_are_frozen_and_bounded(self):
        low, high = controller._wilson_interval(0, 500)
        self.assertAlmostEqual(low, 0.0, places=15)
        self.assertLess(high, 0.02)
        with self.assertRaises(controller.IntegrityAbort):
            controller._wilson_interval(0, 0)
        with self.assertRaises(controller.IntegrityAbort):
            controller._bootstrap_difference([], 100)

    def test_import_and_preflight_are_offline_and_do_not_execute_reserved_block(self):
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
        with mock.patch.object(
            socket, "socket", side_effect=AssertionError("network used")
        ), mock.patch.object(
            subprocess, "Popen", side_effect=AssertionError("subprocess used")
        ), mock.patch.object(
            controller, "run_dropout_trial", side_effect=AssertionError("reserved run")
        ):
            controller.preflight()

    def test_controller_source_contains_explicit_only_execution_boundary(self):
        source = inspect.getsource(controller)
        self.assertIn("Only an explicit run_confirmatory()", source)
        self.assertIn('if __name__ == "__main__":', source)
        self.assertNotIn("run_confirmatory()\n", source.split("def run_confirmatory", 1)[0])


if __name__ == "__main__":
    unittest.main()
