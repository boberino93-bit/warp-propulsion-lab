# v0.3.24 — preregistered empirical holdout-null gate — 2026-09-17 07:31 UTC

External activity: public repository checked before research; 0 stars, 0 forks, discussions disabled, no open issues or PRs, and no accessible external experimental result, correction, student inquiry, collaboration offer or safety issue.

Bounded advance: added an empirical holdout-null gate that freezes a two-sided threshold from an independent synthetic null-calibration ensemble, then evaluates false positives and a 20 µN injected signal on separate holdout streams. This avoids tuning and evaluating the threshold on the same trials. It is not yet a general permutation proof or real sham calibration.

Falsification: reject the gate if independent holdout null false positives do not remain near preregistered alpha across artifact mismatch/distribution shift, or if useful injected-signal sensitivity is lost. Exact-head CI was pending at session creation. No hardware or measured thrust claimed.

NEXT ONE TEST: sweep distribution shift between calibration and holdout (noise amplitude, thermal drift and reversal bias) and quantify where empirical false-positive control fails.
