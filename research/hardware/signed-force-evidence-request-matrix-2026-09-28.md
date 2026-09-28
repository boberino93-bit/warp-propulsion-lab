# Preregistration — minimum signed-force evidence request matrix

Status: **FROZEN when merged; documentary schema only**  
Date: 2026-09-28  
Target: student-reproducible `-0.10/0/+0.10 mN` reference-force qualification  
Families: symmetric differential mechanical transfer; installed-geometry current-reversed voice coil

## Purpose

The prior published-candidate screen stopped because neither accessible record supplied the minimum signed-reversal evidence. This matrix freezes the exact evidence needed before any author or supplier contact. It does not request unpublished personal information, select hardware, authorize a purchase, or relax any existing acceptance limit.

## Shared provenance and identity record

Every submitted dataset must include:

| Field | Required form | Failure condition |
|---|---|---|
| Source identity | DOI/report URL, title, authors, publication date | Missing or unverifiable source |
| Artifact identity | exact apparatus revision, drawing/BOM revision, software commit and data-package hash | mutable or unidentified implementation |
| Rights | license or explicit permission for each redistributed code, drawing, document and dataset | redistribution rights unknown |
| Sign convention | diagram defining positive axis, receiver, Earth/support reaction path and every sign transform | sign assigned only in analysis or by relabeling |
| Conditions | UTC timestamps; location; pressure; temperature; humidity; airflow; vibration; magnetic field; cable state | conditions absent for any retained cycle |
| Traceability | calibration laboratory/certificate identifier, calibration date, value, standard uncertainty, coverage and scope | manufacturer nominal value only |
| Exclusions | frozen, machine-readable reason codes; all attempted cycles retained | outcome-based deletion or seed/cycle replacement |
| Integrity | raw-file SHA-256, schema version and an append-only correction record | silent replacement or unverifiable raw data |

## Frozen cycle table

One row per physical setpoint cycle, retained in randomized execution order:

`schema_version, family, apparatus_revision, run_id, cycle_id, order_index, timestamp_utc, blinded_label, requested_sign, requested_force_mN, realized_input, input_unit, pre_zero_mN, response_mN, post_zero_mN, corrected_response_mN, reference_force_mN, error_uN, temperature_C, humidity_percent, pressure_Pa, airflow_m_per_s, vibration_metric, magnetic_field_uT, cable_state, fixture_orientation, sham_state, operator_note_code, exclusion_code, raw_file_sha256`.

Required schedule:

- ten independently randomized bracketed-zero cycles at `-0.10 mN`;
- ten at `+0.10 mN`;
- ten zero/sham cycles;
- at least one complete physical fixture reversal followed by the same schedule;
- sign labels blinded during primary reduction;
- no replacement of failed or excluded cycles.

## Shared uncertainty table

For every term record `estimate, unit, standard_uncertainty, distribution, divisor, sensitivity_coefficient, signed_contribution, covariance_group, covariance_or_bound, degrees_of_freedom, provenance`.

Mandatory terms include input reference, transfer/force constant, alignment, zero interpolation, repeatability, reversal asymmetry, drift, thermal response, electromagnetic/electrostatic coupling, cable force, airflow, vibration, digitization and analysis model. Unknown covariance is not zero.

Frozen acceptance at each sign:

- `u_c <= 1.5 µN`;
- `U95(k=2) <= 3.0 µN`;
- `|error| + U95 <= 5.0 µN`;
- complete-reversal asymmetry `<= 2.0 µN`;
- benign sham/null results consistent with zero under the same guard band.

## Family M — symmetric differential mechanical transfer

Additional required fields:

- individually calibrated differential-mass values and certificates;
- measured or traceably bounded local gravity;
- air and artifact density with buoyancy correction;
- path geometry, `cos(theta)`, signed transfer ratio and covariance;
- same characterized load transferred through both opposed paths;
- pulley/filament/flexure stiffness, friction, stiction, hysteresis, creep and zero recovery;
- fixture reversal and equal-load sham;
- load positioning energy recorded as an artifact input.

The signed model remains

`F_M = Δm g_local (1 - rho_air/rho_mass) cos(theta) eta_transfer`.

Falsification: reject if the negative sign is created only by relabeling, if different unlinked loads define the two signs, or if any transfer term is unmeasured.

## Family E — installed current-reversed voice coil

Additional required fields:

- exact coil, magnet, fixture and current-source revisions;
- installed position and gap for every cycle;
- traceable measured current at both polarities, voltage and electrical power;
- independent mechanical calibration of `k_F` at both signs;
- force versus current, position, temperature and magnetic history;
- polarity asymmetry, hysteresis, remanence, creep and drift;
- zero-current source-on, wiring-reversed, dummy-load and magnet/coil-absent controls;
- stray-field, grounding, cable-force, Joule-heating, airflow and vibration bounds.

The signed model remains

`F_E = k_F(x, T, I, history) I`, with `P = VI`.

Falsification: reject manufacturer-only `k_F`, another installed geometry, one polarity only, or a result that fails the common guard band.

## Minimum package and review outcome

A qualifying evidence package contains:

1. raw cycle table and raw instrument files;
2. randomized schedule and blinding key disclosed only after primary reduction;
3. calibration certificates and scope;
4. covariance-aware uncertainty workbook or machine-readable table;
5. drawings/BOM revisions and category-specific rights;
6. analysis code, environment and exact expected output;
7. complete negative/null results and correction history.

Review outcomes are only `COMPLETE`, `INCOMPLETE—REQUEST EXACT FIELD`, or `REJECTED—FROZEN GATE FAILED`. Missing evidence cannot be averaged against stronger fields.

## Safety, cost and evidence status

No high voltage, high-power laser, pressure or vacuum procedure is introduced. The CAD $500–$1,000 delivered-BOM gate and existing-tool offsets remain unchanged, but pricing is not requested until the evidence package clears the scientific gate.

This is a preregistration only. No author or supplier was contacted. No component, price, purchase, build, calibration, force measurement, thrust measurement or propulsion discovery exists.

## NEXT ONE TEST

Apply this frozen matrix to the public supplementary/raw-data locations associated with the DLR AST weight-on-string and Lam et al. voice-coil publications. Record each exact public artifact and stop each family at the first missing mandatory field. Do not contact an author or supplier and make no purchase.
