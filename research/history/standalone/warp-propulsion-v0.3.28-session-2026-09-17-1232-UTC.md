# v0.3.28 — uncertainty-aware false-positive gate — 2026-09-17 12:32 UTC

## External activity and provenance
Before research, public repository metadata showed main `0431fc3a9f1b6f5e2b3f751974874503f5201888`, zero stars, zero forks, zero open issues, and discussions disabled. No external experimental result, correction, student inquiry, collaboration offer, or safety report was found on accessible surfaces. Some requested social/review/commit-comment surfaces were not independently enumerable, so absence is not claimed there.

## ONE bounded advance
Added a conservative binomial uncertainty gate: a simulated stationarity point passes only when the Wilson confidence-interval upper endpoint for false positives is <= the preregistered ceiling. This prevents a low Monte Carlo point estimate from passing merely because the sample is too small.

Default z=1.959963984540054. Analytic checks: 10/1000 false positives gives point FPR 1.0% and Wilson upper about 1.831%, passing a 2% ceiling; 20/1000 fails because its upper endpoint exceeds 2%. Zero observed false positives still has a nonzero upper endpoint.

## Evidence status
Protocol/statistical code only. No hardware, measured thrust, propulsion discovery, peer review, or independent replication claimed.

## NEXT ONE TEST
Apply the uncertainty-aware <=2% gate to preregistered high-sample grids around the v0.3.27 last-pass/first-fail brackets for noise amplitude, reversal bias, thermal span, sham mismatch, and combined shift; freeze only brackets whose upper confidence bound passes.
