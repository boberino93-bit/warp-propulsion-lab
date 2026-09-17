"""Non-contact force cross-calibration model.

This models a separately characterized magnetic actuator as F=k*I. It is a
calibration channel, not propulsion. The reaction reservoir is the stationary
actuator/support/environment outside the thrust-stand boundary.
"""
import math


def magnetic_force(current_a, force_constant_n_per_a):
    if not math.isfinite(current_a) or not math.isfinite(force_constant_n_per_a):
        raise ValueError("finite inputs required")
    if force_constant_n_per_a <= 0:
        raise ValueError("positive force constant required")
    return current_a * force_constant_n_per_a


def magnetic_force_uncertainty(current_a, current_sigma_a,
                               force_constant_n_per_a,
                               force_constant_sigma_n_per_a):
    """First-order independent 1-sigma uncertainty for F=kI."""
    vals = (current_a, current_sigma_a, force_constant_n_per_a,
            force_constant_sigma_n_per_a)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("finite inputs required")
    if current_sigma_a < 0 or force_constant_sigma_n_per_a < 0 or force_constant_n_per_a <= 0:
        raise ValueError("invalid uncertainty/model inputs")
    return math.sqrt((force_constant_n_per_a * current_sigma_a) ** 2 +
                     (current_a * force_constant_sigma_n_per_a) ** 2)


def cross_calibration_z(magnetic_force_n, magnetic_sigma_n,
                        deadweight_force_n, deadweight_sigma_n,
                        stand_repeatability_sigma_n=0.0):
    """Difference between independent channels normalized by combined sigma."""
    sigmas = (magnetic_sigma_n, deadweight_sigma_n, stand_repeatability_sigma_n)
    if any((not math.isfinite(s) or s < 0) for s in sigmas):
        raise ValueError("finite nonnegative uncertainties required")
    sigma = math.sqrt(sum(s*s for s in sigmas))
    delta = magnetic_force_n - deadweight_force_n
    if sigma == 0:
        return 0.0 if delta == 0 else math.copysign(math.inf, delta)
    return delta / sigma


def cross_calibration_gate(magnetic_force_n, magnetic_sigma_n,
                           deadweight_force_n, deadweight_sigma_n,
                           stand_repeatability_sigma_n=0.0,
                           max_abs_z=3.0, max_fractional_difference=0.05):
    """Require same sign, <=3 sigma agreement and <=5% magnitude difference."""
    if deadweight_force_n == 0 or max_abs_z <= 0 or max_fractional_difference <= 0:
        raise ValueError("invalid gate inputs")
    z = cross_calibration_z(magnetic_force_n, magnetic_sigma_n,
                            deadweight_force_n, deadweight_sigma_n,
                            stand_repeatability_sigma_n)
    frac = abs(magnetic_force_n-deadweight_force_n)/abs(deadweight_force_n)
    same_sign = magnetic_force_n * deadweight_force_n > 0
    return same_sign and abs(z) <= max_abs_z and frac <= max_fractional_difference
