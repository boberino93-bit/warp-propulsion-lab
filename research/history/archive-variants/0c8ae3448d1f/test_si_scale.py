import unittest, math
from si_scale import *
class TestSI(unittest.TestCase):
 def test_zero_speed(self): self.assertEqual(energy_j(1,0),0)
 def test_velocity_reversal(self): self.assertEqual(energy_j(1,10),energy_j(1,-10))
 def test_scaling(self): self.assertAlmostEqual(energy_j(10,1000)/energy_j(1,100),1000)
 def test_power_scaling(self): self.assertAlmostEqual(inventory_rate_w(10,1000,10)/inventory_rate_w(1,100,1),1000)
 def test_derivative(self):
  v=100.;h=.001
  fd=(energy_j(1,v+h)-energy_j(1,v-h))/(2*h)
  self.assertAlmostEqual(fd/inventory_rate_w(1,v,1),1,places=10)
 def test_invalid(self):
  with self.assertRaises(ValueError): energy_j(0,1)
  with self.assertRaises(ValueError): inventory_rate_w(1,1,float('nan'))
if __name__=='__main__':unittest.main()
