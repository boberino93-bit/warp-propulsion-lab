# Documentary specification: noncontact bidirectional 0.10 mN calibrator

**Frozen:** 2026-09-19 00:30 UTC  
**Status:** design acceptance specification; no hardware selected, purchased, built, or tested  
**Target:** independently traceable signed force at the DUT interface from -1.0 to +1.0 mN, with the strictest gate at ±0.10 mN

## Measurement boundary

The calibrator is an externally supported laboratory actuator. Its equal-and-opposite reaction closes through the laboratory support; it is not a propulsion device and cannot establish anomalous thrust. The measurand is signed force delivered across a noncontact actuator gap to the DUT-side receiver in the final measurement geometry.

The accepted implementation must document the complete chain from electrical input and geometry to force, the support reaction path, receiver coupling, position, alignment, temperature, cables, and the DUT readout. A force inferred only from actuator command is not traceable.

## Candidate principles retained for later screening

### Voice-coil / permanent-magnet actuator

Nominal relation: (F=K_F(x,T,I)I), with electrical dissipation (P=I^2R). Current reversal can reverse force, but acceptance requires an independently calibrated (K_F) map over position, temperature and current, including nonlinearity, hysteresis/remanence, return-current geometry and magnetic coupling to the stand. A catalog force constant is insufficient.

### Symmetric electrostatic actuator

Nominal relation for one gap: (F=	frac12 V^2,dC/dx). Voltage polarity alone does not reverse this attractive force. Signed actuation therefore requires two opposed, independently characterized electrodes or an equivalent mechanically symmetric selector. Acceptance requires traceable voltage, gap and capacitance-gradient measurements plus bounds for leakage, charge retention, patch potentials and electrostatic coupling. A one-sided electrode fails the signed-force requirement.

Neither principle is selected by this document.

## Frozen setpoints and run order

- Signed setpoints: -1.00, -0.50, -0.25, -0.10, 0, +0.10, +0.25, +0.50 and +1.00 mN.
- Ten complete randomized cycles, with a bracketed zero before and after every nonzero setpoint.
- Equal counts in each sign and both approach directions; the random schedule is committed before measurement.
- Calibration is performed in the final fixture, cable routing, environmental enclosure and receiver geometry.
- Warm-up and settling rules are fixed before outcomes. No exclusions or fit changes after viewing results.
- At least one independent reversal of the receiver/actuator geometry must distinguish commanded sign from fixed laboratory bias.

## Frozen uncertainty allocation at ±0.10 mN

Values below are maximum standard uncertainties, not demonstrated performance.

| Component | Maximum standard uncertainty (µN) |
| --- | ---: |
| reference realization / force constant | 0.6 |
| electrical readback | 0.3 |
| alignment and geometry | 0.3 |
| spatial nonuniformity / position | 0.5 |
| thermal state and dummy-power residual | 0.5 |
| hysteresis, remanence or charge memory | 0.4 |
| EM/electrostatic and cable coupling | 0.5 |
| repeatability and drift | 0.8 |
| fit and interpolation | 0.4 |
| **root-sum-square combined standard uncertainty** | **1.5** |
| **expanded uncertainty, k=2** | **3.0** |

The remaining 2.0 µN is a guard band for absolute signed calibration error. Acceptance at both -0.10 and +0.10 mN requires:

[
U_{95}=2u_cle 3.0 mumathrm{N},qquad |E|+U_{95}le 5.0 mumathrm{N}.
]

The 5.0 µN total gate preserves the earlier frozen reference-plus-transfer ceiling of 0.005 mN. Correlated terms must be combined with covariance rather than treated as independent.

## Required controls

1. actuator-off and receiver-absent nulls;
2. signed command reversal and physical fixture reversal;
3. equal-power thermal dummy, with matched timing and temperature logging;
4. de-energized and energized EM/electrostatic coupling checks at the readout and structure;
5. fixed cable routing plus a cable-motion null;
6. airflow/pressure, acoustic and vibration monitoring appropriate to the final environment;
7. mapped force versus gap/position and alignment;
8. repeated zero recovery, creep and time-drift characterization;
9. blinded/randomized order with all failed or saturated cycles retained;
10. independent electrical and dimensional readback, with certificate/scope and calibration dates recorded.

## Falsification and stopping rules

Reject an architecture before procurement if any required uncertainty term lacks a numerical bound, the support reaction path is undefined, signed force depends on an unverified symmetry, or independent SI traceability cannot be documented.

Reject measured performance if either sign fails (|E|+U_{95}le5.0) µN, if sign asymmetry after reversal exceeds 2.0 µN, if a required control correlates with the force channel beyond its allocation, or if the full covariance-aware budget exceeds 3.0 µN expanded uncertainty. Stop without substituting catalog resolution, repeatability or fit residual for uncertainty.

## Evidence and sources

- JCGM 100:2008, *Evaluation of measurement data—Guide to the expression of uncertainty in measurement*, establishes the uncertainty framework: https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf
- NIST, *Measurement Traceability*, distinguishes a documented unbroken calibration chain from an unsupported label: https://www.nist.gov/calibrations/measurement-traceability
- Schwertheim et al. (2021), DOI 10.1063/5.0037100, demonstrates an externally supported voice-coil force-transfer architecture and interlaboratory validation at 0.5–100 mN. Its reported 0.187/0.267 mN standard deviations do not satisfy this specification and are not evidence of 0.10 mN performance.

## Evidence status

This is a preregistered documentary requirement set. The numerical allocation is a design target, not measured uncertainty. No candidate has passed, and no physical calibration or thrust measurement occurred.

## NEXT ONE TEST

Audit one published noncontact voice-coil calibration implementation against this frozen specification, including its traceability chain, signed ±0.10 mN data, covariance-aware uncertainty, controls, construction rights and a delivered Canadian BOM. Reject missing gates and make no purchase.
