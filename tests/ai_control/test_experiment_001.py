import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


_ROOT = Path(__file__).resolve().parents[2]
_HARNESS_SPEC = importlib.util.spec_from_file_location("ai_control.harness", _ROOT / "ai_control" / "harness.py")
assert _HARNESS_SPEC is not None and _HARNESS_SPEC.loader is not None
_HARNESS = importlib.util.module_from_spec(_HARNESS_SPEC)
sys.modules[_HARNESS_SPEC.name] = _HARNESS
_HARNESS_SPEC.loader.exec_module(_HARNESS)
_EXPERIMENT_SPEC = importlib.util.spec_from_file_location("experiment_001_under_test", _ROOT / "ai_control" / "experiment_001.py")
assert _EXPERIMENT_SPEC is not None and _EXPERIMENT_SPEC.loader is not None
experiment = importlib.util.module_from_spec(_EXPERIMENT_SPEC)
sys.modules[_EXPERIMENT_SPEC.name] = experiment
_EXPERIMENT_SPEC.loader.exec_module(experiment)


class Experiment001Tests(unittest.TestCase):
    def test_wilson_extremes(self):
        zero = experiment.wilson_interval(0, 1000)
        one = experiment.wilson_interval(1000, 1000)
        self.assertAlmostEqual(zero[0], 0.0)
        self.assertLess(zero[1], 0.004)
        self.assertGreater(one[0], 0.996)
        self.assertAlmostEqual(one[1], 1.0)

    def test_paired_bootstrap_constant_difference(self):
        self.assertEqual(experiment.paired_bootstrap_interval([1, 1, 1]), (1.0, 1.0))

    def test_nonreserved_small_block_validates_and_writes(self):
        seeds = [900_010, 900_011]
        result = experiment.run_block(seeds)
        self.assertEqual(result["pair_count"], 2)
        self.assertEqual(result["event_count"], 16)
        self.assertEqual(result["primary"]["point_estimate"], 1.0)
        self.assertEqual(result["arms"]["board_disabled"]["metrics"]["compliant_task_success"]["trials"], 1)
        self.assertEqual(result["arms"]["board_disabled"]["metrics"]["compliant_task_success"]["rate"], 1.0)
        self.assertEqual(result["arms"]["board_disabled"]["metrics"]["correct_safe_exit"]["trials"], 1)
        self.assertEqual(result["monitoring"]["completed_transfer_detection"]["sensitivity"], 1.0)
        self.assertEqual(result["monitoring"]["no_transfer_false_alarms"]["rate"], 0.0)
        self.assertEqual(result["monitoring"]["safe_exit_after_first_detected_violation"]["events_to_safe_exit"], [])
        with tempfile.TemporaryDirectory() as directory:
            paths = experiment.write_outputs(result, Path(directory))
            summary = json.loads(paths["summary"].read_text())
            self.assertEqual(summary["pair_count"], 2)
            self.assertTrue(paths["events"].read_text().endswith("\n"))

    def test_fixture_seeds_do_not_overlap_confirmatory_block(self):
        self.assertTrue(all(not 390_000 <= seed <= 390_999 for seed in (900_010, 900_011)))


if __name__ == "__main__":
    unittest.main()
