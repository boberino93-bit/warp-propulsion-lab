import math, unittest
from src.noncontact_calibration import magnetic_force,magnetic_force_uncertainty,cross_calibration_z,cross_calibration_gate
class T(unittest.TestCase):
 def test_linear(self): self.assertAlmostEqual(magnetic_force(.1,.01),1e-3); self.assertAlmostEqual(magnetic_force(-.1,.01),-1e-3)
 def test_range(self): self.assertAlmostEqual(magnetic_force(.01,.01),1e-4); self.assertAlmostEqual(magnetic_force(.1,.01),1e-3)
 def test_unc(self): self.assertAlmostEqual(magnetic_force_uncertainty(.1,1e-5,.01,1e-5),math.sqrt((.01e-5)**2+(.1e-5)**2))
 def test_exact(self): self.assertEqual(cross_calibration_z(1e-3,1e-6,1e-3,1e-7),0); self.assertTrue(cross_calibration_gate(1e-3,1e-6,1e-3,1e-7))
 def test_sign(self): self.assertFalse(cross_calibration_gate(-1e-3,1e-6,1e-3,1e-7))
 def test_bias(self): self.assertFalse(cross_calibration_gate(1.06e-3,1e-3,1e-3,1e-3))
 def test_z(self): self.assertFalse(cross_calibration_gate(1.02e-3,1e-6,1e-3,1e-7))
 def test_rep(self): self.assertLess(abs(cross_calibration_z(1.001e-3,1e-7,1e-3,1e-7,1e-6)),abs(cross_calibration_z(1.001e-3,1e-7,1e-3,1e-7,0)))
 def test_bad(self):
  with self.assertRaises(ValueError): magnetic_force(1,0)
