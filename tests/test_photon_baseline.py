import unittest
from src.photon_baseline import photon_thrust,power_for_thrust,snr,C
class PhotonBaseline(unittest.TestCase):
 def test_absorber(self): self.assertAlmostEqual(photon_thrust(1),1/C)
 def test_reflector(self): self.assertAlmostEqual(photon_thrust(1,1),2/C)
 def test_inverse(self): self.assertAlmostEqual(power_for_thrust(photon_thrust(250,1),1),250)
 def test_1kw_reflector(self): self.assertAlmostEqual(photon_thrust(1000,1)*1e6,6.671281903963041,places=9)
 def test_threshold(self): self.assertGreaterEqual(snr(photon_thrust(1000,1),1e-6),6.6)
 def test_bad(self):
  for args in [(-1,0),(1,-.1),(1,1.1)]: self.assertRaises(ValueError,photon_thrust,*args)
  self.assertRaises(ValueError,snr,1,0)
if __name__=='__main__': unittest.main()
