import unittest

from artifact_stress import stress_false_positive_rate


class ArtifactStressTests(unittest.TestCase):
    def test_clean_null_remains_below_gate(self):
        result = stress_false_positive_rate(trials=2000, seed=320)
        self.assertEqual(result.false_positive_rate, 0.0)

    def test_reversal_bias_can_mimic_signal(self):
        result = stress_false_positive_rate(reversal_bias_n=20e-6, trials=2000, seed=320)
        self.assertGreater(result.false_positive_rate, 0.99)

    def test_time_correlation_exposes_nominal_bound(self):
        independent = stress_false_positive_rate(rho=0.0, reversal_bias_n=10e-6, trials=5000, seed=320)
        correlated = stress_false_positive_rate(rho=0.9, reversal_bias_n=10e-6, trials=5000, seed=320)
        self.assertLess(independent.false_positive_rate, 0.005)
        self.assertGreater(correlated.false_positive_rate, 0.03)

    def test_invalid_rho_rejected(self):
        with self.assertRaises(ValueError):
            stress_false_positive_rate(rho=1.0, trials=1)


if __name__ == "__main__":
    unittest.main()
