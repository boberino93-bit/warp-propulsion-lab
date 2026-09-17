"""Synthetic stationarity-envelope scan for the empirical null gate.

This is protocol design, not hardware evidence. The calibration distribution is
frozen and a declared grid of holdout shifts is tested against an FPR ceiling.
"""
from __future__ import annotations
from dataclasses import dataclass
from src.distribution_shift_gate import evaluate_distribution_shift

@dataclass(frozen=True)
class EnvelopePoint:
    shift: float
    false_positive_rate: float
    detection_rate: float
    passes: bool


def scan_one_parameter(parameter: str, shifts=(0.0,0.02,0.05,0.10,0.15,0.20,0.25),
                       fpr_ceiling=0.02, trials=2000):
    """Return a fixed, non-adaptive scan relative to the v0.3.25 baseline.

    `shift` is fractional: sigma, reversal bias and thermal span are multiplied
    by (1+shift); mismatch moves from 0.90 toward 1 by +shift (absolute).
    """
    if parameter not in {"sigma","reversal_bias","thermal","mismatch"}:
        raise ValueError("unknown parameter")
    if not 0 < fpr_ceiling < 0.5 or trials < 100:
        raise ValueError("invalid scan settings")
    out=[]
    for s in shifts:
        if s < 0: raise ValueError("negative shift")
        kw={"calibration_trials":4000,"holdout_trials":trials}
        if parameter=="sigma": kw["hold_sigma_n"]=5e-6*(1+s)
        elif parameter=="reversal_bias": kw["hold_reversal_bias_n"]=15e-6*(1+s)
        elif parameter=="thermal": kw["hold_thermal_span_n"]=10e-6*(1+s)
        else: kw["hold_mismatch"]=min(1.0,0.90+s)
        r=evaluate_distribution_shift(**kw)
        out.append(EnvelopePoint(s,r.false_positive_rate,r.detection_rate,
                                 r.false_positive_rate <= fpr_ceiling))
    return tuple(out)


def scan_combined(shifts=(0.0,0.01,0.02,0.05,0.10), fpr_ceiling=0.02, trials=2000):
    """Shift all four tested artifact dimensions together by the same fraction."""
    out=[]
    for s in shifts:
        if s < 0: raise ValueError("negative shift")
        r=evaluate_distribution_shift(hold_sigma_n=5e-6*(1+s),
            hold_reversal_bias_n=15e-6*(1+s), hold_thermal_span_n=10e-6*(1+s),
            hold_mismatch=min(1.0,0.90+s), calibration_trials=4000,
            holdout_trials=trials)
        out.append(EnvelopePoint(s,r.false_positive_rate,r.detection_rate,
                                 r.false_positive_rate <= fpr_ceiling))
    return tuple(out)


def last_passing(points):
    passed=[p for p in points if p.passes]
    return passed[-1] if passed else None
