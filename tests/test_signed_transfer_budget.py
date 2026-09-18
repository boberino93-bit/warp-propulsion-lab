import math
import unittest
from simulations.signed_transfer_budget import FROZEN_U95_CEILING_MN, combined_u95_mn, passes_frozen_ceiling

class SignedTransferBudgetTests(unittest.TestCase):
    def setUp(self):
        self.allocation = {
            "reference": 0.000101166,
            "alignment": 0.0001,
            "reversal_repeatability": 0.0009,
            "zero_return": 0.0009,
            "hysteresis": 0.0009,
            "architecture_specific_transfer": 0.0018,
        }

    def test_frozen_allocation_arithmetic(self):
        self.assertAlmostEqual(combined_u95_mn(self.allocation), 0.004770842508218439)
        self.assertTrue(passes_frozen_ceiling(self.allocation))

    def test_ceiling_is_inclusive(self):
        self.assertTrue(passes_frozen_ceiling({"single": FROZEN_U95_CEILING_MN / 2}))

    def test_rss_not_linear_sum(self):
        expected = 2 * math.sqrt(0.001**2 + 0.002**2)
        self.assertAlmostEqual(combined_u95_mn({"first": 0.001, "second": 0.002}), expected)

    def test_invalid_inputs_are_rejected(self):
        for components in ({}, {"x": -1.0}, {"x": math.inf}, {"": 0.1}):
            with self.assertRaises(ValueError):
                combined_u95_mn(components)

if __name__ == "__main__":
    unittest.main()
