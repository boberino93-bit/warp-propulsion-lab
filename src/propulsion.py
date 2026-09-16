"""Ideal momentum and kinetic-power benchmarks. SI units; not hardware predictions."""
from __future__ import annotations

SPEED_OF_LIGHT_M_S = 299_792_458.0


def ideal_rocket_thrust(mass_flow_kg_s: float, exhaust_speed_m_s: float) -> float:
    """F=mdot*v_e in N, ideal collinear steady momentum exchange."""
    if mass_flow_kg_s < 0 or exhaust_speed_m_s < 0:
        raise ValueError("mass flow and exhaust speed must be nonnegative")
    return mass_flow_kg_s * exhaust_speed_m_s


def ideal_jet_kinetic_power(mass_flow_kg_s: float, exhaust_speed_m_s: float) -> float:
    """P=mdot*v_e^2/2 in W, inertial frame where incoming propellant is at rest."""
    if mass_flow_kg_s < 0 or exhaust_speed_m_s < 0:
        raise ValueError("mass flow and exhaust speed must be nonnegative")
    return 0.5 * mass_flow_kg_s * exhaust_speed_m_s**2


def photon_thrust(radiated_power_w: float) -> float:
    """F=P/c N for perfectly collimated photon exhaust (emitted power, not wall power)."""
    if radiated_power_w < 0:
        raise ValueError("radiated power must be nonnegative")
    return radiated_power_w / SPEED_OF_LIGHT_M_S
