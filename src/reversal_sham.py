"""Synthetic polarity-matched sham control for reversal-correlated artifacts.

Protocol/simulation code only. No hardware measurements are represented here.
"""
from __future__ import annotations
import math
import random
from dataclasses import dataclass

from src.blinded_campaign import campaign_threshold_n


@dataclass(frozen=True)
class ShamGateResult:
    reversal_bias_n: float
    rho: float
    raw_false_positive_rate: float
    corrected_false_positive_rate: float
    corrected_detection_rate: float
    trials: int


def reversal_sham_schedule(repeats: int = 16, seed: int = 322):
    """Balanced randomized schedule with polarity-matched disabled shams.

    SHAM+/- applies the same polarity command as ON+/- while the candidate is
    physically disabled from producing thrust. OFF has no polarity command.
    """
    if repeats < 1:
        raise ValueError("repeats must be positive")
    labels = [x for x in ("ON+", "ON-", "SHAM+", "SHAM-", "OFF") for _ in range(repeats)]
    rng = random.Random(seed)
    rng.shuffle(labels)
    return tuple((f"R{i+1:03d}", label) for i, label in enumerate(labels))


def _ar1(n: int, sigma_n: float, rho: float, rng: random.Random):
    if n < 1 or sigma_n <= 0 or not 0 <= rho < 1:
        raise ValueError("invalid AR(1) parameters")
    x = rng.gauss(0.0, sigma_n)
    out = [x]
    innovation_sigma = sigma_n * math.sqrt(1.0 - rho * rho)
    for _ in range(n - 1):
        x = rho * x + rng.gauss(0.0, innovation_sigma)
        out.append(x)
    return out


def _estimate(force_n: float, reversal_bias_n: float, sigma_n: float, rho: float,
              thermal_span_n: float, repeats: int, schedule_seed: int,
              rng: random.Random):
    schedule = [label for _, label in reversal_sham_schedule(repeats, schedule_seed)]
    noise = _ar1(len(schedule), sigma_n, rho, rng)
    values = []
    for i, (label, eps) in enumerate(zip(schedule, noise)):
        centered_time = (i - (len(schedule) - 1) / 2.0) / max(1, len(schedule) - 1)
        polarity = 1 if label.endswith("+") else -1 if label.endswith("-") else 0
        active = 1 if label.startswith("ON") else 0
        values.append(eps + thermal_span_n * centered_time + reversal_bias_n * polarity + force_n * polarity * active)
    means = {label: sum(v for v, state in zip(values, schedule) if state == label) / repeats
             for label in ("ON+", "ON-", "SHAM+", "SHAM-")}
    raw = (means["ON+"] - means["ON-"]) / 2.0
    sham = (means["SHAM+"] - means["SHAM-"]) / 2.0
    return raw, raw - sham


def evaluate_reversal_sham(force_n: float = 20e-6, sigma_art_n: float = 5e-6,
                           systematic_bound_n: float = 10e-6, reversal_bias_n: float = 15e-6,
                           rho: float = 0.9, thermal_span_n: float = 10e-6,
                           repeats: int = 16, trials: int = 20000, seed: int = 322,
                           z: float = 5.0) -> ShamGateResult:
    """Compare raw polarity gate with a matched-sham corrected estimator."""
    if force_n < 0 or reversal_bias_n < 0 or thermal_span_n < 0 or trials < 1:
        raise ValueError("invalid sham-gate parameters")
    threshold = campaign_threshold_n(sigma_art_n, systematic_bound_n, repeats, z)
    rng_null = random.Random(seed)
    rng_signal = random.Random(seed + 1)
    raw_fp = corrected_fp = corrected_det = 0
    for _ in range(trials):
        raw, corrected = _estimate(0.0, reversal_bias_n, sigma_art_n, rho, thermal_span_n,
                                   repeats, seed, rng_null)
        raw_fp += abs(raw) >= threshold
        corrected_fp += abs(corrected) >= threshold
        _, signal_corrected = _estimate(force_n, reversal_bias_n, sigma_art_n, rho, thermal_span_n,
                                        repeats, seed, rng_signal)
        corrected_det += abs(signal_corrected) >= threshold
    return ShamGateResult(reversal_bias_n, rho, raw_fp / trials, corrected_fp / trials,
                          corrected_det / trials, trials)
