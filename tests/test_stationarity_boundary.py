import unittest
from src.stationarity_boundary import refine_boundary

class StationarityBoundaryTests(unittest.TestCase):
    def test_reversal_boundary_is_bracketed(self):
        b=refine_boundary('reversal_bias',(0.0,0.01,0.02,0.03,0.05),trials=2000)
        self.assertIsNotNone(b.last_passing_shift)
        self.assertIsNotNone(b.first_failing_shift)
        self.assertLess(b.last_passing_shift,b.first_failing_shift)
        self.assertLessEqual(b.last_passing_fpr,0.02)
        self.assertGreater(b.first_failing_fpr,0.02)

    def test_combined_reports_conservative_bracket_or_open_upper(self):
        b=refine_boundary('combined',(0.0,0.005,0.01,0.02,0.05),trials=1000)
        self.assertIsNotNone(b.last_passing_shift)
        if b.first_failing_shift is not None:
            self.assertLess(b.last_passing_shift,b.first_failing_shift)

    def test_grid_validation(self):
        with self.assertRaises(ValueError):
            refine_boundary('sigma',(0.0,0.0),trials=1000)

if __name__=='__main__': unittest.main()
