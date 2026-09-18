import math
import unittest
from src.adm_acceleration_conservation import (
    momentum_time_derivative_acceleration,
    stress_divergence_acceleration,
    local_momentum_residual_acceleration,
)
from src.adm_momentum import gaussian_derivatives


class ADMAccelerationConservationTests(unittest.TestCase):
    def test_local_acceleration_order_conservation(self):
        a=0.07
        fyy,fzz,_,_=gaussian_derivatives(0.4,0.8,-0.3,1.2)
        self.assertAlmostEqual(local_momentum_residual_acceleration(a,fyy,fzz),0.0,places=15)

    def test_nonzero_terms_cancel_not_trivially_zero(self):
        a=0.11
        fyy,fzz,_,_=gaussian_derivatives(0.2,0.0,0.0,1.0)
        dtj=momentum_time_derivative_acceleration(a,fyy,fzz)
        divs=stress_divergence_acceleration(a,fyy,fzz)
        self.assertNotEqual(dtj,0.0)
        self.assertAlmostEqual(dtj,-divs,places=15)

    def test_acceleration_reversal_reverses_both_channels(self):
        fyy,fzz,_,_=gaussian_derivatives(0.7,0.3,0.2,0.9)
        for fn in (momentum_time_derivative_acceleration,stress_divergence_acceleration):
            self.assertAlmostEqual(fn(-0.2,fyy,fzz),-fn(0.2,fyy,fzz),places=15)

    def test_wrong_stress_sign_fails_conservation(self):
        a=0.09
        fyy,fzz,_,_=gaussian_derivatives(0.1,0.4,0.5,1.1)
        dtj=momentum_time_derivative_acceleration(a,fyy,fzz)
        wrong_div=-stress_divergence_acceleration(a,fyy,fzz)
        self.assertGreater(abs(dtj+wrong_div),1e-8)

    def test_length_scaling_inverse_cubed_with_acceleration_dimension(self):
        # If coordinates and sigma scale by L while geometric acceleration a scales as 1/L,
        # both conservation terms scale as L^-3.
        x,y,z,sigma,a=0.3,0.5,-0.2,1.0,0.08
        fyy,fzz,_,_=gaussian_derivatives(x,y,z,sigma)
        base=stress_divergence_acceleration(a,fyy,fzz)
        L=3.0
        gyy,gzz,_,_=gaussian_derivatives(L*x,L*y,L*z,L*sigma)
        scaled=stress_divergence_acceleration(a/L,gyy,gzz)
        self.assertAlmostEqual(scaled,base/L**3,places=15)


if __name__ == '__main__':
    unittest.main()
