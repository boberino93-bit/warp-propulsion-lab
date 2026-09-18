# Research session — 2026-09-17 22:30 UTC — v0.3.34

## External-activity check
No open PRs or open issues were visible at start. Main HEAD was project-owner merge dd59c19a8bd092a3e01272c346df37e93570b6a8. No new external experimental result, correction, student inquiry, collaboration offer, or safety issue was identified on accessible surfaces. Surfaces not independently enumerable are not claimed absent.

## Reconciliation
GitHub main was newer than the latest visible ChatGPT Library archive/session. Branch research/v0.3.34-noise-sigma-boundary was created directly from exact main HEAD; no force push or divergent overwrite.

## ONE bounded advance
Frozen synthetic threshold: 15.585078155794357 µN. Calibration sigma 5 µN; reversal bias 15 µN; thermal span 10 µN; mismatch 0.90; repeats 16; null seed 326; 10,000 holdout trials per point. Acceptance: 95% Wilson upper <= 2%.

Noise sigma increase results:
0.000: 119/10000, FPR .0119, Wilson upper .0142206 PASS
0.020: 140/10000, .0140, .0164965 PASS
0.050: 166/10000, .0166, .0192962 PASS
0.055: 167/10000, .0167, .0194035 PASS
0.060: 170/10000, .0170, .0197254 PASS
0.065: 172/10000, .0172, .0199399 PASS
0.070: 177/10000, .0177, .0204757 FAIL
0.075: 183/10000, .0183, .0211180 FAIL
0.100: 208/10000, .0208, .0237867 FAIL
0.150: 259/10000, .0259, .0291999 FAIL
0.200: 317/10000, .0317, .0353177 FAIL
0.250: 390/10000, .0390, .0429748 FAIL

Tested bracket: last-pass +6.5% / first-fail +7.0%, corresponding to 5.325 / 5.350 µN holdout sigma. Synthetic protocol result only.

## Evidence status
Not physical thrust, hardware calibration, peer review, independent replication, or propulsion discovery.

## NEXT ONE TEST
Run the unchanged 10,000-trial Wilson-qualified thermal-span slice using the same frozen threshold.
