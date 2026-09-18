"""Exact conservative x-momentum identity for a rigidly translating Alcubierre metric.
Geometric units G=c=1; repository shift convention beta^x=-v f.
"""
import math
PI=math.pi

def gaussian_axis_terms(x, sigma, v):
    """Return (covariant connection-source term, v0.3.7 naive residual) in T units."""
    if not all(math.isfinite(q) for q in (x,sigma,v)) or sigma <= 0:
        raise ValueError("finite x,v and positive finite sigma required")
    f=math.exp(-(x/sigma)**2)
    # Exact mixed-index conservative identity from G_{mu nu}/8pi:
    # d_mu T^mu_x = 1/2 T^{ab} d_x g_ab
    # RHS = v^2 f_x (f_yy+f_zz)/(16 pi).
    exact = v*v*x*f*f/(2.0*PI*sigma**4)
    # Previous deliberately truncated partial-ADM residual.
    naive = v*v*x*f/(2.0*PI*sigma**4)
    return exact, naive

def exact_source_from_derivatives(v, fx, fyy, fzz):
    if not all(math.isfinite(q) for q in (v,fx,fyy,fzz)):
        raise ValueError("inputs must be finite")
    return v*v*fx*(fyy+fzz)/(16.0*PI)
