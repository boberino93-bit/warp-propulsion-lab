"""Momentum-constraint source diagnostic for prescribed Alcubierre shift.

Convention: ds^2=-dt^2+(dx-v f dt)^2+dy^2+dz^2,
K_ij=(D_i beta_j+D_j beta_i)/2, beta_x=-v f, and
D_j(K^{ij}-gamma^{ij}K)=8*pi*S^i in G=c=1.
Changing the K_ij convention flips every S^i sign, not the conclusions.
"""
import math


def momentum_density(v_over_c, fyy, fzz, fxy, fxz):
    """Return (Sx,Sy,Sz) in geometric inverse-length-squared units."""
    for q in (v_over_c, fyy, fzz, fxy, fxz):
        if not math.isfinite(q):
            raise ValueError("finite inputs required")
    a = v_over_c/(16.0*math.pi)
    return (-a*(fyy+fzz), a*fxy, a*fxz)


def gaussian_derivatives(x, y, z, sigma):
    """Second derivatives needed above for f=exp(-r^2/(2 sigma^2))."""
    if not (math.isfinite(sigma) and sigma > 0):
        raise ValueError("sigma must be finite and positive")
    if not all(math.isfinite(q) for q in (x,y,z)):
        raise ValueError("finite coordinates required")
    s2=sigma*sigma
    f=math.exp(-(x*x+y*y+z*z)/(2*s2))
    fyy=((y*y)/(s2*s2)-1/s2)*f
    fzz=((z*z)/(s2*s2)-1/s2)*f
    fxy=(x*y/(s2*s2))*f
    fxz=(x*z/(s2*s2))*f
    return fyy,fzz,fxy,fxz
