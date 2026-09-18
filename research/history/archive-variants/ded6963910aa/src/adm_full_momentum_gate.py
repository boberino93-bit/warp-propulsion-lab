"""Gate for the omitted translating-shape term in Alcubierre x-momentum balance.

Geometric units G=c=1. For j_x=-v (f_yy+f_zz)/(16*pi) and a rigid profile
f(x-x_s(t),y,z), the fixed-coordinate time derivative contains both acceleration
and translation. The acceleration piece is cancelled by the previously derived
acceleration stress divergence. What remains in the *naive Cartesian partial*
balance is v^2 d_x(f_yy+f_zz)/(16*pi). A nonzero value is evidence that
partial_t j_x + partial_j S_xj=0 is not the complete ADM/covariant conservation
law; shift/advection/connection terms must be retained. It is not thrust.
"""
import math
PI=math.pi

def translation_residual(v, fxyy, fxzz):
    vals=(v,fxyy,fxzz)
    if not all(math.isfinite(q) for q in vals):
        raise ValueError("inputs must be finite")
    return v*v*(fxyy+fxzz)/(16.0*PI)

def gaussian_axis_derivatives(x, sigma):
    """Return (f_yy+f_zz, d_x(f_yy+f_zz)) at y=z=0 for exp(-r^2/sigma^2)."""
    if not math.isfinite(x) or not math.isfinite(sigma) or sigma <= 0:
        raise ValueError("finite x and positive finite sigma required")
    f=math.exp(-(x/sigma)**2)
    lap_perp=-4.0*f/(sigma*sigma)
    dx_lap_perp=8.0*x*f/(sigma**4)
    return lap_perp, dx_lap_perp
