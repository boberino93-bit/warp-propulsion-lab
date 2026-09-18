import importlib.util
from pathlib import Path
import sys
import unittest


_ROOT = Path(__file__).resolve().parents[2]
_HARNESS_SPEC = importlib.util.spec_from_file_location(
    "ai_control.harness", _ROOT / "ai_control" / "harness.py"
)
assert _HARNESS_SPEC is not None and _HARNESS_SPEC.loader is not None
harness = importlib.util.module_from_spec(_HARNESS_SPEC)
sys.modules[_HARNESS_SPEC.name] = harness
_HARNESS_SPEC.loader.exec_module(harness)

_EXPERIMENT_SPEC = importlib.util.spec_from_file_location(
    "ai_control_experiment_002_under_test",
    _ROOT / "ai_control" / "experiment_002.py",
)
assert _EXPERIMENT_SPEC is not None and _EXPERIMENT_SPEC.loader is not None
experiment = importlib.util.module_from_spec(_EXPERIMENT_SPEC)
sys.modules[_EXPERIMENT_SPEC.name] = experiment
_EXPERIMENT_SPEC.loader.exec_module(experiment)


class Experiment002Tests(unittest.TestCase):
    def test_reserved_block_is_exactly_one_thousand_pairs(self):
        self.assertEqual(experiment.LAST_SEED - experiment.FIRST_SEED + 1, 1000)

    def test_wilson_zero_of_500_passes_two_percent_gate(self):
        self.assertLess(experiment._wilson_upper(0, 500), 0.02)

    def test_chain_verifier_accepts_nonreserved_fixture(self):
        result = harness.run_safeguard_trial(
            seed=42,
            config=harness.SafeguardConfig(monitor_enforced_stop=True),
            source_commit="fixture",
            violation_present=True,
            feasible=True,
        )
        experiment._verify_chain(result)
        self.assertEqual(result.status, "CONTROLLED_STOP")


if __name__ == "__main__":
    unittest.main()
