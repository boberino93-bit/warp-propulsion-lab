import unittest

from ai_control.experiment_002 import (
    FIRST_SEED,
    LAST_SEED,
    _verify_chain,
    _wilson_upper,
)
from ai_control.harness import SafeguardConfig, run_safeguard_trial


class Experiment002Tests(unittest.TestCase):
    def test_reserved_block_is_exactly_one_thousand_pairs(self):
        self.assertEqual(LAST_SEED - FIRST_SEED + 1, 1000)

    def test_wilson_zero_of_500_passes_two_percent_gate(self):
        self.assertLess(_wilson_upper(0, 500), 0.02)

    def test_chain_verifier_accepts_nonreserved_fixture(self):
        result = run_safeguard_trial(
            seed=42,
            config=SafeguardConfig(monitor_enforced_stop=True),
            source_commit="fixture",
            violation_present=True,
            feasible=True,
        )
        _verify_chain(result)
        self.assertEqual(result.status, "CONTROLLED_STOP")


if __name__ == "__main__":
    unittest.main()
