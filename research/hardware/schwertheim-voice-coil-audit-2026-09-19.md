# Audit: Schwertheim et al. voice-coil calibration against the frozen ±0.10 mN specification

**Audited:** 2026-09-19 01:30 UTC  
**Candidate:** hanging-pendulum thrust-balance calibration using an Akribis AVM12-6.4 voice-coil actuator  
**Primary source:** Schwertheim et al., *Review of Scientific Instruments* 92, 034502 (2021), DOI [10.1063/5.0037100](https://doi.org/10.1063/5.0037100)  
**Decision:** **REJECT for the current demonstrator gate**

## System boundary and physical scaling

The voice coil is an externally supported calibration actuator. Current in a magnetic field produces an interaction force; the equal-and-opposite reaction closes through the actuator support and laboratory structure. The method calibrates a balance and is not a self-contained propulsion mechanism.

The applicable nominal model remains (F=K_F(x,T,I)I), with electrical dissipation (P=I^2R). The independently measurable prediction is balance response versus the force transferred by the voice coil across the calibrated current range.

## What the publication demonstrates

The open-access primary paper reports:

- an AVM12-6.4 voice-coil actuator used for calibration traceability;
- an interlaboratory comparison between two hanging-pendulum balances;
- high linearity and stable calibration over several days;
- a published validated force interval of **0.5–100 mN**.

These are useful architecture and reproducibility results. They do not extend automatically below the tested interval.

## Frozen-gate comparison

| Frozen requirement | Published evidence found | Result |
| --- | --- | --- |
| Noncontact externally supported transfer | Voice-coil calibration architecture | Pass in principle |
| Signed -0.10/0/+0.10 mN data | Published validation begins at 0.5 mN; no signed ±0.10 mN sequence identified | Fail |
| Ten randomized signed cycles with bracketed zeros | Stable multi-day calibration, but frozen schedule not demonstrated | Fail |
| Independently traceable input-to-force chain at ±0.10 mN | Traceability intent is reported; no complete ±0.10 mN chain was demonstrated | Fail |
| (u_cle1.5) µN and (U_{95}le3.0) µN | No covariance-aware budget satisfying these limits at ±0.10 mN | Fail |
| (|E|+U_{95}le5.0) µN at both signs | No qualifying ±0.10 mN errors and uncertainties | Fail |
| Position, alignment, thermal, hysteresis/remanence, EM/cable, drift and interpolation terms | Relevant calibration controls are described, but the complete frozen numerical table was not reported at ±0.10 mN | Fail |
| Physical receiver/fixture reversal | No qualifying frozen reversal sequence identified | Fail |
| Redistributable construction source/rights | Open-access article does not establish redistributable CAD/electronics source rights for a student build | Fail |
| Delivered Canadian BOM within CAD 500–1,000 | No complete orderable Canadian BOM or delivered price | Fail |

## Controls required before reconsideration

A derivative candidate must add the exact signed ±0.10 mN schedule; bracketed actuator-off zeros; physical fixture reversal; equal-power thermal dummy; mapped gap/position and alignment; return-current and stray-field nulls; fixed cable routing; airflow/pressure and vibration monitoring; and covariance-aware uncertainty. Catalog actuator accuracy or source-meter resolution cannot replace end-to-end force uncertainty.

## Falsification result

The candidate is rejected because its validated range starts at 0.5 mN, five times the strictest target, and because the required signed data, complete uncertainty table, rights and Canadian BOM were not demonstrated. Extrapolation to 0.10 mN is forbidden.

No hardware was selected, priced as a complete system, purchased, built or tested.

## Rights and evidence status

The paper is open access; that does not by itself grant rights to reproduce every third-party actuator, instrument, drawing or proprietary component. This is a literature audit, not measured calibration or thrust.

## NEXT ONE TEST

Preregister a paper-only scaling calculation for the published AVM12-6.4 architecture at ±0.10 mN using manufacturer force-constant/current data and source-meter uncertainty. Stop if the required datasheets or covariance terms are unavailable; do not claim validation and make no purchase.
