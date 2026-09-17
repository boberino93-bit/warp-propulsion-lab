"""Conservative refinement of synthetic stationarity-envelope boundaries.

Protocol design only. This module does not encode hardware limits. It brackets
where the deterministic-seed synthetic holdout FPR first exceeds a declared
ceiling, using a fixed grid and increased trials near that boundary.
"""
from __future__ import annotations
from dataclasses import dataclass
from src.stationarity_envelope import scan_one_parameter, scan_combined

@dataclass(frozen=True)
class BoundaryBracket:
    last_passing_shift: float | None
    first_failing_shift: float | None
    last_passing_fpr: float | None
    first_failing_fpr: float | None
    trials: int


def refine_boundary(parameter: str, shifts, fpr_ceiling=0.02, trials=5000):
    """Return the first pass-to-fail bracket on a preregistered increasing grid.

    A bracket, rather than a fitted boundary, avoids implying precision finer
    than the tested Monte Carlo grid. All points are evaluated; no adaptive
    stopping or post-hoc grid selection is performed inside this function.
    """
    shifts=tuple(shifts)
    if not shifts or any(b <= a for a,b in zip(shifts, shifts[1:])):
        raise ValueError("shifts must be a nonempty strictly increasing grid")
    pts = scan_combined(shifts, fpr_ceiling, trials) if parameter == "combined" else scan_one_parameter(parameter, shifts, fpr_ceiling, trials)
    last=None
    for p in pts:
        if p.passes:
            last=p
        elif last is not None:
            return BoundaryBracket(last.shift,p.shift,last.false_positive_rate,p.false_positive_rate,trials)
        else:
            return BoundaryBracket(None,p.shift,None,p.false_positive_rate,trials)
    return BoundaryBracket(last.shift if last else None,None,last.false_positive_rate if last else None,None,trials)
