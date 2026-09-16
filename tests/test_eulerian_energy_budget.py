import math, unittest
from src.eulerian_energy_budget import local_energy_density, integrated_gaussian_energy

class EulerianEnergyBudgetTests(unittest.TestCase):
    def test_nonpositive_and_axis_zero(self):
        self.assertEqual(local_energy_density(.4,0,0,1.2,.6),0.0)
        self.assertLess(local_energy_density(0,.4,0,1.2,.6),0.0)
    def test_velocity_square_and_reversal(self):
        e=integrated_gaussian_energy(1.1,.3)
        self.assertAlmostEqual(integrated_gaussian_energy(1.1,-.3),e,14)
        self.assertAlmostEqual(integrated_gaussian_energy(1.1,.6),4*e,14)
    def test_linear_length_scaling(self):
        e=integrated_gaussian_energy(1.0,.5)
        self.assertAlmostEqual(integrated_gaussian_energy(2.0,.5),2*e,14)
    def test_independent_numerical_volume_integral(self):
        s,v=1.0,.4; L=4.5; n=360
        dx=2*L/n; dr=L/n; total=0.0
        for i in range(n):
            x=-L+(i+.5)*dx
            for j in range(n):
                r=(j+.5)*dr
                f2=math.exp(-2*(x*x+r*r)/(s*s))
                E=-(v*v)*r*r*f2/(8*math.pi*s**4)
                total += E*(2*math.pi*r*dr*dx)
        self.assertAlmostEqual(total,integrated_gaussian_energy(s,v),delta=2e-6)
    def test_invalid_scale(self):
        with self.assertRaises(ValueError): integrated_gaussian_energy(0,.2)
