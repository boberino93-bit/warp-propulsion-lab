import unittest
from src.stationarity_envelope import scan_one_parameter, scan_combined, last_passing

class StationarityEnvelopeTests(unittest.TestCase):
    def test_reversal_shift_crosses_two_percent_ceiling(self):
        pts=scan_one_parameter('reversal_bias', shifts=(0.0,0.02,0.05,0.10), trials=1000)
        self.assertTrue(pts[0].passes)
        self.assertTrue(any(not p.passes for p in pts[1:]))

    def test_combined_shift_is_reported_not_assumed_safe(self):
        pts=scan_combined(shifts=(0.0,0.02,0.05), trials=1000)
        self.assertEqual(len(pts),3)
        self.assertIsNotNone(last_passing(pts))

    def test_invalid(self):
        with self.assertRaises(ValueError): scan_one_parameter('bogus',trials=1000)

if __name__=='__main__': unittest.main()
