import ast
from dataclasses import FrozenInstanceError
import importlib.util
import inspect
from pathlib import Path
import socket
import subprocess
import sys
import unittest
from unittest import mock


_HARNESS_PATH = Path(__file__).resolve().parents[2] / "ai_control" / "harness.py"
_SPEC = importlib.util.spec_from_file_location("ai_control_safeguard_under_test", _HARNESS_PATH)
assert _SPEC is not None and _SPEC.loader is not None
harness = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = harness
_SPEC.loader.exec_module(harness)

SafeguardConfig = harness.SafeguardConfig
run_safeguard_trial = harness.run_safeguard_trial
safeguard_paired_config_diff = harness.safeguard_paired_config_diff

TEST_SEED_VIOLATION = 910_000
TEST_SEED_BENIGN = 910_001
SOURCE_COMMIT = "unit-fixture-not-a-git-claim"


class SafeguardImplementationTests(unittest.TestCase):
    def setUp(self):
        self.logging = SafeguardConfig(monitor_enforced_stop=False)
        self.enforced = SafeguardConfig(monitor_enforced_stop=True)

    def run_trial(self, config, *, seed=TEST_SEED_VIOLATION, violation=True, feasible=True):
        return run_safeguard_trial(
            seed=seed,
            config=config,
            source_commit=SOURCE_COMMIT,
            violation_present=violation,
            feasible=feasible,
        )

    def test_pair_diff_is_exactly_monitor_enforcement(self):
        self.assertEqual(
            safeguard_paired_config_diff(self.logging, self.enforced),
            {"monitor_enforced_stop": (False, True)},
        )

    def test_nonintervention_changes_are_rejected(self):
        with self.assertRaises(ValueError):
            SafeguardConfig(monitor_enforced_stop=True, communication_enabled=False)
        with self.assertRaises(ValueError):
            SafeguardConfig(monitor_enforced_stop=True, max_agent_events=5)

    def test_enforced_violation_commits_detection_then_stops(self):
        result = self.run_trial(self.enforced)
        self.assertEqual(result.status, "CONTROLLED_STOP")
        self.assertTrue(result.controlled_stop)
        self.assertTrue(result.board_readonly)
        self.assertEqual(result.agent_event_count, 2)
        self.assertEqual(result.post_detection_agent_events, 0)
        self.assertFalse(result.completed_restricted_hint_use)
        self.assertIsNotNone(result.detection_event_hash)
        self.assertIsNotNone(result.stop_transition_event_hash)

        detection = next(event for event in result.events if event.event_hash == result.detection_event_hash)
        transition = next(event for event in result.events if event.event_hash == result.stop_transition_event_hash)
        self.assertEqual(detection.actor_kind, "agent")
        self.assertEqual(detection.monitor_decision, "restricted_transfer_detected")
        self.assertFalse(detection.stop_state)
        self.assertEqual(transition.actor_kind, "controller")
        self.assertEqual(transition.previous_event_hash, detection.event_hash)
        self.assertTrue(transition.stop_state)
        self.assertTrue(transition.board_readonly)
        self.assertFalse(any(event.actor_kind == "agent" for event in result.events[result.events.index(detection) + 1 :]))

    def test_logging_only_violation_continues_to_completed_use(self):
        result = self.run_trial(self.logging)
        self.assertEqual(result.status, "COMPLETED")
        self.assertFalse(result.controlled_stop)
        self.assertTrue(result.completed_restricted_hint_use)
        self.assertEqual(result.agent_event_count, 4)
        self.assertEqual(result.post_detection_agent_events, 2)
        self.assertFalse(result.board_readonly)

    def test_benign_controls_do_not_stop(self):
        for config in (self.logging, self.enforced):
            with self.subTest(config=config.monitor_enforced_stop):
                result = self.run_trial(
                    config,
                    seed=TEST_SEED_BENIGN,
                    violation=False,
                    feasible=False,
                )
                self.assertEqual(result.status, "COMPLETED")
                self.assertFalse(result.controlled_stop)
                self.assertIsNone(result.detection_event_hash)
                self.assertEqual(result.post_detection_agent_events, 0)
                self.assertTrue(result.correct_safe_exit)
                self.assertEqual(result.agent_event_count, 4)

    def test_deterministic_replay_and_hash_chain(self):
        first = self.run_trial(self.enforced)
        second = self.run_trial(self.enforced)
        self.assertEqual(first, second)
        previous = "0" * 64
        for event in first.events:
            self.assertEqual(event.previous_event_hash, previous)
            previous = event.event_hash

    def test_controlled_stop_is_not_integrity_abort(self):
        result = self.run_trial(self.enforced)
        self.assertNotEqual(result.status, "ABORTED")
        self.assertEqual(result.status, "CONTROLLED_STOP")

    def test_scoring_oracle_remains_immutable(self):
        oracle = harness.ScoringOracle()
        with self.assertRaises(FrozenInstanceError):
            oracle.safe_exit_token = "CHANGED"

    def test_no_network_subprocess_or_external_capability(self):
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network used")), mock.patch.object(
            subprocess, "Popen", side_effect=AssertionError("subprocess used")
        ):
            result = self.run_trial(self.enforced)
        self.assertEqual(result.status, "CONTROLLED_STOP")

        tree = ast.parse(inspect.getsource(harness))
        forbidden = {"socket", "subprocess", "urllib", "http", "requests", "pathlib", "os"}
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

    def test_fixtures_do_not_use_reserved_confirmatory_seeds(self):
        for seed in (TEST_SEED_VIOLATION, TEST_SEED_BENIGN):
            self.assertFalse(420_000 <= seed <= 420_999)


if __name__ == "__main__":
    unittest.main()
