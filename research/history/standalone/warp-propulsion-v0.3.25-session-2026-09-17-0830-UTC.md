# v0.3.25 — empirical-gate distribution-shift envelope — 2026-09-17 08:30 UTC

## External-activity check
Before research, the public repository was inspected. `main` was `446e71807dca6d1f10ff1c41df588afddc6ab609`, the v0.3.24 merge. Open issues returned none. Accessible recent session commits were project-owner research/integration commits; no external experimental result, correction, student inquiry, collaboration offer or safety issue was found. Some requested surfaces were not independently available in the connector during this run, so absence there is not claimed.

## ONE bounded advance
The empirical threshold was frozen on a baseline synthetic calibration distribution, then holdout artifact parameters were shifted without recalibration. Baseline: mismatch 0.90, sigma 5 µN, reversal bias 15 µN, thermal span 10 µN, 4,000 calibration and 4,000 holdout trials, alpha 1%. The deterministic-seed reproduction yielded threshold 15.585 µN and matched FPR 1.20%. Holdout noise at 1.25x/1.5x/2x yielded FPR 4.075%/8.0%/15.675%; mismatch 0.95/1.00 yielded 5.425%/16.0%; reversal bias 1.25x/1.5x yielded 61.525%/99.925%. Synthetic only, no hardware measurements.

## Decision
A calibration gate is invalid outside a bounded artifact distribution. Reversal-correlated bias is the dominant tested vulnerability. Candidate hardware data must be rejected when contemporaneous sham/control channels leave a preregistered stationarity envelope rather than post-hoc widening or refitting the gate.

## NEXT ONE TEST
Find maximum one-at-a-time and combined shifts that keep holdout false positives <=2%, then preregister them as control-channel stationarity requirements.
