import unittest
from src.medium import top_hat_shape, stationary_dust_density, relative_mass_flux

class DustToyChecks(unittest.TestCase):
    def test_profile_symmetry_and_bounds(self):
        for xi in (0,0.1,2,5,20):
            f=top_hat_shape(xi,5,2)
            self.assertGreaterEqual(f,0.0)
            self.assertLess(f,1.0)
            self.assertAlmostEqual(f,top_hat_shape(-xi,5,2))
    def test_flat_limit(self):
        self.assertEqual(stationary_dust_density(2.0,0),2.0)
    def test_steady_flux_is_constant(self):
        rho0, vs = 1.225, 100.0
        for xi in (-100,-20,-8,-5,-2,0,2,5,8,20,100):
            f=top_hat_shape(xi,5,2)
            rho=stationary_dust_density(rho0,f)
            self.assertAlmostEqual(relative_mass_flux(rho,f,vs), -rho0*vs, places=8)
    def test_finite_difference_steady_continuity_residual(self):
        rho0, vs, h=1.225, 100.0, 0.001
        def flux(x):
            f=top_hat_shape(x,5,2)
            return relative_mass_flux(stationary_dust_density(rho0,f),f,vs)
        for x in (-9,-4,0,4,9):
            self.assertLess(abs((flux(x+h)-flux(x-h))/(2*h)),1e-7)
    def test_singularity_guard(self):
        for f in (1.0,1.1,-0.1):
            with self.assertRaises(ValueError): stationary_dust_density(1,f)
    def test_approaching_one_grows_without_bounded_limit(self):
        self.assertAlmostEqual(stationary_dust_density(1,0.9),10)
        self.assertAlmostEqual(stationary_dust_density(1,0.99),100)
    def test_invalid_shape(self):
        with self.assertRaises(ValueError): top_hat_shape(0,0,1)
        with self.assertRaises(ValueError): top_hat_shape(0,1,0)

if __name__ == '__main__': unittest.main()
