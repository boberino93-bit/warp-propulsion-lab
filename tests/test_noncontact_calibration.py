import math
import unittest

from src.noncontact_calibration import (
    magnetic_force, magnetic_force_uncertainty,
    cross_calibration_z, cross_calibration_gate,
)


class NonContactCalibrationTests(unittest.TestCase):
    def test_linear_force_and_reversal(self):
        self.assertAlmostEqual(magnetic_force(0.1, 0.01), 1e-3)
        self.assertAlmostEqual(magnetic_force(-0.1, 0.01), -1e-3)

    def test_target_range_example(self):
        k = 0.01
        self.assertAlmostEqual(magnetic_force(0.01, k), 1e-4)
        self.assertAlmostEqual(magnetic_force(0.1, k), 1e-3)

    def test_uncertainty(self):
        s = magnetic_force_uncertainty(0.1, 1e-5, 0.01, 1e-5)
        expected = math.sqrt((0.01e-5)**2 + (0.1e-5)**2)
        self.assertAlmostEqual(s, expected)

    def test_exact_cross_calibration(self):
        self.assertEqual(cross_calibration_z(1e-3, 1e-6, 1e-3, 1e-7), 0.0)
        self.assertTrue(cross_calibration_gate(1e-3, 1e-6, 1e-3, 1e-7))

    def test_wrong_sign_rejected(self):
        self.assertFalse(cross_calibration_gate(-1e-3, 1e-6, 1e-3, 1e-7))

    def test_large_bias_rejected(self):
        self.assertFalse(cross_calibration_gate(1.06e-3, 1e-3, 1e-3, 1e-3))

    def test_statistically_inconsistent_rejected(self):
        self.assertFalse(cross_calibration_gate(1.02e-3, 1e-6, 1e-6, 1e-7))

    def test_repeatability_enters_combined_uncertainty(self):
        z0 = abs(cross_calibration_z(1.001e-3, 1e-7, 1e-3, 1e-7, 0.0))
        z1 = abs(cross_calibration_z(1.001e-3, 1e-7, 1e-3, 1e-7, 1e-6))
        self.assertLess(z1, z0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            magnetic_force(1.0, 0.0)
        with self.assertRaises(ValueError):
            magnetic_force_uncertainty(1.0, -1.0, 1.0, 0.0)
        with self.assertRaises(ValueError):
            cross_calibration_gate(1.0, 0.1, 0.0, 0.1)


if __name__ == "__main__":
    unittest.main()
