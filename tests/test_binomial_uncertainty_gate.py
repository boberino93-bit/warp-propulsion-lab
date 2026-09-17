import unittest

from theory.binomial_uncertainty_gate import false_positive_gate, wilson_upper


class BinomialUncertaintyGateTests(unittest.TestCase):
    def test_zero_false_positives_not_zero_upper_bound(self):
        self.assertGreater(wilson_upper(0, 1000), 0.0)

    def test_one_percent_at_1000_passes_two_percent_ceiling(self):
        result = false_positive_gate(10, 1000)
        self.assertTrue(result["passes"])
        self.assertLess(result["upper_fpr"], 0.02)

    def test_two_percent_point_rate_fails_two_percent_ceiling(self):
        result = false_positive_gate(20, 1000)
        self.assertFalse(result["passes"])
        self.assertGreater(result["upper_fpr"], 0.02)

    def test_small_sample_can_fail_despite_low_point_rate(self):
        result = false_positive_gate(1, 100)
        self.assertFalse(result["passes"])

    def test_invalid_counts_rejected(self):
        with self.assertRaises(ValueError):
            wilson_upper(2, 1)


if __name__ == "__main__":
    unittest.main()
