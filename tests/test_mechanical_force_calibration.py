import unittest

from src.mechanical_force_calibration import (
    deadweight_force, deadweight_force_uncertainty, required_mass_for_force,
    recovery_z, bidirectional_gate,
)


class MechanicalForceCalibrationTests(unittest.TestCase):
    def test_target_mass_range(self):
        m01 = required_mass_for_force(1e-4, 9.80665, 1.2, 8000.0)
        m10 = required_mass_for_force(1e-3, 9.80665, 1.2, 8000.0)
        self.assertAlmostEqual(m01 * 1e6, 10.1987, places=3)
        self.assertAlmostEqual(m10 * 1e6, 101.987, places=2)

    def test_buoyancy_reduces_force(self):
        vacuum = deadweight_force(1e-4, 9.80665)
        air = deadweight_force(1e-4, 9.80665, 1.2, 8000.0)
        self.assertLess(air, vacuum)
        self.assertAlmostEqual((vacuum-air)/vacuum, 1.2/8000.0, places=12)

    def test_sign_reversal(self):
        plus = deadweight_force(5e-5, 9.80665, sign=1)
        minus = deadweight_force(5e-5, 9.80665, sign=-1)
        self.assertEqual(plus, -minus)

    def test_uncertainty_positive_and_small_for_example(self):
        f = deadweight_force(1.01987e-4, 9.80665, 1.2, 8000.0)
        s = deadweight_force_uncertainty(1.01987e-4, 1e-8, 9.80665, 1e-5,
                                         1.2, 0.02, 8000.0, 100.0)
        self.assertGreater(s, 0)
        self.assertLess(s/f, 2e-4)

    def test_exact_recovery(self):
        self.assertEqual(recovery_z(1e-3, 1e-5, 1e-3, 1e-7), 0.0)
        self.assertTrue(bidirectional_gate(1e-3, -1e-3, 1e-5, 1e-3, 1e-7))

    def test_wrong_sign_or_bias_fails(self):
        self.assertFalse(bidirectional_gate(1e-3, 1e-3, 1e-5, 1e-3, 1e-7))
        self.assertFalse(bidirectional_gate(1.06e-3, -1.0e-3, 1e-3, 1e-3, 1e-7))

    def test_transfer_uncertainty_is_explicit(self):
        z_no_transfer = abs(recovery_z(1.03e-3, 1e-6, 1e-3, 1e-7, 0.0))
        z_with_transfer = abs(recovery_z(1.03e-3, 1e-6, 1e-3, 1e-7, 2e-5))
        self.assertGreater(z_no_transfer, z_with_transfer)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            required_mass_for_force(-1, 9.8)
        with self.assertRaises(ValueError):
            deadweight_force(1e-4, 9.8, sign=0)


if __name__ == "__main__":
    unittest.main()
