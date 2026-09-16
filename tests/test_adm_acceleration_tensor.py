import math
import unittest
from src.adm_acceleration_tensor import acceleration_stress_tensor, acceleration_trace, acceleration_force_x

class ADMAccelerationTensorTests(unittest.TestCase):
    def test_tensor_and_trace_reproduce_prior_trace_gate(self):
        a,fx,fy,fz=.7,-.12,.05,-.03
        sxx,syy,szz,sxy,sxz,syz=acceleration_stress_tensor(a,fx,fy,fz)
        self.assertEqual(sxx,0.0)
        self.assertAlmostEqual(sxx+syy+szz,acceleration_trace(a,fx),places=14)
        self.assertAlmostEqual(sxy,a*fy/(16*math.pi),places=14)
        self.assertAlmostEqual(sxz,a*fz/(16*math.pi),places=14)
        self.assertEqual(syz,0.0)
    def test_longitudinal_acceleration_stress_cancels_exactly(self):
        for fx in (-2.,-.1,0.,.4,3.): self.assertEqual(acceleration_stress_tensor(1.3,fx,.2,-.4)[0],0.0)
    def test_linear_acceleration_scaling_and_reversal(self):
        args=(.11,-.07,.03); p=acceleration_stress_tensor(2.,*args); m=acceleration_stress_tensor(-2.,*args)
        self.assertTrue(all(abs(x+y)<1e-15 for x,y in zip(p,m)))
    def test_integrated_x_force_is_boundary_cancellation(self):
        h=.03; L=6.; a=.8; n=int(2*L/h)+1; total=0.
        for iy in range(n):
            y=-L+iy*h; wy=.5 if iy in (0,n-1) else 1.
            for iz in range(n):
                z=-L+iz*h; wz=.5 if iz in (0,n-1) else 1.; f=math.exp(-(y*y+z*z))
                total += wy*wz*acceleration_force_x(a,(4*y*y-2)*f,(4*z*z-2)*f)
        self.assertLess(abs(total*h*h),2e-12)
    def test_nonlocalized_boundary_can_carry_force(self):
        self.assertGreater(acceleration_force_x(1.,2.,0.),0.)

if __name__=='__main__': unittest.main()
