"""Distribution-shift stress test for the empirical null gate.

Synthetic protocol study only. Calibration parameters are frozen while holdout
artifact parameters are shifted. No hardware measurements are represented.
"""
from __future__ import annotations
import random
from dataclasses import dataclass
from src.imperfect_sham import _estimate
from src.empirical_null_gate import _upper_quantile

@dataclass(frozen=True)
class ShiftGateResult:
    threshold_n: float
    false_positive_rate: float
    detection_rate: float
    calibration_trials: int
    holdout_trials: int


def frozen_calibration_threshold(cal_mismatch=0.90, cal_sigma_n=5e-6,
                                 cal_reversal_bias_n=15e-6,
                                 cal_thermal_span_n=10e-6, repeats=16,
                                 calibration_trials=4000, alpha=0.01, seed=325):
    """Compute the deterministic baseline threshold once for declared settings."""
    if not 0 <= cal_mismatch <= 1:
        raise ValueError("invalid mismatch")
    if cal_sigma_n <= 0 or min(cal_reversal_bias_n, cal_thermal_span_n) < 0:
        raise ValueError("invalid artifact parameter")
    if calibration_trials < 100 or not 0 < alpha < 0.5:
        raise ValueError("invalid sampling parameter")
    cal_rng = random.Random(seed)
    calibration = [abs(_estimate(0.0, cal_mismatch, cal_reversal_bias_n, cal_sigma_n,
                                 cal_thermal_span_n, repeats, cal_rng))
                   for _ in range(calibration_trials)]
    return _upper_quantile(calibration, 1-alpha)


def evaluate_distribution_shift(cal_mismatch=0.90, hold_mismatch=0.90,
                                cal_sigma_n=5e-6, hold_sigma_n=5e-6,
                                cal_reversal_bias_n=15e-6, hold_reversal_bias_n=15e-6,
                                cal_thermal_span_n=10e-6, hold_thermal_span_n=10e-6,
                                force_n=20e-6, repeats=16, calibration_trials=4000,
                                holdout_trials=4000, alpha=0.01, seed=325,
                                threshold_n=None):
    """Evaluate a holdout campaign; optionally reuse a precomputed threshold.

    Supplying ``threshold_n`` skips calibration generation only. Holdout RNG
    seeds and all force/artifact calculations are unchanged, so reuse is exactly
    equivalent when the supplied threshold came from the same frozen settings.
    """
    if not (0 <= cal_mismatch <= 1 and 0 <= hold_mismatch <= 1):
        raise ValueError("invalid mismatch")
    if min(cal_sigma_n, hold_sigma_n) <= 0 or min(cal_reversal_bias_n, hold_reversal_bias_n, cal_thermal_span_n, hold_thermal_span_n) < 0:
        raise ValueError("invalid artifact parameter")
    if calibration_trials < 100 or holdout_trials < 1 or not 0 < alpha < 0.5:
        raise ValueError("invalid sampling parameter")
    if threshold_n is None:
        threshold = frozen_calibration_threshold(cal_mismatch, cal_sigma_n,
            cal_reversal_bias_n, cal_thermal_span_n, repeats,
            calibration_trials, alpha, seed)
    else:
        threshold = float(threshold_n)
        if threshold <= 0:
            raise ValueError("invalid frozen threshold")
    null_rng = random.Random(seed+1)
    signal_rng = random.Random(seed+2)
    fp = det = 0
    for _ in range(holdout_trials):
        fp += abs(_estimate(0.0, hold_mismatch, hold_reversal_bias_n, hold_sigma_n,
                            hold_thermal_span_n, repeats, null_rng)) >= threshold
        det += abs(_estimate(force_n, hold_mismatch, hold_reversal_bias_n, hold_sigma_n,
                             hold_thermal_span_n, repeats, signal_rng)) >= threshold
    return ShiftGateResult(threshold, fp/holdout_trials, det/holdout_trials,
                           calibration_trials, holdout_trials)
