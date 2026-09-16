"""Eulerian source-energy budget for a Gaussian Alcubierre profile.
Geometric units G=c=1. Profile f=exp(-r^2/sigma^2).
"""
import math
PI=math.pi

def local_energy_density(x,y,z,sigma,v):
    if not all(math.isfinite(q) for q in (x,y,z,sigma,v)) or sigma <= 0:
        raise ValueError("finite coordinates/v and positive finite sigma required")
    r2=x*x+y*y+z*z
    f=math.exp(-r2/(sigma*sigma))
    fy=-2.0*y*f/(sigma*sigma)
    fz=-2.0*z*f/(sigma*sigma)
    return -(v*v)*(fy*fy+fz*fz)/(32.0*PI)

def integrated_gaussian_energy(sigma,v):
    """Integral of Eulerian E over R^3 for f=exp(-r^2/sigma^2)."""
    if not all(math.isfinite(q) for q in (sigma,v)) or sigma <= 0:
        raise ValueError("finite v and positive finite sigma required")
    return -(v*v)*math.sqrt(PI)*sigma/(32.0*math.sqrt(2.0))
