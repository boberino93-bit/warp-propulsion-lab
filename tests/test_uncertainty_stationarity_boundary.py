import unittest
from src.uncertainty_stationarity_boundary import scan_uncertainty_boundary

class TestUncertaintyStationarityBoundary(unittest.TestCase):
    def test_invalid_grid(self):
        with self.assertRaises(ValueError):
            scan_uncertainty_boundary("sigma", (0.01, 0.01), trials=100)

    def test_reversal_bracket_is_uncertainty_aware(self):
        pts, bracket = scan_uncertainty_boundary(
            "reversal_bias", (0.0, 0.0025, 0.005, 0.01, 0.02), trials=1000)
        for p in pts:
            self.assertEqual(p.passes, p.wilson_upper_fpr <= 0.02)
        if bracket.last_passing is not None:
            self.assertLessEqual(bracket.last_passing.wilson_upper_fpr, 0.02)
        if bracket.first_failing is not None:
            self.assertGreater(bracket.first_failing.wilson_upper_fpr, 0.02)

    def test_combined_bracket_is_ordered(self):
        _, bracket = scan_uncertainty_boundary(
            "combined", (0.0, 0.001, 0.0025, 0.005, 0.01), trials=1000)
        if bracket.last_passing and bracket.first_failing:
            self.assertLess(bracket.last_passing.shift, bracket.first_failing.shift)

if __name__ == "__main__":
    unittest.main()
