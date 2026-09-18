import math, unittest
from src.covariant_x_momentum import gaussian_axis_terms, exact_source_from_derivatives

class CovariantXMomentumChecks(unittest.TestCase):
    def test_center_zero_by_parity(self):
        exact, naive=gaussian_axis_terms(0.0,1.3,0.4)
        self.assertEqual(exact,0.0); self.assertEqual(naive,0.0)
    def test_exact_not_naive_away_from_center(self):
        x,s,v=0.7,1.2,0.5
        exact,naive=gaussian_axis_terms(x,s,v)
        f=math.exp(-(x/s)**2)
        self.assertAlmostEqual(exact/naive,f,12)
        self.assertNotAlmostEqual(exact,naive,12)
    def test_velocity_reversal_even(self):
        self.assertAlmostEqual(gaussian_axis_terms(.5,1.0,.3)[0],gaussian_axis_terms(.5,1.0,-.3)[0],14)
    def test_odd_global_cancellation(self):
        # symmetric trapezoid sum of exact source along axis must cancel
        vals=[]
        for k in range(-400,401):
            x=k*0.02
            vals.append(gaussian_axis_terms(x,1.0,.6)[0])
        self.assertLess(abs(sum(vals)*0.02),1e-12)
    def test_derivative_formula_matches_gaussian(self):
        x,s,v=.4,1.1,.7; f=math.exp(-(x/s)**2)
        fx=-2*x*f/s**2; fyy=fzz=-2*f/s**2
        exact,_=gaussian_axis_terms(x,s,v)
        self.assertAlmostEqual(exact_source_from_derivatives(v,fx,fyy,fzz),exact,14)
