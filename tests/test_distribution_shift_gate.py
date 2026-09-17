import unittest
from src.distribution_shift_gate import evaluate_distribution_shift

class DistributionShiftGateTests(unittest.TestCase):
    def test_matched_holdout_near_nominal(self):
        r=evaluate_distribution_shift(holdout_trials=4000)
        self.assertLessEqual(r.false_positive_rate,0.025)
        self.assertGreaterEqual(r.detection_rate,0.95)

    def test_noise_shift_breaks_nominal_control(self):
        r=evaluate_distribution_shift(hold_sigma_n=7.5e-6,holdout_trials=4000)
        self.assertGreater(r.false_positive_rate,0.05)

    def test_reversal_bias_shift_is_severe(self):
        r=evaluate_distribution_shift(hold_reversal_bias_n=18.75e-6,holdout_trials=4000)
        self.assertGreater(r.false_positive_rate,0.50)

    def test_mismatch_shift_breaks_control(self):
        r=evaluate_distribution_shift(hold_mismatch=0.95,holdout_trials=4000)
        self.assertGreater(r.false_positive_rate,0.025)

    def test_validation(self):
        with self.assertRaises(ValueError): evaluate_distribution_shift(hold_mismatch=1.1)
        with self.assertRaises(ValueError): evaluate_distribution_shift(hold_sigma_n=0)

if __name__ == '__main__': unittest.main()
