# Preregistration: paper-only ±0.10 mN voice-coil scaling calculation

**Frozen:** 2026-09-19 02:30 UTC  
**Status:** preregistered before extraction or calculation  
**Starting commit:** `7eb1ccc8bb177da1d07b585d7ac5157fe3cd3cb3`

## Question

Can published manufacturer data for the Akribis AVM12-6.4 voice coil and official source-measure-unit specifications support a prospective, covariance-aware calculation at signed ±0.10 mN that satisfies the already-frozen noncontact calibrator limits?

This is a paper calculation only. It cannot validate the actuator at ±0.10 mN, select hardware, authorize a purchase, or constitute a force or propulsion measurement.

## Pinned source hierarchy

1. Schwertheim et al., *Review of Scientific Instruments* 92 (2021), DOI: https://doi.org/10.1063/5.0037100 — architecture and the published 0.5–100 mN validation interval.
2. Exact official Akribis AVM12-6.4 drawing/data sheet, including revision/date. The current official AVM family page is contextual only: https://www.akribis-sys.com/product-avm-standard-series/295.html . It identifies the family and publishes a ±10% force-constant tolerance for the current AVM12-10, but it is not a substitute for the exact historical AVM12-6.4 record.
3. Exact official Keysight B2902A data sheet/specification, including revision/date and calibration interval. Support landing page: https://www.keysight.com/us/en/support/B2902A/precision-source-measure-unit-2-ch-100fa-210v-3a-dc-10-5a-pulse.html .

No distributor summary, search snippet, catalog resolution, later-family model, or paper's nominal component label may replace a missing exact specification.

## Frozen model and units

For each sign,

[
F = K_F(x,T,I) I,qquad I_t = F_t/K_F,qquad P=I_t^2R
]

with (F_t=±100 mumathrm{N}), (K_F) in N/A, (I) in A, (R) in ohms, and (P) in W.

The standard uncertainty is to be evaluated in force units:

[
u_F^2=(Iu_K)^2+(Ku_I)^2+2KI,mathrm{cov}(K,I)
+u_{x,F}^2+u_{T,F}^2+u_{mathrm{nl},F}^2+u_{mathrm{hys},F}^2
+u_{mathrm{EM},F}^2+u_{mathrm{drift},F}^2 .
]

Terms may be set to zero only when a pinned primary source supplies a defensible bound or the term is demonstrably absent. Unknown is not zero. Correlations must be propagated or conservatively bounded; independence may not be assumed merely because values come from separate tables.

## Frozen extraction table

Extract verbatim, with page/table/condition:

- AVM12-6.4 force constant, tolerance/uncertainty and distribution;
- position, current and temperature dependence of force constant;
- resistance and its temperature condition;
- nonlinearity, hysteresis/remanence and drift bounds;
- B2902A selected current range, programming and measurement accuracy, resolution, noise, temperature coefficient, time/calibration terms;
- calibration status required for the stated instrument specifications;
- evidence for covariance or a conservative worst-case correlation bound.

Calculate only after every required field is populated: signed current, electrical power, each standard-uncertainty contribution in µN, covariance contribution, combined (u_c), (U_{95}=2u_c), and guard-banded error.

## Frozen acceptance and falsification

Both signs must satisfy:

- (u_c ≤ 1.5 mumathrm{N});
- (U_{95} ≤ 3.0 mumathrm{N});
- (|E|+U_{95} ≤ 5.0 mumathrm{N}).

Stop without a numerical performance claim if the exact official AVM12-6.4 data sheet cannot be authenticated; the force-constant uncertainty or its position/temperature/current conditions are absent; the selected B2902A range accuracy cannot be established; calibration state is unspecified; or covariance and the remaining mechanism-specific terms cannot be bounded. A nominal current computed from an unqualified force constant is not an uncertainty result.

## Controls and scope

The eventual physical design still requires signed reversal, bracketed zeros, independent force traceability, and thermal, electromagnetic, cable, airflow, vibration and drift controls. This calculation tests only whether published component specifications could close one prospective uncertainty table. No hardware is selected, purchased, built or tested.

## Next ONE test

Execute the frozen extraction and calculation exactly once from authenticated, revision-pinned manufacturer documents. If any stop condition fires, retain the incomplete table and report no estimate.
