import unittest
from src.mechanical_force_calibration import *
class MechanicalForceCalibrationTests(unittest.TestCase):
 def test_target_mass_range(self):
  self.assertAlmostEqual(required_mass_for_force(1e-4,9.80665,1.2,8000)*1e6,10.1987,places=3); self.assertAlmostEqual(required_mass_for_force(1e-3,9.80665,1.2,8000)*1e6,101.987,places=2)
 def test_buoyancy_reduces_force(self):
  v=deadweight_force(1e-4,9.80665); a=deadweight_force(1e-4,9.80665,1.2,8000); self.assertLess(a,v); self.assertAlmostEqual((v-a)/v,1.2/8000,places=12)
 def test_sign_reversal(self): self.assertEqual(deadweight_force(5e-5,9.80665,sign=1),-deadweight_force(5e-5,9.80665,sign=-1))
 def test_uncertainty_positive_and_small_for_example(self):
  f=deadweight_force(1.01987e-4,9.80665,1.2,8000); s=deadweight_force_uncertainty(1.01987e-4,1e-8,9.80665,1e-5,1.2,.02,8000,100); self.assertGreater(s,0); self.assertLess(s/f,2e-4)
 def test_exact_recovery(self): self.assertEqual(recovery_z(1e-3,1e-5,1e-3,1e-7),0); self.assertTrue(bidirectional_gate(1e-3,-1e-3,1e-5,1e-3,1e-7))
 def test_wrong_sign_or_bias_fails(self): self.assertFalse(bidirectional_gate(1e-3,1e-3,1e-5,1e-3,1e-7)); self.assertFalse(bidirectional_gate(1.06e-3,-1e-3,1e-3,1e-3,1e-7))
 def test_transfer_uncertainty_is_explicit(self): self.assertGreater(abs(recovery_z(1.03e-3,1e-6,1e-3,1e-7,0)),abs(recovery_z(1.03e-3,1e-6,1e-3,1e-7,2e-5)))
 def test_invalid(self):
  with self.assertRaises(ValueError): required_mass_for_force(-1,9.8)
  with self.assertRaises(ValueError): deadweight_force(1e-4,9.8,sign=0)
if __name__=='__main__': unittest.main()
