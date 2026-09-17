import unittest
from src.accelerating_energy_power import gaussian_total_energy, gaussian_acceleration_power

class TestAcceleratingEnergyPower(unittest.TestCase):
    def test_matches_centered_velocity_derivative(self):
        v,a,s=0.37,-0.021,2.4
        h=1e-6
        numeric=(gaussian_total_energy(v+a*h,s)-gaussian_total_energy(v-a*h,s))/(2*h)
        self.assertAlmostEqual(numeric, gaussian_acceleration_power(v,a,s), places=10)
    def test_zero_for_no_acceleration_or_rest(self):
        self.assertEqual(gaussian_acceleration_power(1.2,0,3),0)
        self.assertEqual(gaussian_acceleration_power(0,1.2,3),0)
    def test_joint_reversal(self):
        p=gaussian_acceleration_power(.4,.2,2)
        self.assertAlmostEqual(gaussian_acceleration_power(-.4,-.2,2),p)
        self.assertAlmostEqual(gaussian_acceleration_power(-.4,.2,2),-p)
    def test_linear_scale_and_dimensions(self):
        p=gaussian_acceleration_power(.4,.2,2)
        self.assertAlmostEqual(gaussian_acceleration_power(.4,.2,6),3*p)
    def test_invalid_scale(self):
        with self.assertRaises(ValueError): gaussian_acceleration_power(1,1,0)

if __name__ == '__main__': unittest.main()
