"""Auditable uncertainty arithmetic for signed low-force transfer concepts.

Values are standard uncertainties in millinewtons. Allocations are not measurements.
"""
from __future__ import annotations
import math
from collections.abc import Mapping

FROZEN_U95_CEILING_MN = 0.005
COVERAGE_FACTOR = 2.0

def combined_u95_mn(components_mn: Mapping[str, float], *, coverage_factor: float = COVERAGE_FACTOR) -> float:
    """Return root-sum-square expanded uncertainty after strict validation."""
    if not components_mn:
        raise ValueError("at least one uncertainty component is required")
    if not math.isfinite(coverage_factor) or coverage_factor <= 0:
        raise ValueError("coverage_factor must be finite and positive")
    values = []
    for name, value in components_mn.items():
        if not name:
            raise ValueError("component names must be nonempty")
        if not math.isfinite(value) or value < 0:
            raise ValueError("standard uncertainties must be finite and nonnegative")
        values.append(value)
    return coverage_factor * math.sqrt(sum(value * value for value in values))

def passes_frozen_ceiling(components_mn: Mapping[str, float]) -> bool:
    """Apply the frozen inclusive U95 ceiling."""
    return combined_u95_mn(components_mn) <= FROZEN_U95_CEILING_MN
