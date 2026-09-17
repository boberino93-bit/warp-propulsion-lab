"""Conservative uncertainty gate for Monte Carlo false-positive estimates.

Synthetic/protocol utility only. It does not establish a physical thrust threshold.
"""

from math import sqrt


def wilson_upper(successes: int, trials: int, z: float = 1.959963984540054) -> float:
    """Return the two-sided-normal Wilson interval upper endpoint.

    ``z`` defaults to the 95% normal critical value.  For a preregistered
    one-sided confidence requirement, callers should supply the corresponding
    one-sided critical value explicitly.
    """
    if trials <= 0:
        raise ValueError("trials must be positive")
    if successes < 0 or successes > trials:
        raise ValueError("successes must lie in [0, trials]")
    if z <= 0:
        raise ValueError("z must be positive")
    p = successes / trials
    z2 = z * z
    denom = 1.0 + z2 / trials
    center = (p + z2 / (2.0 * trials)) / denom
    half = z * sqrt(p * (1.0 - p) / trials + z2 / (4.0 * trials * trials)) / denom
    return min(1.0, center + half)


def false_positive_gate(successes: int, trials: int, ceiling: float = 0.02, z: float = 1.959963984540054) -> dict:
    """Require the uncertainty upper bound, not just point FPR, below ceiling."""
    if not 0.0 < ceiling < 1.0:
        raise ValueError("ceiling must lie strictly between zero and one")
    point = successes / trials if trials > 0 else float("nan")
    upper = wilson_upper(successes, trials, z=z)
    return {"successes": successes, "trials": trials, "point_fpr": point,
            "upper_fpr": upper, "ceiling": ceiling, "passes": upper <= ceiling}
