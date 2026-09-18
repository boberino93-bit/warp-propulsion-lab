import math
import unittest
from src.adm_momentum import momentum_density, gaussian_derivatives

class ADMMomentumTests(unittest.TestCase):
    def test_axis_gaussian_sign_and_formula(self):
        v,s=0.2,3.0
        d=gaussian_derivatives(0,0,0,s)
        sx,sy,sz=momentum_density(v,*d)
        self.assertAlmostEqual(sx, v/(8*math.pi*s*s))
        self.assertAlmostEqual(sy,0.0); self.assertAlmostEqual(sz,0.0)

    def test_linear_speed_scaling(self):
        d=gaussian_derivatives(1,.7,-.2,2.0)
        a=momentum_density(.1,*d); b=momentum_density(.3,*d)
        for aa,bb in zip(a,b): self.assertAlmostEqual(bb,3*aa)

    def test_parity_cancels_transverse_components(self):
        v=.4; x,y,z,s=1.1,.8,.5,2.3
        p=momentum_density(v,*gaussian_derivatives(x,y,z,s))
        py=momentum_density(v,*gaussian_derivatives(x,-y,z,s))
        pz=momentum_density(v,*gaussian_derivatives(x,y,-z,s))
        self.assertAlmostEqual(p[1],-py[1]); self.assertAlmostEqual(p[2],-pz[2])

    def test_volume_integral_tends_to_zero(self):
        # Midpoint Riemann integral. Local Sx is nonzero, but localized smooth f
        # makes integral transverse Laplacians a boundary term -> zero at infinity.
        v,s=.25,1.0
        def integrate(L,n):
            h=2*L/n; total=0.0
            for i in range(n):
                x=-L+(i+.5)*h
                for j in range(n):
                    y=-L+(j+.5)*h
                    for k in range(n):
                        z=-L+(k+.5)*h
                        total += momentum_density(v,*gaussian_derivatives(x,y,z,s))[0]
            return total*h**3
        small=abs(integrate(2.5,20)); large=abs(integrate(5.0,40))
        self.assertLess(large, small/100)
        self.assertLess(large, 1e-5)

if __name__=='__main__': unittest.main()
