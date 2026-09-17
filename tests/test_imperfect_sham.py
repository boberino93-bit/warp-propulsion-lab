import unittest
from src.imperfect_sham import evaluate_imperfect_sham

class TestImperfectSham(unittest.TestCase):
    def test_matched_sham_controls_null(self):
        r=evaluate_imperfect_sham(0.0,trials=1000)
        self.assertLess(r.false_positive_rate,0.01)
    def test_severe_mismatch_breaks_gate(self):
        r=evaluate_imperfect_sham(0.95,trials=1000)
        self.assertGreater(r.false_positive_rate,0.05)
    def test_signal_survives_reasonable_match(self):
        r=evaluate_imperfect_sham(0.5,trials=1000)
        self.assertGreater(r.detection_rate,0.95)

if __name__ == '__main__': unittest.main()
