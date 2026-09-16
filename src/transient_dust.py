"""Finite-time 1-D prescribed-shift dust characteristics.

This is a kinematic continuity-equation model, not a solution of the
Einstein equations, a fluid shock solver, or a propulsion mechanism.
All inputs and times use SI units; v may be positive, negative, or zero.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

from src.medium import top_hat_shape


@dataclass(frozen=True)
class CharacteristicState:
    xi_m: float
    x_m: float
    density_kg_m3: float
    jacobian: float
    f: float


def shape_gradient_per_m(xi_m: float, half_width_m: float, wall_m: float) -> float:
    """Analytic derivative df/dxi of the tanh profile, in inverse metres."""
    if half_width_m <= 0 or wall_m <= 0:
        raise ValueError("half width and wall thickness must be positive")
    left = math.tanh((xi_m + half_width_m) / wall_m)
    right = math.tanh((xi_m - half_width_m) / wall_m)
    return 0.5 * ((1.0 - left * left) - (1.0 - right * right)) / wall_m


def evolve_characteristic(
    xi_initial_m: float,
    elapsed_s: float,
    bubble_velocity_m_s: float,
    upstream_density_kg_m3: float,
    half_width_m: float,
    wall_m: float,
    steps: int = 400,
) -> CharacteristicState:
    """Advect an initial Eulerian dust parcel from initial laboratory time t=0.

    Integrates dxi/dt = v_s (f(xi)-1) and d(log J)/dt = v_s f'(xi)
    with classical fourth-order Runge--Kutta; J = dxi(t)/dxi(0).
    Return rho(t)=rho_initial/J for a uniform initial Eulerian density.
    For nonuniform initial density, replace rho_initial by rho_initial(xi0).
    """
    vals = (xi_initial_m, elapsed_s, bubble_velocity_m_s,
            upstream_density_kg_m3, half_width_m, wall_m)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("inputs must be finite")
    if upstream_density_kg_m3 <= 0 or half_width_m <= 0 or wall_m <= 0:
        raise ValueError("density, half-width and wall thickness must be positive")
    if not isinstance(steps, int) or isinstance(steps, bool) or steps < 1:
        raise ValueError("steps must be a positive integer")

    def derivatives(xi: float) -> tuple[float, float]:
        f = top_hat_shape(xi, half_width_m, wall_m)
        return (bubble_velocity_m_s * (f - 1.0),
                bubble_velocity_m_s * shape_gradient_per_m(xi, half_width_m, wall_m))

    xi, log_j = xi_initial_m, 0.0
    dt = elapsed_s / steps
    for _ in range(steps):
        k1x, k1j = derivatives(xi)
        k2x, k2j = derivatives(xi + dt * k1x / 2.0)
        k3x, k3j = derivatives(xi + dt * k2x / 2.0)
        k4x, k4j = derivatives(xi + dt * k3x)
        xi += dt * (k1x + 2*k2x + 2*k3x + k4x) / 6.0
        log_j += dt * (k1j + 2*k2j + 2*k3j + k4j) / 6.0
    jacobian = math.exp(log_j)
    return CharacteristicState(
        xi_m=xi,
        x_m=xi + bubble_velocity_m_s * elapsed_s,
        density_kg_m3=upstream_density_kg_m3 / jacobian,
        jacobian=jacobian,
        f=top_hat_shape(xi, half_width_m, wall_m),
    )
