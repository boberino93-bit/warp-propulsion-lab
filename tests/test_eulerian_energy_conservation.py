import unittest
from src.eulerian_energy_conservation import gaussian_balance, gaussian_energy_density

class TestEulerianEnergyConservation(unittest.TestCase):
    def test_local_nonzero_and_front_back_odd(self):
        a=gaussian_balance(0.6,0.4,0.2,1.3,0.7)
        self.assertNotEqual(a,0.0)
        self.assertAlmostEqual(a,-gaussian_balance(-0.6,0.4,0.2,1.3,0.7),places=14)
    def test_velocity_reversal_cubic(self):
        a=gaussian_balance(.5,.3,.2,1.1,.4)
        self.assertAlmostEqual(gaussian_balance(.5,.3,.2,1.1,-.4),-a,places=14)
        self.assertAlmostEqual(gaussian_balance(.5,.3,.2,1.1,.8),8*a,places=14)
    def test_dimensional_scaling(self):
        lam=2.5
        a=gaussian_balance(.5,.3,.2,1.1,.6)
        b=gaussian_balance(lam*.5,lam*.3,lam*.2,lam*1.1,.6)
        self.assertAlmostEqual(b,a/lam**3,places=14)
    def test_global_parity_cancellation(self):
        sigma=1.0; v=.5; h=.2; total=0.0
        for i in range(-20,21):
          x=i*h
          for j in range(-12,13):
            y=j*h
            for k in range(-12,13):
              z=k*h
              total += gaussian_balance(x,y,z,sigma,v)*h**3
        self.assertLess(abs(total),1e-15)
    def test_energy_sign_and_stationary_limit(self):
        self.assertLess(gaussian_energy_density(.3,.4,.2,1.0,.7),0.0)
        self.assertEqual(gaussian_balance(.3,.4,.2,1.0,0.0),0.0)

if __name__=='__main__': unittest.main()
