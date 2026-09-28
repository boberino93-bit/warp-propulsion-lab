# Published reversible reference-force candidate screen — 2026-09-28

Status: **bounded documentary result under the frozen 2026-09-28 protocol**  
Target: signed `-0.10/0/+0.10 mN`  
Starting main: `83c7b7dbc2dcc7197cdd1320855c688080344e12`

## Frozen method

Applied `reversible-reference-force-screen-preregistration-2026-09-28.md` once to one published implementation from each family. Each candidate stops at its first mandatory `FAIL` or mandatory `UNKNOWN`; later fields are `NOT REACHED`. Missing evidence is not assigned zero and resolution is not reclassified as expanded uncertainty.

## Family M — DLR AST weight-on-string calibration

Primary source: A. Neumann, J. Simon and J. Schmidt, “Thrust measurement and thrust balance development at DLR’s electric propulsion test facility,” *EPJ Techniques and Instrumentation* 8, 17 (2021), DOI [10.1140/epjti/s40485-021-00074-7](https://doi.org/10.1140/epjti/s40485-021-00074-7). The publisher version is CC BY 4.0.

Published implementation: a motorized contact plate causes the platform to lift weights; a wire and pulley turn the vertical weight force into a horizontal pull. The paper states a `0–250 mN` range, `2.5 mN` accuracy and `<0.25 mN` resolution for the AST balance, with weight and voice-coil calibration.

| Frozen field | Published evidence | Status |
|---|---|---|
| Signed `-0.10/0/+0.10 mN` realization by the same differential load on symmetric opposed paths | The documented weight-on-string system applies a one-direction horizontal pull. The source does not publish symmetric opposed paths or negative `-0.10 mN` cycles. | **FAIL — STOP** |
| `u_c <= 1.5 µN`, `U95 <= 3.0 µN`, guard band and reversal asymmetry | Not evaluated after stop. The stated `<0.25 mN` resolution and `2.5 mN` accuracy are not qualifying uncertainty at `0.10 mN`. | NOT REACHED |
| Ten randomized cycles, covariance, artifact controls, rights and delivered Canadian BOM | Not evaluated after stop. | NOT REACHED |

Smallest evidence request: raw bracketed-zero cycles using the same characterized differential load on two independently characterized opposed paths at `-0.10` and `+0.10 mN`, plus the signed transfer and uncertainty table. The published one-direction system cannot be converted into that evidence by relabeling its sign.

## Family E — Lam et al. commercial voice-coil calibrator

Primary source: J. K. Lam, S. C. Koay, C. H. Lim and K. H. Cheah, “A voice coil based electromagnetic system for calibration of a sub-micronewton torsional thrust stand,” *Measurement* 131, 597–604 (2019), DOI [10.1016/j.measurement.2018.09.029](https://doi.org/10.1016/j.measurement.2018.09.029).

Published implementation: a commercial voice coil and permanent magnet generated steady calibration forces from `30–23,000 µN`. The publisher record reports steady-force uncertainty errors of `7.80–18.48%`.

| Frozen field | Published evidence | Status |
|---|---|---|
| Current-reversed signed `-0.10/0/+0.10 mN` cycles at the installed geometry | The accessible primary publisher record reports magnitudes in a positive `30–23,000 µN` interval. It does not document negative-force cycles, complete current reversal, or current-reversal asymmetry at `±0.10 mN`. | **UNKNOWN mandatory field — FAIL/STOP** |
| `u_c <= 1.5 µN`, `U95 <= 3.0 µN`, guard band and reversal asymmetry | Not evaluated after stop. The reported percentage-uncertainty range is not silently mapped to an unreported signed `0.10 mN` point. | NOT REACHED |
| Independent mechanical calibration, full covariance/controls, rights and delivered Canadian BOM | Not evaluated after stop. | NOT REACHED |

Smallest evidence request: raw installed-geometry data for randomized bracketed-zero cycles under both current polarities at `±0.10 mN`, with mechanical reference values, current traceability, polarity asymmetry and the full covariance-aware uncertainty table.

## Result and boundary accounting

Both candidates failed at the first signed-reversal evidence gate. The deadweight reaction closes through Earth/support; the voice-coil reaction closes through the coil/magnet fixture and external support. Neither is propulsion. Positioning and electrical power are artifact inputs, and no power-to-thrust claim follows from this screen.

No candidate was selected. No component, supplier or price was substituted; no purchase, build, calibration, force measurement or thrust measurement occurred. Later rights, BOM and safety fields remain deliberately `NOT REACHED`.

## NEXT ONE TEST

Preregister one documentary evidence-request matrix for a student-reproducible signed-force calibrator, separating the minimum new measurements needed to qualify (a) symmetric differential mechanical transfer and (b) installed-geometry current reversal. Freeze the raw-data schema, sign convention and uncertainty fields before contacting any author or supplier; make no purchase.
