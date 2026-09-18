import math
import unittest
from src.adm_acceleration_stress import acceleration_trace_source, gaussian_integrated_acceleration_trace

class ADMAccelerationStressTests(unittest.TestCase):
    def test_formula_and_sign(self):
        self.assertAlmostEqual(acceleration_trace_source(2.0, 3.0), -6.0/(4*math.pi))
        self.assertAlmostEqual(acceleration_trace_source(-2.0, 3.0), 6.0/(4*math.pi))

    def test_linear_acceleration_scaling(self):
        x = acceleration_trace_source(0.3, -0.7)
        self.assertAlmostEqual(acceleration_trace_source(0.9, -0.7), 3*x)

    def test_gradient_parity(self):
        a=0.4
        self.assertAlmostEqual(acceleration_trace_source(a, 0.2), -acceleration_trace_source(a, -0.2))

    def test_local_nonzero_but_global_cancellation(self):
        self.assertNotEqual(acceleration_trace_source(0.5, 0.1), 0.0)
        self.assertAlmostEqual(gaussian_integrated_acceleration_trace(0.5, 1.0, 5.0, n=31), 0.0, places=12)

    def test_dimensions_scaling_length(self):
        # a and fx each scale as L^-1, so source scales as L^-2.
        base=acceleration_trace_source(0.4, 0.3)
        scaled=acceleration_trace_source(0.4/2, 0.3/2)
        self.assertAlmostEqual(scaled, base/4)

if __name__ == '__main__': unittest.main()
