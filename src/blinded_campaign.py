"""Predeclared blinded campaign / Monte Carlo eligibility checks.

Synthetic statistics only. This module does not represent measured thrust.
"""
from __future__ import annotations
import math
import random
from dataclasses import dataclass

@dataclass(frozen=True)
class CampaignResult:
    injected_force_n: float
    detection_rate: float
    false_positive_rate: float
    trials: int


def campaign_threshold_n(sigma_art_n: float, systematic_bound_n: float, samples_per_polarity: int, z: float = 5.0) -> float:
    """Conservative threshold for a polarity-aligned campaign mean."""
    if sigma_art_n <= 0 or systematic_bound_n < 0 or samples_per_polarity < 1 or z <= 0:
        raise ValueError("invalid campaign parameters")
    sigma_mean = sigma_art_n / math.sqrt(2.0 * samples_per_polarity)
    return systematic_bound_n + z * sigma_mean


def _one_trial(force_n: float, sigma_n: float, bias_n: float, n: int, rng: random.Random) -> float:
    plus = [force_n + bias_n + rng.gauss(0.0, sigma_n) for _ in range(n)]
    minus = [-force_n + bias_n + rng.gauss(0.0, sigma_n) for _ in range(n)]
    return (sum(plus) - sum(minus)) / (2.0 * n)


def monte_carlo_campaign(injected_force_n: float, sigma_art_n: float, systematic_bound_n: float,
                         samples_per_polarity: int = 16, trials: int = 20000,
                         seed: int = 319, z: float = 5.0) -> CampaignResult:
    """Estimate detection and null false-positive rates with frozen rules."""
    if injected_force_n < 0 or trials < 1:
        raise ValueError("invalid Monte Carlo parameters")
    threshold = campaign_threshold_n(sigma_art_n, systematic_bound_n, samples_per_polarity, z)
    rng_signal = random.Random(seed)
    rng_null = random.Random(seed + 1)
    det = 0
    fp = 0
    for _ in range(trials):
        if _one_trial(injected_force_n, sigma_art_n, systematic_bound_n, samples_per_polarity, rng_signal) >= threshold:
            det += 1
        if abs(_one_trial(0.0, sigma_art_n, systematic_bound_n, samples_per_polarity, rng_null)) >= threshold:
            fp += 1
    return CampaignResult(injected_force_n, det / trials, fp / trials, trials)


def randomized_blind_schedule(repeats: int = 16, seed: int = 319):
    """Return reproducible balanced ON+/ON-/OFF/SHAM schedule for preregistration."""
    if repeats < 1:
        raise ValueError("repeats must be positive")
    labels = [c for c in ("ON+", "ON-", "OFF", "SHAM") for _ in range(repeats)]
    rng = random.Random(seed)
    rng.shuffle(labels)
    return tuple((f"R{i+1:03d}", label) for i, label in enumerate(labels))
