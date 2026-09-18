import math
import unittest
from src.adm_acceleration_tensor import (
    acceleration_stress_tensor, acceleration_trace, acceleration_force_x,
)

class ADMAccelerationTensorTests(unittest.TestCase):
    def test_tensor_and_trace_reproduce_prior_trace_gate(self):
        a, fx, fy, fz = 0.7, -0.12, 0.05, -0.03
        sxx, syy, szz, sxy, sxz, syz = acceleration_stress_tensor(a,fx,fy,fz)
        self.assertEqual(sxx, 0.0)
        self.assertAlmostEqual(sxx+syy+szz, acceleration_trace(a,fx), places=14)
        self.assertAlmostEqual(sxy, a*fy/(16*math.pi), places=14)
        self.assertAlmostEqual(sxz, a*fz/(16*math.pi), places=14)
        self.assertEqual(syz, 0.0)

    def test_longitudinal_acceleration_stress_cancels_exactly(self):
        for fx in (-2.0, -0.1, 0.0, 0.4, 3.0):
            self.assertEqual(acceleration_stress_tensor(1.3,fx,.2,-.4)[0], 0.0)

    def test_linear_acceleration_scaling_and_reversal(self):
        args=(0.11,-0.07,0.03)
        p=acceleration_stress_tensor(2.0,*args)
        m=acceleration_stress_tensor(-2.0,*args)
        self.assertTrue(all(abs(x+y)<1e-15 for x,y in zip(p,m)))

    def test_integrated_x_force_is_boundary_cancellation(self):
        # f=exp(-(x^2+y^2+z^2)); at x=z=0, integrate force_x over y.
        # f_yy=(4y^2-2)e^-y^2 and f_zz=-2e^-y^2; integral is -2 sqrt(pi).
        # This 1D slice is NOT zero because z boundary is not integrated.
        # Integrate full y,z plane analytically/numerically: each second derivative integrates zero.
        h=0.03; L=6.0; a=.8
        n=int(2*L/h)+1
        total=0.0
        for iy in range(n):
            y=-L+iy*h
            wy=0.5 if iy in (0,n-1) else 1.0
            for iz in range(n):
                z=-L+iz*h
                wz=0.5 if iz in (0,n-1) else 1.0
                f=math.exp(-(y*y+z*z))
                fyy=(4*y*y-2)*f
                fzz=(4*z*z-2)*f
                total += wy*wz*acceleration_force_x(a,fyy,fzz)
        total *= h*h
        self.assertLess(abs(total), 2e-12)

    def test_nonlocalized_boundary_can_carry_force(self):
        # f=y^2 gives f_yy=2: without localization, force density need not cancel.
        self.assertGreater(acceleration_force_x(1.0,2.0,0.0),0.0)

if __name__ == '__main__': unittest.main()
