import unittest
from src.accelerating_adm import instantaneous_momentum_density, gaussian_integrated_sx
class AcceleratingADMMomentumTests(unittest.TestCase):
    def test_acceleration_does_not_enter_momentum_constraint(self):
        args=(0.3,-0.12,0.04,0.03,-0.02); vals=[instantaneous_momentum_density(args[0],a,*args[1:]) for a in (-10.,0.,7.5)]; self.assertEqual(vals[0],vals[1]); self.assertEqual(vals[1],vals[2])
    def test_velocity_still_scales_linearly(self):
        d=(0.2,-0.1,0.07,-0.03); a=instantaneous_momentum_density(.2,5.,*d); b=instantaneous_momentum_density(.4,5.,*d)
        for x,y in zip(a,b): self.assertAlmostEqual(y,2*x)
    def test_local_source_can_be_nonzero_during_acceleration(self):
        self.assertTrue(all(x!=0 for x in instantaneous_momentum_density(.4,3.,-1.,-2.,.5,-.25)))
    def test_integrated_sx_remains_boundary_cancellation(self):
        small=abs(gaussian_integrated_sx(.4,3.,1.,2.,25)); large=abs(gaussian_integrated_sx(.4,3.,1.,5.,31)); self.assertLess(large,small); self.assertLess(large,2e-5)
if __name__=='__main__': unittest.main()
