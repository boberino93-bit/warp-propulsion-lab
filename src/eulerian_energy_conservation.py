"""Rigid-translation Eulerian energy balance for the standard Alcubierre metric.
Geometric units G=c=1, lapse alpha=1, flat spatial metric, beta^x=-v f.
"""
import math
PI = math.pi

def balance_from_derivatives(v, f, fy, fz, fxy, fxz):
    vals=(v,f,fy,fz,fxy,fxz)
    if not all(math.isfinite(q) for q in vals):
        raise ValueError("inputs must be finite")
    A=fy*fxy+fz*fxz
    return -v**3 * A * (f-1.0)/(16.0*PI)

def gaussian_balance(x,y,z,sigma,v):
    if not all(math.isfinite(q) for q in (x,y,z,sigma,v)) or sigma <= 0:
        raise ValueError("finite coordinates/v and positive finite sigma required")
    f=math.exp(-(x*x+y*y+z*z)/(sigma*sigma))
    A=-8.0*x*(y*y+z*z)*f*f/sigma**6
    return -v**3*A*(f-1.0)/(16.0*PI)

def gaussian_energy_density(x,y,z,sigma,v):
    if not all(math.isfinite(q) for q in (x,y,z,sigma,v)) or sigma <= 0:
        raise ValueError("finite coordinates/v and positive finite sigma required")
    f=math.exp(-(x*x+y*y+z*z)/(sigma*sigma))
    return -v*v*(y*y+z*z)*f*f/(8.0*PI*sigma**4)
