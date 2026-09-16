import unittest
from src.accelerating_energy_local import energy_time_accel,kij_sij_accel,local_accel_residual,gaussian_integrated_accel_term
from src.accelerating_energy_power import gaussian_acceleration_power

class TestAcceleratingEnergyLocal(unittest.TestCase):
    def test_pointwise_closure(self): self.assertAlmostEqual(local_accel_residual(0.7,0.12,0.31,-0.22),0.0,places=15)
    def test_nonzero_channels_equal(self):
        lhs=energy_time_accel(0.7,0.12,0.31,-0.22); rhs=kij_sij_accel(0.7,0.12,0.31,-0.22)
        self.assertNotEqual(lhs,0.0); self.assertAlmostEqual(lhs,rhs,places=15)
    def test_reversal_signs(self):
        base=energy_time_accel(0.4,0.2,0.3,0.1)
        self.assertAlmostEqual(energy_time_accel(-0.4,0.2,0.3,0.1),-base)
        self.assertAlmostEqual(energy_time_accel(0.4,-0.2,0.3,0.1),-base)
    def test_integrated_matches_inventory_derivative(self):
        for v,a,s in [(0.2,0.03,0.8),(0.7,-0.1,1.4),(-0.4,0.2,2.0)]:
            self.assertAlmostEqual(gaussian_integrated_accel_term(v,a,s),gaussian_acceleration_power(v,a,s),places=15)
    def test_scale_and_invalid_sigma(self):
        x=gaussian_integrated_accel_term(0.3,0.2,1.0)
        self.assertAlmostEqual(gaussian_integrated_accel_term(0.3,0.2,2.0),2*x)
        with self.assertRaises(ValueError): gaussian_integrated_accel_term(0.3,0.2,0.0)
