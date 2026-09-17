"""Synthetic stress model for imperfect polarity-matched shams.

Protocol/simulation only. No hardware measurements are represented here.
"""
from __future__ import annotations
import math
import random
from dataclasses import dataclass
from src.blinded_campaign import campaign_threshold_n
from src.reversal_sham import reversal_sham_schedule

@dataclass(frozen=True)
class ImperfectShamResult:
    mismatch_fraction: float
    false_positive_rate: float
    detection_rate: float
    trials: int

def _long_memory(n, sigma_n, rng):
    """Finite multiscale correlated process approximating long-memory/1/f-like noise."""
    rhos=(0.3,0.6,0.8,0.9,0.96,0.985,0.995,0.999)
    components=[]
    for rho in rhos:
        x=rng.gauss(0.0,1.0); arr=[x]; innovation=math.sqrt(1-rho*rho)
        for _ in range(n-1):
            x=rho*x+rng.gauss(0.0,innovation); arr.append(x)
        components.append(arr)
    y=[sum(c[i] for c in components)/math.sqrt(len(components)) for i in range(n)]
    mean=sum(y)/n
    var=sum((v-mean)**2 for v in y)/n
    scale=sigma_n/math.sqrt(var)
    return [(v-mean)*scale for v in y]

def _estimate(force_n, mismatch_fraction, reversal_bias_n, sigma_n, thermal_span_n, repeats, rng):
    schedule=[label for _,label in reversal_sham_schedule(repeats,322)]
    noise=_long_memory(len(schedule),sigma_n,rng); values=[]
    for i,(label,eps) in enumerate(zip(schedule,noise)):
        t=(i-(len(schedule)-1)/2)/max(1,len(schedule)-1)
        polarity=1 if label.endswith('+') else -1 if label.endswith('-') else 0
        active=label.startswith('ON'); sham=label.startswith('SHAM')
        coupling=1.0 if active else (1.0-mismatch_fraction if sham else 0.0)
        nonlinear_thermal=thermal_span_n*(4*t*t-1/3)
        values.append(eps+nonlinear_thermal+reversal_bias_n*polarity*coupling+force_n*polarity*active)
    means={state:sum(v for v,s in zip(values,schedule) if s==state)/repeats for state in ('ON+','ON-','SHAM+','SHAM-')}
    return (means['ON+']-means['ON-']-means['SHAM+']+means['SHAM-'])/2

def evaluate_imperfect_sham(mismatch_fraction, force_n=20e-6, sigma_art_n=5e-6, systematic_bound_n=10e-6,
                            reversal_bias_n=15e-6, thermal_span_n=10e-6, repeats=16, trials=5000,
                            seed=323, z=5.0):
    if not 0 <= mismatch_fraction <= 1 or trials < 1: raise ValueError('invalid parameters')
    threshold=campaign_threshold_n(sigma_art_n,systematic_bound_n,repeats,z)
    null_rng=random.Random(seed); signal_rng=random.Random(seed+1); fp=det=0
    for _ in range(trials):
        fp += abs(_estimate(0.0,mismatch_fraction,reversal_bias_n,sigma_art_n,thermal_span_n,repeats,null_rng)) >= threshold
        det += abs(_estimate(force_n,mismatch_fraction,reversal_bias_n,sigma_art_n,thermal_span_n,repeats,signal_rng)) >= threshold
    return ImperfectShamResult(mismatch_fraction,fp/trials,det/trials,trials)
