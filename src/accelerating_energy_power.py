"""Integrated acceleration power for the repository's one-scale Gaussian Alcubierre source.
Geometric units G=c=1. This is a prescribed-metric source requirement, not a propulsion model.
"""
import math


def gaussian_total_energy(v: float, sigma: float) -> float:
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    return -(v*v)*math.sqrt(math.pi)*sigma/(32.0*math.sqrt(2.0))


def gaussian_acceleration_power(v: float, a: float, sigma: float) -> float:
    """dE_total/dt for fixed sigma and instantaneous dv/dt=a."""
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    return -v*a*math.sqrt(math.pi)*sigma/(16.0*math.sqrt(2.0))
