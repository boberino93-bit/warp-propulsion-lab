"""Empirical holdout-null gate for the imperfect-sham protocol.

Synthetic protocol study only. Calibration null campaigns are separated from
holdout evaluation campaigns so the detection threshold is not tuned on the
same trials used to report false-positive rate.
"""
from __future__ import annotations
import math
import random
from dataclasses import dataclass
from src.imperfect_sham import _estimate

@dataclass(frozen=True)
class EmpiricalNullResult:
    mismatch_fraction: float
    threshold_n: float
    false_positive_rate: float
    detection_rate: float
    calibration_trials: int
    holdout_trials: int
    alpha: float


def _upper_quantile(values, q):
    if not values or not 0 < q < 1:
        raise ValueError("invalid quantile")
    ordered=sorted(values)
    # Conservative nearest-rank empirical quantile.
    rank=max(1, math.ceil(q*len(ordered)))
    return ordered[min(rank-1, len(ordered)-1)]


def evaluate_empirical_null_gate(mismatch_fraction, force_n=20e-6, sigma_art_n=5e-6,
                                 reversal_bias_n=15e-6, thermal_span_n=10e-6,
                                 repeats=16, calibration_trials=4000,
                                 holdout_trials=4000, alpha=0.01, seed=324):
    """Freeze an empirical two-sided gate on independent synthetic null runs.

    This models preregistration by using one RNG stream for calibration and
    independent streams for holdout null and signal evaluation. It is not a
    substitute for real blocked/sham calibration data.
    """
    if not 0 <= mismatch_fraction <= 1 or calibration_trials < 100 or holdout_trials < 1:
        raise ValueError("invalid parameters")
    if not 0 < alpha < 0.5:
        raise ValueError("invalid alpha")
    cal_rng=random.Random(seed)
    calibration=[abs(_estimate(0.0,mismatch_fraction,reversal_bias_n,sigma_art_n,
                               thermal_span_n,repeats,cal_rng))
                 for _ in range(calibration_trials)]
    threshold=_upper_quantile(calibration,1-alpha)
    null_rng=random.Random(seed+1)
    signal_rng=random.Random(seed+2)
    fp=det=0
    for _ in range(holdout_trials):
        fp += abs(_estimate(0.0,mismatch_fraction,reversal_bias_n,sigma_art_n,
                            thermal_span_n,repeats,null_rng)) >= threshold
        det += abs(_estimate(force_n,mismatch_fraction,reversal_bias_n,sigma_art_n,
                             thermal_span_n,repeats,signal_rng)) >= threshold
    return EmpiricalNullResult(mismatch_fraction,threshold,fp/holdout_trials,
                               det/holdout_trials,calibration_trials,
                               holdout_trials,alpha)
