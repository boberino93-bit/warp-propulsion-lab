import unittest
from src.blinded_campaign import campaign_threshold_n, monte_carlo_campaign

class TestBlindedCampaign(unittest.TestCase):
    def test_threshold(self):
        self.assertAlmostEqual(campaign_threshold_n(5e-6, 10e-6, 16), 14.419417382415922e-6)
    def test_invalid(self):
        with self.assertRaises(ValueError): campaign_threshold_n(0, 1e-6, 1)
    def test_null_false_positive_predeclared(self):
        r = monte_carlo_campaign(0, 5e-6, 10e-6, trials=20000)
        self.assertLessEqual(r.false_positive_rate, 5e-4)
    def test_35_microN_detects(self):
        r = monte_carlo_campaign(35e-6, 5e-6, 10e-6, trials=20000)
        self.assertGreaterEqual(r.detection_rate, 0.999)
    def test_below_campaign_threshold_fails_often(self):
        r = monte_carlo_campaign(10e-6, 5e-6, 10e-6, trials=20000)
        self.assertLess(r.detection_rate, 0.01)
    def test_reproducible(self):
        a = monte_carlo_campaign(15e-6, 5e-6, 10e-6, trials=1000, seed=7)
        b = monte_carlo_campaign(15e-6, 5e-6, 10e-6, trials=1000, seed=7)
        self.assertEqual(a, b)

if __name__ == '__main__': unittest.main()

class TestBlindSchedule(unittest.TestCase):
    def test_balanced_randomized_schedule(self):
        from src.blinded_campaign import randomized_blind_schedule
        s = randomized_blind_schedule(8, seed=1)
        labels = [x[1] for x in s]
        self.assertEqual(len(s), 32)
        for c in ("ON+", "ON-", "OFF", "SHAM"):
            self.assertEqual(labels.count(c), 8)
        self.assertNotEqual(labels, [c for c in ("ON+", "ON-", "OFF", "SHAM") for _ in range(8)])
