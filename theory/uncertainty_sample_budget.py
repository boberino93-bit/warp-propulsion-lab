"""Sample-size budget for the preregistered false-positive uncertainty gate.

Synthetic/protocol utility only. It does not establish a physical thrust threshold.
"""

from theory.binomial_uncertainty_gate import wilson_upper


def max_passing_false_positives(trials: int, ceiling: float = 0.02,
                                z: float = 1.959963984540054) -> dict:
    """Return largest integer false-positive count whose Wilson upper <= ceiling."""
    if trials <= 0:
        raise ValueError("trials must be positive")
    if not 0.0 < ceiling < 1.0:
        raise ValueError("ceiling must lie strictly between zero and one")
    if z <= 0:
        raise ValueError("z must be positive")
    lo, hi = 0, trials
    if wilson_upper(0, trials, z=z) > ceiling:
        return {"trials": trials, "max_false_positives": -1,
                "max_point_fpr": None, "upper_fpr": wilson_upper(0, trials, z=z),
                "ceiling": ceiling, "z": z}
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if wilson_upper(mid, trials, z=z) <= ceiling:
            lo = mid
        else:
            hi = mid - 1
    return {"trials": trials, "max_false_positives": lo,
            "max_point_fpr": lo / trials, "upper_fpr": wilson_upper(lo, trials, z=z),
            "ceiling": ceiling, "z": z}
