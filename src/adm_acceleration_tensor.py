"""Acceleration-only spatial stress required by the ADM K_ij evolution equation.

Geometric units G=c=1, alpha=1, flat gamma_ij, shift beta_x=-v(t) f.
Fixed-geometry source diagnostic, not a material model or propulsion device.
"""
import math
PI = math.pi

def acceleration_stress_tensor(a, fx, fy, fz):
    vals=(a,fx,fy,fz)
    if not all(math.isfinite(x) for x in vals): raise ValueError("inputs must be finite")
    q=a/(16.0*PI)
    return (0.0,-2.0*q*fx,-2.0*q*fx,q*fy,q*fz,0.0)

def acceleration_trace(a,fx): return -a*fx/(4.0*PI)

def acceleration_force_x(a,fyy,fzz):
    if not all(math.isfinite(x) for x in (a,fyy,fzz)): raise ValueError("inputs must be finite")
    return a*(fyy+fzz)/(16.0*PI)
