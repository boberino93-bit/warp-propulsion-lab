"""Low-risk deadweight force-injection calibration model.

This module models the reference force itself. Any pulley, filament, lever, or
other transfer mechanism is OUTSIDE this reference and must have a separately
measured transfer uncertainty; it must not be silently treated as unity.
"""
import math


def deadweight_force(mass_kg, gravity_m_s2, air_density_kg_m3=0.0,
                     weight_density_kg_m3=8000.0, sign=1):
    """Return signed apparent deadweight force m*g*(1-rho_air/rho_weight)."""
    if mass_kg <= 0 or gravity_m_s2 <= 0:
        raise ValueError("positive mass and gravity required")
    if air_density_kg_m3 < 0 or weight_density_kg_m3 <= 0:
        raise ValueError("invalid density")
    if air_density_kg_m3 >= weight_density_kg_m3:
        raise ValueError("air density must be below weight density")
    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or +1")
    return sign * mass_kg * gravity_m_s2 * (1.0 - air_density_kg_m3 / weight_density_kg_m3)


def deadweight_force_uncertainty(mass_kg, mass_sigma_kg, gravity_m_s2,
                                 gravity_sigma_m_s2, air_density_kg_m3=0.0,
                                 air_density_sigma_kg_m3=0.0,
                                 weight_density_kg_m3=8000.0,
                                 weight_density_sigma_kg_m3=0.0):
    """First-order independent 1-sigma uncertainty of apparent deadweight force."""
    if mass_kg <= 0 or gravity_m_s2 <= 0 or weight_density_kg_m3 <= 0:
        raise ValueError("positive nominal inputs required")
    if min(mass_sigma_kg, gravity_sigma_m_s2, air_density_kg_m3,
           air_density_sigma_kg_m3, weight_density_sigma_kg_m3) < 0:
        raise ValueError("uncertainties/density cannot be negative")
    if air_density_kg_m3 >= weight_density_kg_m3:
        raise ValueError("air density must be below weight density")
    b = 1.0 - air_density_kg_m3 / weight_density_kg_m3
    d_dm = gravity_m_s2 * b
    d_dg = mass_kg * b
    d_drhoa = -mass_kg * gravity_m_s2 / weight_density_kg_m3
    d_drhow = mass_kg * gravity_m_s2 * air_density_kg_m3 / (weight_density_kg_m3 ** 2)
    return math.sqrt((d_dm * mass_sigma_kg) ** 2 +
                     (d_dg * gravity_sigma_m_s2) ** 2 +
                     (d_drhoa * air_density_sigma_kg_m3) ** 2 +
                     (d_drhow * weight_density_sigma_kg_m3) ** 2)


def required_mass_for_force(force_n, gravity_m_s2, air_density_kg_m3=0.0,
                            weight_density_kg_m3=8000.0):
    """Mass needed for an apparent deadweight force magnitude."""
    if force_n <= 0 or gravity_m_s2 <= 0:
        raise ValueError("positive force and gravity required")
    b = 1.0 - air_density_kg_m3 / weight_density_kg_m3
    if b <= 0:
        raise ValueError("invalid buoyancy factor")
    return force_n / (gravity_m_s2 * b)


def recovery_z(measured_force_n, measured_sigma_n, reference_force_n,
               reference_sigma_n, transfer_sigma_n=0.0):
    """Signed recovery residual normalized by combined independent uncertainty."""
    if min(measured_sigma_n, reference_sigma_n, transfer_sigma_n) < 0:
        raise ValueError("uncertainties cannot be negative")
    sigma = math.sqrt(measured_sigma_n**2 + reference_sigma_n**2 + transfer_sigma_n**2)
    if sigma == 0:
        return 0.0 if measured_force_n == reference_force_n else math.copysign(math.inf, measured_force_n-reference_force_n)
    return (measured_force_n-reference_force_n)/sigma


def bidirectional_gate(measured_plus_n, measured_minus_n, sigma_measured_n,
                       reference_magnitude_n, sigma_reference_n,
                       transfer_sigma_n=0.0, max_abs_z=3.0,
                       max_fractional_bias=0.05):
    """Require recovery of both magnitude and sign for + and - injections."""
    if reference_magnitude_n <= 0 or sigma_measured_n < 0 or sigma_reference_n < 0 or transfer_sigma_n < 0:
        raise ValueError("invalid gate inputs")
    if max_abs_z <= 0 or max_fractional_bias <= 0:
        raise ValueError("positive gates required")
    refs = (reference_magnitude_n, -reference_magnitude_n)
    meas = (measured_plus_n, measured_minus_n)
    for m, r in zip(meas, refs):
        z = recovery_z(m, sigma_measured_n, r, sigma_reference_n, transfer_sigma_n)
        bias = abs(m-r)/reference_magnitude_n
        if abs(z) > max_abs_z or bias > max_fractional_bias:
            return False
    return measured_plus_n > 0 and measured_minus_n < 0
