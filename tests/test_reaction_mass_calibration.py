import unittest
from src.reaction_mass_calibration import *

class ReactionMassCalibrationTests(unittest.TestCase):
    def test_reference_mass_flow_and_uncertainty(self):
        mdot = mass_flow(0.0006, 60.0)
        self.assertAlmostEqual(mdot, 1e-5)
        s = mass_flow_uncertainty(0.0006, 60.0, 1e-6, 0.01)
        self.assertAlmostEqual(s/mdot, ((2*(1e-6/0.0006)**2)+(0.01/60)**2)**0.5)

    def test_inferred_velocity_and_uncertainty(self):
        ve = inferred_exhaust_velocity(1e-3, 1e-5)
        self.assertAlmostEqual(ve, 100.0)
        s = inferred_velocity_uncertainty(1e-3, 1e-5, 1e-5, 2e-7)
        self.assertAlmostEqual(s/ve, (0.01**2 + 0.02**2)**0.5)

    def test_exact_closure(self):
        self.assertAlmostEqual(closure_z(1e-3, 1e-5, 1e-5, 2e-7, 100, 1), 0.0)
        self.assertTrue(calibration_passes(1e-3, 1e-5, 1e-5, 2e-7, 100, 1))

    def test_bias_gate_rejects_large_offset_even_if_uncertainty_large(self):
        self.assertFalse(calibration_passes(1.08e-3, 1e-3, 1e-5, 2e-7, 100, 1))

    def test_z_gate_rejects_precise_small_offset(self):
        self.assertFalse(calibration_passes(1.02e-3, 1e-6, 1e-5, 1e-9, 100, 0.01))

    def test_invalid(self):
        with self.assertRaises(ValueError): mass_flow(0, 1)
        with self.assertRaises(ValueError): inferred_exhaust_velocity(1, 0)
        with self.assertRaises(ValueError): calibration_passes(1,0.1,1,0.1,1,0.1,max_abs_z=0)

if __name__ == '__main__': unittest.main()
