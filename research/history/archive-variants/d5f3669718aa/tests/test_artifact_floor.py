import math, unittest
from src.artifact_floor import combined_random_sigma, systematic_artifact_bound, minimum_detectable_thrust, artifact_corrected_snr, candidate_is_eligible

class ArtifactFloorTests(unittest.TestCase):
    def test_quadrature_random(self): self.assertAlmostEqual(combined_random_sigma(3e-6,4e-6),5e-6)
    def test_systematics_do_not_cancel(self): self.assertAlmostEqual(systematic_artifact_bound(2e-6,3e-6,1e-6),6e-6)
    def test_mdt(self): self.assertAlmostEqual(minimum_detectable_thrust(5e-6,10e-6),35e-6)
    def test_corrected_snr(self): self.assertAlmostEqual(artifact_corrected_snr(35e-6,5e-6,10e-6),5.0)
    def test_inside_systematic_bound_zero_snr(self): self.assertEqual(artifact_corrected_snr(8e-6,5e-6,10e-6),0.0)
    def test_eligible(self): self.assertTrue(candidate_is_eligible(40e-6,5e-6,10e-6))
    def test_reject_below_mdt(self): self.assertFalse(candidate_is_eligible(34e-6,5e-6,10e-6))
    def test_reject_if_floor_exceeds_0p1mn_calibration(self): self.assertFalse(candidate_is_eligible(200e-6,20e-6,10e-6))
    def test_bad(self):
        with self.assertRaises(ValueError): combined_random_sigma(-1)
        with self.assertRaises(ValueError): artifact_corrected_snr(1,0,0)
