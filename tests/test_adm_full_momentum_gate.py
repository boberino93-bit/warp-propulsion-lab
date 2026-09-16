import unittest
from src.adm_full_momentum_gate import translation_residual, gaussian_axis_derivatives
class ADMFullMomentumGateTests(unittest.TestCase):
 def test_translation_term_is_locally_nonzero(self):
  _,dx=gaussian_axis_derivatives(.7,2.); self.assertNotEqual(translation_residual(.2,dx,0),0)
 def test_speed_square_and_reversal(self):
  _,dx=gaussian_axis_derivatives(.7,2.); r=translation_residual(.2,dx,0); self.assertAlmostEqual(translation_residual(-.2,dx,0),r); self.assertAlmostEqual(translation_residual(.4,dx,0),4*r)
 def test_gaussian_parity_and_boundary_integral(self):
  s=1.3; v=.3; _,dp=gaussian_axis_derivatives(.8,s); _,dm=gaussian_axis_derivatives(-.8,s); self.assertAlmostEqual(translation_residual(v,dp,0),-translation_residual(v,dm,0)); L=8*s; n=20000; h=2*L/n; total=0.;
  for i in range(n):
   x=-L+(i+.5)*h; _,d=gaussian_axis_derivatives(x,s); total+=translation_residual(v,d,0)*h
  self.assertLess(abs(total),1e-12)
 def test_dimensional_length_scaling(self):
  _,d1=gaussian_axis_derivatives(.5,1.); _,d2=gaussian_axis_derivatives(1.,2.); self.assertAlmostEqual(d2,d1/8.)
