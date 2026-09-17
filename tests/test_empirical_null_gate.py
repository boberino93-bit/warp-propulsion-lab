import unittest
from src.empirical_null_gate import evaluate_empirical_null_gate

class EmpiricalNullGateTests(unittest.TestCase):
    def test_holdout_false_positive_near_preregistered_alpha(self):
        r=evaluate_empirical_null_gate(0.90,calibration_trials=1200,holdout_trials=1200,alpha=0.01,seed=324)
        self.assertLessEqual(r.false_positive_rate,0.03)
        self.assertGreater(r.threshold_n,0)

    def test_signal_retention_is_reported_not_assumed(self):
        r=evaluate_empirical_null_gate(0.90,force_n=20e-6,calibration_trials=1200,holdout_trials=1200,alpha=0.01,seed=325)
        self.assertGreater(r.detection_rate,0.50)

    def test_invalid_parameters_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_empirical_null_gate(1.1)

if __name__ == '__main__':
    unittest.main()
