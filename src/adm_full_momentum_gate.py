"""Gate for omitted translating-shape term in Alcubierre x-momentum balance.
Geometric units G=c=1. A nonzero naive residual diagnoses omitted ADM/covariant terms; it is not thrust.
"""
import math
PI=math.pi

def translation_residual(v, fxyy, fxzz):
    vals=(v,fxyy,fxzz)
    if not all(math.isfinite(q) for q in vals): raise ValueError("inputs must be finite")
    return v*v*(fxyy+fxzz)/(16.0*PI)

def gaussian_axis_derivatives(x, sigma):
    if not math.isfinite(x) or not math.isfinite(sigma) or sigma <= 0: raise ValueError("finite x and positive finite sigma required")
    f=math.exp(-(x/sigma)**2)
    return -4.0*f/(sigma*sigma), 8.0*x*f/(sigma**4)
