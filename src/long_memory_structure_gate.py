"""Preregistered synthetic stress test for long-memory structure shift.

This changes correlation structure while preserving each generated trace's
sample standard deviation. It represents no hardware measurement.
"""
from __future__ import annotations
import math
import random
from dataclasses import dataclass

from src.distribution_shift_gate import frozen_calibration_threshold
from src.reversal_sham import reversal_sham_schedule

BASE_RHOS = (0.3, 0.6, 0.8, 0.9, 0.96, 0.985, 0.995, 0.999)


@dataclass(frozen=True)
class LongMemoryStructureResult:
    persistence_power: float
    threshold_n: float
    false_positives: int
    detections: int
    trials: int

    @property
    def false_positive_rate(self):
        return self.false_positives / self.trials

    @property
    def detection_rate(self):
        return self.detections / self.trials


def _long_memory(n, sigma_n, rng, persistence_power):
    if n < 2 or sigma_n <= 0 or persistence_power <= 0:
        raise ValueError("invalid long-memory parameter")
    components = []
    for base_rho in BASE_RHOS:
        rho = base_rho ** persistence_power
        x = rng.gauss(0.0, 1.0)
        arr = [x]
        innovation = math.sqrt(1.0 - rho * rho)
        for _ in range(n - 1):
            x = rho * x + rng.gauss(0.0, innovation)
            arr.append(x)
        components.append(arr)
    y = [sum(c[i] for c in components) / math.sqrt(len(components)) for i in range(n)]
    mean = sum(y) / n
    var = sum((v - mean) ** 2 for v in y) / n
    if var == 0:
        raise ValueError("degenerate trace")
    scale = sigma_n / math.sqrt(var)
    return [(v - mean) * scale for v in y]


def _estimate(force_n, mismatch_fraction, reversal_bias_n, sigma_n,
              thermal_span_n, repeats, rng, persistence_power):
    schedule = [label for _, label in reversal_sham_schedule(repeats, 322)]
    noise = _long_memory(len(schedule), sigma_n, rng, persistence_power)
    values = []
    for i, (label, eps) in enumerate(zip(schedule, noise)):
        t = (i - (len(schedule) - 1) / 2) / max(1, len(schedule) - 1)
        polarity = 1 if label.endswith('+') else -1 if label.endswith('-') else 0
        active = label.startswith('ON')
        sham = label.startswith('SHAM')
        coupling = 1.0 if active else (1.0 - mismatch_fraction if sham else 0.0)
        thermal = thermal_span_n * (4 * t * t - 1 / 3)
        values.append(eps + thermal + reversal_bias_n * polarity * coupling
                      + force_n * polarity * active)
    means = {state: sum(v for v, s in zip(values, schedule) if s == state) / repeats
             for state in ('ON+', 'ON-', 'SHAM+', 'SHAM-')}
    return (means['ON+'] - means['ON-'] - means['SHAM+'] + means['SHAM-']) / 2


def evaluate_long_memory_structure(persistence_power=0.5, trials=10_000,
                                   threshold_n=None, seed=326,
                                   mismatch_fraction=0.90, sigma_n=5e-6,
                                   reversal_bias_n=15e-6,
                                   thermal_span_n=10e-6, repeats=16,
                                   force_n=20e-6):
    if persistence_power <= 0 or trials < 1:
        raise ValueError("invalid evaluation parameter")
    threshold = (frozen_calibration_threshold(seed=325) if threshold_n is None
                 else float(threshold_n))
    if threshold <= 0:
        raise ValueError("invalid frozen threshold")
    null_rng = random.Random(seed)
    signal_rng = random.Random(seed + 1)
    fp = det = 0
    for _ in range(trials):
        fp += abs(_estimate(0.0, mismatch_fraction, reversal_bias_n, sigma_n,
                            thermal_span_n, repeats, null_rng,
                            persistence_power)) >= threshold
        det += abs(_estimate(force_n, mismatch_fraction, reversal_bias_n, sigma_n,
                             thermal_span_n, repeats, signal_rng,
                             persistence_power)) >= threshold
    return LongMemoryStructureResult(persistence_power, threshold, fp, det, trials)
