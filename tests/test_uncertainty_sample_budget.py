import unittest

from theory.uncertainty_sample_budget import max_passing_false_positives


class TestUncertaintySampleBudget(unittest.TestCase):
    def test_1000_trials(self):
        r = max_passing_false_positives(1000)
        self.assertEqual(r["max_false_positives"], 11)
        self.assertLessEqual(r["upper_fpr"], 0.02)

    def test_10000_trials(self):
        r = max_passing_false_positives(10000)
        self.assertEqual(r["max_false_positives"], 172)
        self.assertAlmostEqual(r["max_point_fpr"], 0.0172)

    def test_more_trials_allow_point_estimate_closer_to_ceiling(self):
        a = max_passing_false_positives(1000)
        b = max_passing_false_positives(50000)
        self.assertGreater(b["max_point_fpr"], a["max_point_fpr"])

    def test_too_few_trials_can_fail_even_at_zero(self):
        r = max_passing_false_positives(10)
        self.assertEqual(r["max_false_positives"], -1)

    def test_invalid_trials(self):
        with self.assertRaises(ValueError):
            max_passing_false_positives(0)


if __name__ == "__main__":
    unittest.main()
