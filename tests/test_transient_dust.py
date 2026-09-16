"""Independent analytical invariant and numerical convergence tests for transient model."""
import math
import unittest

from src.medium import top_hat_shape
from src.transient_dust import evolve_characteristic, shape_gradient_per_m


class TransientDustChecks(unittest.TestCase):
    def setUp(self):
        self.params = dict(bubble_velocity_m_s=100.0,
                           upstream_density_kg_m3=1.225,
                           half_width_m=5.0, wall_m=2.0)

    def evolve(self, xi0=8.0, elapsed=0.04, steps=400):
        return evolve_characteristic(xi0, elapsed, steps=steps, **self.params)

    def test_initial_condition(self):
        state = self.evolve(elapsed=0)
        self.assertEqual(state.xi_m, 8.0)
        self.assertEqual(state.density_kg_m3, 1.225)
        self.assertEqual(state.jacobian, 1.0)

    def test_density_times_jacobian_is_initial_density(self):
        for xi0 in (-9, -3, 0, 3, 9):
            for t in (0.0, 0.01, 0.04):
                s = self.evolve(xi0, t)
                self.assertAlmostEqual(s.density_kg_m3*s.jacobian, 1.225, places=11)
                self.assertGreater(s.jacobian, 0)

    def test_independent_stationary_characteristic_invariant(self):
        """Analytic invariant of the continuum PDE, not the RK4 density equation."""
        for xi0 in (-9, -2, 0, 3, 9):
            initial_f = top_hat_shape(xi0, 5, 2)
            s = self.evolve(xi0, 0.04, 400)
            expected = 1.225 * (1-initial_f) / (1-s.f)
            self.assertAlmostEqual(s.density_kg_m3, expected, delta=1e-7)

    def test_gradient_matches_finite_difference(self):
        h = 1e-4
        for x in (-9, -4, 0, 4, 9):
            numerical = (top_hat_shape(x+h, 5, 2)-top_hat_shape(x-h, 5, 2))/(2*h)
            self.assertAlmostEqual(shape_gradient_per_m(x, 5, 2), numerical, delta=2e-9)

    def test_front_compression_not_global_instantaneous_steady_state(self):
        xi0 = 8
        s = self.evolve(xi0, elapsed=0.03)
        self.assertGreater(s.density_kg_m3, self.params['upstream_density_kg_m3'])
        instantaneous_steady = 1.225/(1-s.f)
        self.assertGreater(abs(s.density_kg_m3-instantaneous_steady), 0.01)

    def test_time_reversibility_and_no_density_creation(self):
        fwd = self.evolve(8, 0.04)
        back = evolve_characteristic(fwd.xi_m, -0.04, 100, fwd.density_kg_m3,
                                     5, 2, 400)
        self.assertAlmostEqual(back.xi_m, 8, delta=1e-9)
        self.assertAlmostEqual(back.density_kg_m3, 1.225, delta=1e-9)

    def test_zero_bubble_speed_gives_static_density(self):
        s = evolve_characteristic(8, 10, 0, 1.225, 5, 2)
        self.assertEqual(s.xi_m, 8)
        self.assertEqual(s.x_m, 8)
        self.assertEqual(s.density_kg_m3, 1.225)

    def test_rk4_step_convergence(self):
        reference = self.evolve(8, 0.06, 4096)
        e_coarse = abs(self.evolve(8, 0.06, 8).density_kg_m3 - reference.density_kg_m3)
        e_fine = abs(self.evolve(8, 0.06, 16).density_kg_m3 - reference.density_kg_m3)
        self.assertGreater(e_coarse, 1e-10)
        self.assertLess(e_fine, e_coarse / 8)

    def test_mass_in_a_material_interval_by_independent_quadrature(self):
        """Integrate rho(x,t) dx, rather than summing the code's J identity."""
        def total_mass(samples):
            initial_positions = [-12 + 24*i/(samples-1) for i in range(samples)]
            states = [self.evolve(x, 0.03, 200) for x in initial_positions]
            self.assertTrue(all(b.x_m > a.x_m for a,b in zip(states,states[1:])))
            return sum((a.density_kg_m3+b.density_kg_m3)*(b.x_m-a.x_m)/2
                       for a,b in zip(states,states[1:]))
        target = 1.225*24  # initial density times initial one-dimensional length
        err_coarse = abs(total_mass(121)-target)
        err_fine = abs(total_mass(241)-target)
        self.assertLess(err_fine/target, 5e-5)
        self.assertLess(err_fine, err_coarse/3)

    def test_bad_inputs(self):
        with self.assertRaises(ValueError):
            self.evolve(steps=0)
        with self.assertRaises(ValueError):
            self.evolve(steps=1.2)
        with self.assertRaises(ValueError):
            evolve_characteristic(0, 1, 10, -1, 5, 2)
        with self.assertRaises(ValueError):
            evolve_characteristic(math.inf, 1, 10, 1, 5, 2)


if __name__ == '__main__':
    unittest.main()
