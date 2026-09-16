"""1D stationary Eulerian dust in a *prescribed* warp-like shift.

NOT a self-consistent GR fluid or a functioning propulsion model.
"""
from __future__ import annotations
import math


def top_hat_shape(xi_m: float, half_width_m: float, wall_m: float) -> float:
    """0 <= f < 1 for finite R,w; smooth near-top-hat profile."""
    if half_width_m <= 0 or wall_m <= 0:
        raise ValueError("half width and wall thickness must be positive")
    return 0.5 * (math.tanh((xi_m + half_width_m) / wall_m)
                  - math.tanh((xi_m - half_width_m) / wall_m))


def stationary_dust_density(upstream_density_kg_m3: float, f: float) -> float:
    """rho=rho0/(1-f); ONLY for the steady Eulerian dust assumptions."""
    if upstream_density_kg_m3 <= 0:
        raise ValueError("positive upstream density required")
    if not 0 <= f < 1:
        raise ValueError("steady finite-density solution requires 0 <= f < 1")
    return upstream_density_kg_m3 / (1.0 - f)


def relative_mass_flux(density_kg_m3: float, f: float,
                       bubble_velocity_m_s: float) -> float:
    """rho*(v_s*f - v_s); signed steady comoving flux [kg/(m^2 s)]."""
    return density_kg_m3 * bubble_velocity_m_s * (f - 1.0)
