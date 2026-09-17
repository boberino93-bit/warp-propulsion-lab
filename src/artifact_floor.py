"""Conservative thrust-stand artifact-floor eligibility model.

All inputs are forces in newtons. The model separates unknown-sign systematic
null-channel bounds from independent random 1-sigma noise. It is a screening
gate, not a claim that artifacts are Gaussian or that hardware has been tested.
"""
import math

def combined_random_sigma(*sigma_n):
    if not sigma_n or any((not math.isfinite(s) or s < 0) for s in sigma_n): raise ValueError("finite nonnegative sigma inputs required")
    return math.sqrt(sum(s*s for s in sigma_n))

def systematic_artifact_bound(*bounds_n):
    if not bounds_n or any((not math.isfinite(b) or b < 0) for b in bounds_n): raise ValueError("finite nonnegative artifact bounds required")
    return sum(bounds_n)

def minimum_detectable_thrust(random_sigma_n, systematic_bound_n, sigma_level=5.0):
    vals=(random_sigma_n, systematic_bound_n, sigma_level)
    if not all(math.isfinite(v) for v in vals) or random_sigma_n < 0 or systematic_bound_n < 0 or sigma_level <= 0: raise ValueError("invalid detection inputs")
    return systematic_bound_n + sigma_level * random_sigma_n

def artifact_corrected_snr(measured_force_n, random_sigma_n, systematic_bound_n):
    vals=(measured_force_n, random_sigma_n, systematic_bound_n)
    if not all(math.isfinite(v) for v in vals) or random_sigma_n <= 0 or systematic_bound_n < 0: raise ValueError("invalid SNR inputs")
    return max(0.0, abs(measured_force_n)-systematic_bound_n)/random_sigma_n

def candidate_is_eligible(measured_force_n, random_sigma_n, systematic_bound_n, calibrated_reference_floor_n=1e-4, sigma_level=5.0):
    if not math.isfinite(calibrated_reference_floor_n) or calibrated_reference_floor_n <= 0: raise ValueError("positive calibrated reference floor required")
    mdt=minimum_detectable_thrust(random_sigma_n, systematic_bound_n, sigma_level)
    return mdt < calibrated_reference_floor_n and abs(measured_force_n) >= mdt
