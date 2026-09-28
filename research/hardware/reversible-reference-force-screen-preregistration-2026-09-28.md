# Preregistration — low-risk signed ±0.10 mN reference-force screen

Status: **FROZEN when merged; documentary screen only.**  
Date: 2026-09-28  
Target: signed `-0.10/0/+0.10 mN` calibration for a personal, student-reproducible demonstrator  
Budget: delivered CAD $500–$1,000; existing 3D printer, soldering station and multimeter

## Question

Can either of two low-risk, inherently reversible reference-force families satisfy the existing signed calibration, uncertainty, controls, rights, BOM and personal-prototype safety gates without high-power laser, high voltage, pressure or vacuum hardware?

The two frozen families are:

1. differential deadweight/symmetric filament transfer; and
2. current-reversed voice-coil force, independently calibrated against a mechanical reference.

This document does not select a design, component, supplier or purchase.

## Source basis

- NIST describes deadweight force as the conventional primary realization and reports traceable small-force mass artifacts: https://nvlpubs.nist.gov/nistpubs/jres/108/4/j84vanl.pdf
- NIST states applied deadweight uncertainty includes mass, local gravity and air density: https://www.nist.gov/programs-projects/calibration-force-transducers
- Lam et al. report a commercial voice-coil calibrator spanning 30–23,000 µN, but with reported steady-force uncertainty as high as 18.48%; it is relevant evidence, not automatic acceptance: https://doi.org/10.1016/j.measurement.2018.09.029
- DLR reports thrust-stand calibration by both a calibrated voice coil and a weight-on-string system: https://doi.org/10.1140/epjti/s40485-021-00074-7

Secondary descriptions, catalog claims and resolution values cannot substitute for primary signed calibration data and expanded uncertainty.

## Common frozen acceptance gates

At both `-0.10 mN` and `+0.10 mN`:

- combined standard uncertainty `u_c <= 1.5 µN`;
- expanded uncertainty `U95(k=2) <= 3.0 µN`;
- guard band `|error| + U95 <= 5.0 µN`;
- sign asymmetry after complete reversal `<= 2.0 µN`;
- ten randomized bracketed-zero cycles at each sign;
- null/reversal/thermal/electromagnetic/cable/airflow/vibration/drift controls within frozen allocations;
- independent SI traceability and a covariance-aware uncertainty table;
- complete construction source with redistribution rights or explicit permission;
- complete delivered Canadian BOM at CAD $500–$1,000, including fixtures, enclosure, shipping and taxes;
- no hazardous unsupervised laser, high-voltage, pressure or vacuum requirement.

A candidate fails if any mandatory field is missing. Do not infer that resolution, repeatability or linear-fit `R²` is expanded uncertainty.

## Family M — differential deadweight/symmetric transfer

### Boundary and scaling

The Earth/support structure is the external momentum reservoir. For a characterized apparent mass difference transferred along the measurement axis,

`F_M = Δm g_local (1 - rho_air/rho_mass) cos(theta) eta_transfer`.

The sign is produced by moving the same characterized differential load between symmetric opposed paths, not by relabeling a positive load. Quasi-static positioning power is an artifact/control input, not propulsion power.

### Mandatory evidence

- individually calibrated mass values near the required differential, certificates and uncertainty;
- measured local gravity or a traceable bounded correction;
- air density, mass density, alignment and buoyancy;
- symmetric geometry with signed transfer ratio;
- friction, pulley/filament stiffness, hysteresis, creep, stiction and zero recovery at both signs;
- measured fixture reversal and sham load;
- raw randomized cycles and full covariance;
- drawings, rights and complete BOM.

Falsification: reject if either sign cannot be independently realized, if transfer uncertainty is unmeasured, or if the common guard band fails.

## Family E — current-reversed voice coil

### Boundary and scaling

The coil/magnet fixture reacts against the external support. The signed force model is

`F_E = k_F(x, T, I, history) I`,

where current reversal changes sign only if the complete coil/magnet geometry and support reaction are characterized. Electrical input power is `P = VI`; heat is an artifact source, not useful thrust.

### Mandatory evidence

- exact actuator revision and construction rights;
- independent mechanical calibration of `k_F` at both current signs and at the installed position;
- traceable source-meter current with calibration date and uncertainty;
- force versus current, displacement, temperature and magnetic history;
- current-reversal asymmetry, hysteresis, remanence, creep and drift;
- matched source-on zero-current, reversed wiring, dummy-load and magnet/coil-absent controls;
- stray magnetic coupling, grounding, cable force, Joule heating, airflow and vibration bounds;
- raw randomized cycles, full covariance and complete Canadian BOM.

Falsification: reject if the force constant is manufacturer-only, measured at another geometry, lacks both signs, or cannot meet the common guard band. The published Lam range includes 0.10 mN, but its reported uncertainty range alone does not establish acceptance.

## Frozen comparison method

Screen exactly one published implementation from each family. For every field record: source, dated version, measured value, uncertainty type, sign evidence, rights, BOM and status `PASS/FAIL/UNKNOWN`. Stop a candidate at its first mandatory `FAIL`; retain later fields as `NOT REACHED`. An `UNKNOWN` mandatory field is a failure for acquisition.

No score averaging is permitted. Select nothing unless one candidate passes every common and family-specific gate. If both fail, retain the null result and define the smallest missing-evidence request; do not substitute components or prices.

## Controls, uncertainty and safety

Both candidates must use identical stand-side bracketed zeros, randomized sign order, complete fixture reversal, thermal logs, cable/airflow/vibration controls and blinded analysis. Unknown covariance is not zero. No physical build or operating instruction is authorized by this screen.

## Evidence status

Preregistration only. No hardware was selected, priced, purchased, built, calibrated or tested. No thrust or propulsion result exists.

## NEXT ONE TEST

Apply this frozen table once to one published differential-deadweight implementation and one published current-reversed voice-coil implementation. Stop each at its first mandatory failure; make no purchase.
