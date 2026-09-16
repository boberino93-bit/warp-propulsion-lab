import unittest

from src.reaction_mass_baseline import (
    thrust,
    jet_power,
    propellant_rate_g_min,
    photon_power_equivalent,
)


class ReactionMassBaselineTests(unittest.TestCase):
    def test_reference_case(self):
        self.assertAlmostEqual(thrust(1e-5, 100), 1e-3)
        self.assertAlmostEqual(jet_power(1e-5, 100), 0.05)
        self.assertAlmostEqual(propellant_rate_g_min(1e-5), 0.6)

    def test_momentum_scaling(self):
        self.assertAlmostEqual(thrust(2e-5, 100), 2e-3)
        self.assertAlmostEqual(thrust(1e-5, 200), 2e-3)

    def test_power_scaling(self):
        self.assertAlmostEqual(jet_power(1e-5, 200), 0.2)

    def test_photon_comparison(self):
        self.assertAlmostEqual(photon_power_equivalent(1e-3), 299792.458)
        self.assertAlmostEqual(photon_power_equivalent(1e-3, True), 149896.229)

    def test_reject_negative(self):
        with self.assertRaises(ValueError):
            thrust(-1, 1)


if __name__ == "__main__":
    unittest.main()
