import unittest
from src.accelerating_adm import instantaneous_momentum_density, gaussian_integrated_sx

class AcceleratingADMMomentumTests(unittest.TestCase):
    def test_acceleration_does_not_enter_momentum_constraint(self):
        args=(0.3, -0.12, 0.04, 0.03, -0.02)
        vals=[instantaneous_momentum_density(args[0],a,*args[1:]) for a in (-10.0,0.0,7.5)]
        self.assertEqual(vals[0],vals[1]); self.assertEqual(vals[1],vals[2])

    def test_velocity_still_scales_linearly(self):
        d=(0.2,-0.1,0.07,-0.03)
        a=instantaneous_momentum_density(0.2,5.0,*d)
        b=instantaneous_momentum_density(0.4,5.0,*d)
        for x,y in zip(a,b): self.assertAlmostEqual(y,2*x)

    def test_local_source_can_be_nonzero_during_acceleration(self):
        sx,sy,sz=instantaneous_momentum_density(0.4,3.0,-1.0,-2.0,0.5,-0.25)
        self.assertNotEqual(sx,0.0); self.assertNotEqual(sy,0.0); self.assertNotEqual(sz,0.0)

    def test_integrated_sx_remains_boundary_cancellation(self):
        # Increasing domain should drive localized Gaussian volume integral toward zero.
        small=abs(gaussian_integrated_sx(0.4,3.0,1.0,2.0,25))
        large=abs(gaussian_integrated_sx(0.4,3.0,1.0,5.0,31))
        self.assertLess(large, small)
        self.assertLess(large, 2e-5)

if __name__=='__main__': unittest.main()
