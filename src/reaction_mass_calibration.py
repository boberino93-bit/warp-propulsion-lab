"""Uncertainty model for reaction-mass thrust-stand calibration."""
import math


def mass_flow(delta_mass_kg, duration_s):
    if delta_mass_kg <= 0 or duration_s <= 0:
        raise ValueError("positive mass loss and duration required")
    return delta_mass_kg / duration_s


def mass_flow_uncertainty(delta_mass_kg, duration_s, mass_reading_sigma_kg, duration_sigma_s=0.0):
    """1-sigma mdot uncertainty; delta mass is difference of two independent readings."""
    if delta_mass_kg <= 0 or duration_s <= 0 or mass_reading_sigma_kg < 0 or duration_sigma_s < 0:
        raise ValueError("invalid uncertainty inputs")
    mdot = mass_flow(delta_mass_kg, duration_s)
    rel2 = 2.0 * (mass_reading_sigma_kg / delta_mass_kg) ** 2 + (duration_sigma_s / duration_s) ** 2
    return mdot * math.sqrt(rel2)


def inferred_exhaust_velocity(force_n, mdot_kg_s):
    if force_n <= 0 or mdot_kg_s <= 0:
        raise ValueError("positive force and mass flow required")
    return force_n / mdot_kg_s


def inferred_velocity_uncertainty(force_n, force_sigma_n, mdot_kg_s, mdot_sigma_kg_s):
    if force_n <= 0 or mdot_kg_s <= 0 or force_sigma_n < 0 or mdot_sigma_kg_s < 0:
        raise ValueError("invalid uncertainty inputs")
    ve = inferred_exhaust_velocity(force_n, mdot_kg_s)
    return ve * math.sqrt((force_sigma_n / force_n) ** 2 + (mdot_sigma_kg_s / mdot_kg_s) ** 2)


def closure_z(force_n, force_sigma_n, mdot_kg_s, mdot_sigma_kg_s, ve_ref_m_s, ve_ref_sigma_m_s):
    """z score for F - mdot*Ve_ref, assuming independent 1-sigma inputs and zero pressure thrust."""
    if min(force_n, mdot_kg_s, ve_ref_m_s) <= 0 or min(force_sigma_n, mdot_sigma_kg_s, ve_ref_sigma_m_s) < 0:
        raise ValueError("invalid closure inputs")
    predicted = mdot_kg_s * ve_ref_m_s
    sigma_pred = math.sqrt((ve_ref_m_s * mdot_sigma_kg_s) ** 2 + (mdot_kg_s * ve_ref_sigma_m_s) ** 2)
    sigma_delta = math.sqrt(force_sigma_n ** 2 + sigma_pred ** 2)
    if sigma_delta == 0:
        return 0.0 if force_n == predicted else math.inf
    return (force_n - predicted) / sigma_delta


def calibration_passes(force_n, force_sigma_n, mdot_kg_s, mdot_sigma_kg_s,
                       ve_ref_m_s, ve_ref_sigma_m_s, max_abs_z=3.0, max_fractional_bias=0.05):
    """Predeclared gate: momentum closure within 3 sigma AND 5% fractional bias by default."""
    if max_abs_z <= 0 or max_fractional_bias <= 0:
        raise ValueError("positive gates required")
    predicted = mdot_kg_s * ve_ref_m_s
    frac_bias = abs(force_n - predicted) / predicted
    return abs(closure_z(force_n, force_sigma_n, mdot_kg_s, mdot_sigma_kg_s,
                         ve_ref_m_s, ve_ref_sigma_m_s)) <= max_abs_z and frac_bias <= max_fractional_bias
