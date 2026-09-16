import math,unittest
from src.adm_momentum import momentum_density,gaussian_derivatives
class ADMMomentumTests(unittest.TestCase):
 def test_axis_gaussian_sign_and_formula(self):
  v,s=.2,3.; sx,sy,sz=momentum_density(v,*gaussian_derivatives(0,0,0,s)); self.assertAlmostEqual(sx,v/(8*math.pi*s*s)); self.assertAlmostEqual(sy,0); self.assertAlmostEqual(sz,0)
 def test_linear_speed_scaling(self):
  d=gaussian_derivatives(1,.7,-.2,2.); a=momentum_density(.1,*d); b=momentum_density(.3,*d)
  for x,y in zip(a,b): self.assertAlmostEqual(y,3*x)
 def test_parity_cancels_transverse_components(self):
  v=.4; x,y,z,s=1.1,.8,.5,2.3; p=momentum_density(v,*gaussian_derivatives(x,y,z,s)); py=momentum_density(v,*gaussian_derivatives(x,-y,z,s)); pz=momentum_density(v,*gaussian_derivatives(x,y,-z,s)); self.assertAlmostEqual(p[1],-py[1]); self.assertAlmostEqual(p[2],-pz[2])
 def test_volume_integral_tends_to_zero(self):
  v,s=.25,1.
  def integ(L,n):
   h=2*L/n; total=0
   for i in range(n):
    for j in range(n):
     for k in range(n):
      x=-L+(i+.5)*h; y=-L+(j+.5)*h; z=-L+(k+.5)*h; total+=momentum_density(v,*gaussian_derivatives(x,y,z,s))[0]
   return total*h**3
  small=abs(integ(2.5,20)); large=abs(integ(5.,40)); self.assertLess(large,small/100); self.assertLess(large,1e-5)
if __name__=='__main__': unittest.main()
