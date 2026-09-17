"""Synthetic stress tests for the blinded campaign gate.

This module deliberately models artifacts that can mimic polarity-reversing thrust.
It is simulation/protocol code only; it does not represent measured hardware data.
"""
from __future__ import annotations
import math
import random
from dataclasses import dataclass

from src.blinded_campaign import campaign_threshold_n


@dataclass(frozen=True)
class StressResult:
    rho: float
    reversal_bias_n: float
    false_positive_rate: float
    trials: int


def _stationary_ar1(n: int, sigma_n: float, rho: float, rng: random.Random):
    if n < 1 or sigma_n <= 0 or not 0 <= rho < 1:
        raise ValueError("invalid AR(1) parameters")
    x = rng.gauss(0.0, sigma_n)
    out = [x]
    innovation_sigma = sigma_n * math.sqrt(1.0 - rho * rho)
    for _ in range(n - 1):
        x = rho * x + rng.gauss(0.0, innovation_sigma)
        out.append(x)
    return out


def _null_estimate(samples_per_polarity: int, sigma_art_n: float, rho: float,
                   reversal_bias_n: float, rng: random.Random) -> float:
    """Return a zero-thrust polarity-aligned estimate.

    A reversal-correlated artifact is +b in ON+ and -b in ON-. It therefore
    survives the polarity-aligned estimator exactly like a real force. AR(1)
    noise represents time correlation within each polarity block.
    """
    plus_noise = _stationary_ar1(samples_per_polarity, sigma_art_n, rho, rng)
    minus_noise = _stationary_ar1(samples_per_polarity, sigma_art_n, rho, rng)
    plus = [reversal_bias_n + x for x in plus_noise]
    minus = [-reversal_bias_n + x for x in minus_noise]
    n = samples_per_polarity
    return (sum(plus) - sum(minus)) / (2.0 * n)


def stress_false_positive_rate(sigma_art_n: float = 5e-6, systematic_bound_n: float = 10e-6,
                               samples_per_polarity: int = 16, rho: float = 0.0,
                               reversal_bias_n: float = 0.0, trials: int = 20000,
                               seed: int = 320, z: float = 5.0) -> StressResult:
    """Estimate false positives under correlated noise and reversal bias."""
    if reversal_bias_n < 0 or trials < 1:
        raise ValueError("invalid stress parameters")
    threshold = campaign_threshold_n(sigma_art_n, systematic_bound_n, samples_per_polarity, z)
    rng = random.Random(seed)
    hits = 0
    for _ in range(trials):
        if abs(_null_estimate(samples_per_polarity, sigma_art_n, rho, reversal_bias_n, rng)) >= threshold:
            hits += 1
    return StressResult(rho, reversal_bias_n, hits / trials, trials)
