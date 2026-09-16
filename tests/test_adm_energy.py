import math
import unittest
from src.adm_energy import eulerian_energy_from_gradients, radial_energy


class ADMSourceEnergyTests(unittest.TestCase):
    def test_hamiltonian_from_extrinsic_curvature(self):
        # beta_x=-v*f; Kxx=-v*fx, Kxy=-v*fy/2, Kxz=-v*fz/2.
        # gamma_ij=delta_ij, 3R=0, K^2-KijKij=-v^2*(fy^2+fz^2)/2.
        for v, fx, fy, fz in ((.3, .7, .2, -.4), (1.5, -.2, .5, .8), (0, 3, 2, 1)):
            kxx, kxy, kxz = -v*fx, -v*fy/2, -v*fz/2
            k2 = kxx*kxx
            kij2 = kxx*kxx + 2*kxy*kxy + 2*kxz*kxz
            self.assertAlmostEqual((k2-kij2)/(16*math.pi),
                                   eulerian_energy_from_gradients(v, fx, fy, fz))

    def test_sign_and_longitudinal_gradient_cancellation(self):
        self.assertEqual(eulerian_energy_from_gradients(.8, 999, 0, 0), 0)
        self.assertLess(eulerian_energy_from_gradients(.8, 0, 1, 0), 0)

    def test_radial_angular_dependence_and_velocity_square(self):
        a = radial_energy(.2, 0, 3, 4, -.5)
        b = radial_energy(.4, 0, 3, 4, -.5)
        self.assertAlmostEqual(b, 4*a)
        self.assertAlmostEqual(radial_energy(.2, 5, 0, 0, -.5), 0)
        self.assertEqual(radial_energy(.2, 0, 0, 0, 0), 0)

    def test_bad_origin_and_nonfinite(self):
        with self.assertRaises(ValueError): radial_energy(.2, 0, 0, 0, 1)
        with self.assertRaises(ValueError): eulerian_energy_from_gradients(float('nan'), 0, 0, 0)
