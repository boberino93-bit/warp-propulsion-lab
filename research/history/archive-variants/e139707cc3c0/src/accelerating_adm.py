"""Instantaneous ADM momentum diagnostic for an accelerating Alcubierre shift.

For beta_x=-v(t) f(x-x_s(t),y,z), alpha=1 and flat gamma_ij, the
momentum constraint depends on spatial derivatives of beta on each slice.
It therefore contains v(t), but no explicit acceleration a=dv/dt.
This does NOT close the spacetime stress/energy conservation budget;
acceleration can enter evolution equations/spatial stresses.
"""
import math
from src.adm_momentum import momentum_density


def instantaneous_momentum_density(v_over_c, acceleration_geom, fyy, fzz, fxy, fxz):
    """Return ADM momentum density and explicitly audit acceleration independence.

    acceleration_geom is accepted as a finite geometric-unit acceleration solely
    so tests can falsify any accidental acceleration dependence in this constraint.
    """
    if not math.isfinite(acceleration_geom):
        raise ValueError("finite acceleration required")
    return momentum_density(v_over_c, fyy, fzz, fxy, fxz)


def gaussian_integrated_sx(v_over_c, acceleration_geom, sigma, half_width, n=41):
    """Midpoint numerical integral of Sx for a localized Gaussian profile."""
    if not (sigma > 0 and half_width > 0 and n >= 3):
        raise ValueError("positive sigma/half_width and n>=3 required")
    h=2.0*half_width/n
    total=0.0
    invs2=1.0/(sigma*sigma)
    for i in range(n):
        x=-half_width+(i+0.5)*h
        for j in range(n):
            y=-half_width+(j+0.5)*h
            for k in range(n):
                z=-half_width+(k+0.5)*h
                r2=x*x+y*y+z*z
                f=math.exp(-0.5*r2*invs2)
                fyy=(y*y*invs2*invs2-invs2)*f
                fzz=(z*z*invs2*invs2-invs2)*f
                sx,_,_=instantaneous_momentum_density(v_over_c, acceleration_geom,fyy,fzz,0.0,0.0)
                total += sx
    return total*h**3
