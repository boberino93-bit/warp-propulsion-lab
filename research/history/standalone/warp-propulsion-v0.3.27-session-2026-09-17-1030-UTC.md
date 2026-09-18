# v0.3.27 — conservative stationarity-boundary refinement — 2026-09-17 10:30 UTC

PR #27 exact-head CI passed 156/156 tests in 53.770 s plus benchmark and was merged as b28212a0770c495c6bacd02eb501fc326da3b356.

ONE bounded advance: added conservative pass/fail boundary bracketing for preregistered synthetic stationarity grids. The method reports the last passing tested point and first failing tested point rather than interpolating unsupported precision.

No physical thrust stand, measured force, hardware calibration, independent replication, or novel propulsion mechanism is claimed.

NEXT ONE TEST: run high-sample preregistered grids for sigma, reversal bias, thermal span, mismatch and combined shift, then freeze only brackets with adequate Monte Carlo uncertainty.
