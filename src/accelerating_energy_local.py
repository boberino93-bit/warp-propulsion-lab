"""Acceleration-linear Eulerian energy closure for the prescribed Alcubierre metric.
Geometric units G=c=1. This is source bookkeeping, not an actuator or engine model.
"""
import math

def energy_time_accel(v, a, fy, fz):
    return -v*a*(fy*fy + fz*fz)/(16.0*math.pi)

def kij_sij_accel(v, a, fy, fz):
    return -v*a*(fy*fy + fz*fz)/(16.0*math.pi)

def local_accel_residual(v, a, fy, fz):
    return energy_time_accel(v,a,fy,fz) - kij_sij_accel(v,a,fy,fz)

def gaussian_integrated_accel_term(v, a, sigma):
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    return -v*a*math.sqrt(math.pi)*sigma/(16.0*math.sqrt(2.0))
