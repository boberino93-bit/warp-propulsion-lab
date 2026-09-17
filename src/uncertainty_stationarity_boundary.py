"""Uncertainty-aware synthetic stationarity-boundary scan.

Protocol/statistical code only. A point passes only if the Wilson upper
confidence endpoint for its holdout false-positive count is <= the declared
ceiling. This does not encode a physical hardware limit.
"""
from __future__ import annotations
from dataclasses import dataclass
from src.stationarity_envelope import scan_one_parameter, scan_combined
from theory.binomial_uncertainty_gate import wilson_upper

@dataclass(frozen=True)
class UncertaintyBoundaryPoint:
    shift: float
    false_positive_rate: float
    false_positives: int
    wilson_upper_fpr: float
    detection_rate: float
    passes: bool

@dataclass(frozen=True)
class UncertaintyBoundaryBracket:
    last_passing: UncertaintyBoundaryPoint | None
    first_failing: UncertaintyBoundaryPoint | None
    trials: int
    ceiling: float


def scan_uncertainty_boundary(parameter: str, shifts, trials=10000,
                              fpr_ceiling=0.02, z=1.959963984540054):
    """Evaluate a preregistered grid and bracket first uncertainty-aware failure."""
    shifts = tuple(shifts)
    if not shifts or any(b <= a for a, b in zip(shifts, shifts[1:])):
        raise ValueError("shifts must be a nonempty strictly increasing grid")
    if trials < 100 or not 0 < fpr_ceiling < 0.5 or z <= 0:
        raise ValueError("invalid scan settings")
    raw = (scan_combined(shifts, fpr_ceiling, trials) if parameter == "combined"
           else scan_one_parameter(parameter, shifts, fpr_ceiling, trials))
    points = []
    for p in raw:
        # The simulator reports hits/trials. Recover the exact deterministic hit count.
        hits = int(round(p.false_positive_rate * trials))
        upper = wilson_upper(hits, trials, z=z)
        points.append(UncertaintyBoundaryPoint(
            p.shift, hits / trials, hits, upper, p.detection_rate,
            upper <= fpr_ceiling))
    last = None
    for p in points:
        if p.passes:
            last = p
        elif last is not None:
            return tuple(points), UncertaintyBoundaryBracket(last, p, trials, fpr_ceiling)
        else:
            return tuple(points), UncertaintyBoundaryBracket(None, p, trials, fpr_ceiling)
    return tuple(points), UncertaintyBoundaryBracket(last, None, trials, fpr_ceiling)
