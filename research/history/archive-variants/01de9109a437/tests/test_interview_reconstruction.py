"""Conditional interview arithmetic. No sensor data or propulsion inference."""
import math
import unittest

def triangular_motion(distance, duration):
    """Rest-to-rest symmetric constant acceleration then braking, SI units."""
    if not math.isfinite(distance) or distance <= 0:
        raise ValueError("distance must be finite and positive")
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("duration must be finite and positive")
    return 4 * distance / duration**2, 2 * distance / duration

class ReconstructionChecks(unittest.TestCase):
    def test_independent_piecewise_integration(self):
        distance, duration = 2500, 25
        acceleration, peak = triangular_motion(distance, duration)
        n = 10000
        dt = duration / n
        area = sum(acceleration * min((i + .5)*dt, duration-(i+.5)*dt)*dt
                   for i in range(n))
        self.assertAlmostEqual(area, distance, places=6)
        self.assertAlmostEqual(peak, 200)

    def test_same_distance_different_peaks(self):
        for tau in (25, 10, 2 * 2500 / (3000 * .44704)):
            acceleration, peak = triangular_motion(2500, tau)
            self.assertLessEqual(tau, 25)
            self.assertAlmostEqual(.5 * peak * tau, 2500)
        self.assertAlmostEqual(2 * 2500 / (3000 * .44704), 3.728227, places=5)

    def test_time_sensitivity(self):
        a, _ = triangular_motion(8534.4, .78)
        a2, _ = triangular_motion(8534.4, 1.56)
        self.assertAlmostEqual(a / a2, 4)

    def test_invalid_inputs(self):
        for d, t in ((0, 1), (1, 0), (-1, 1), (1, float("nan"))):
            with self.assertRaises(ValueError):
                triangular_motion(d, t)
