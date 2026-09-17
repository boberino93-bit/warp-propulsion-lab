import unittest

from src.reversal_sham import evaluate_reversal_sham, reversal_sham_schedule


class ReversalShamTests(unittest.TestCase):
    def test_schedule_balanced(self):
        labels = [label for _, label in reversal_sham_schedule(repeats=4)]
        for state in ("ON+", "ON-", "SHAM+", "SHAM-", "OFF"):
            self.assertEqual(labels.count(state), 4)

    def test_matched_sham_rejects_reversal_artifact(self):
        result = evaluate_reversal_sham(force_n=0.0, reversal_bias_n=20e-6,
                                        rho=0.9, trials=2000)
        self.assertGreater(result.raw_false_positive_rate, 0.95)
        self.assertLess(result.corrected_false_positive_rate, 0.01)

    def test_true_force_survives_sham_subtraction(self):
        result = evaluate_reversal_sham(force_n=20e-6, reversal_bias_n=15e-6,
                                        rho=0.9, trials=2000)
        self.assertGreater(result.corrected_detection_rate, 0.99)

    def test_invalid_rho_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_reversal_sham(rho=1.0, trials=1)


if __name__ == "__main__":
    unittest.main()
