# Preregistration — opposed-electrode electrostatic calibrator documentary audit

**Frozen:** 2026-09-28 08:35 UTC  
**Status:** paper-only audit protocol; no design selected, purchased, built, energized or tested  
**Target:** signed force at ±0.10 mN under the existing noncontact-calibrator gate

## One bounded question

Can one published, independently documented opposed-electrode electrostatic implementation demonstrate all evidence needed to realize signed ±0.10 mN at the DUT interface with `U95 <= 3.0 µN` and `|E| + U95 <= 5.0 µN`, while also providing lawful construction information and a complete delivered Canadian BOM within CAD $500–$1,000?

A candidate passes only on published or manufacturer-authenticated evidence. Missing values remain missing; resolution, repeatability, simulation or a catalog tolerance cannot substitute for expanded uncertainty.

## Physical boundary and prediction

The actuator is externally supported. Electrical energy enters through the voltage source; the receiver experiences the commanded force and the equal-and-opposite momentum closes through the selected electrode, its mount and the laboratory support. This is a calibration force source, not a propulsion mechanism.

For a constant-voltage electrode pair with capacitance `C(x)`, the signed force component along coordinate `x` is

`F_x = 1/2 * (V - V_CPD)^2 * dC/dx`.

`V_CPD` is the effective contact/patch-potential offset. Voltage polarity alone cannot reverse the attractive force. Negative and positive setpoints must therefore select independently characterized electrodes on opposite sides of the receiver, or an equivalent published symmetric geometry whose support reactions and signs are explicit.

For a selected side `s in {-,+}`, the audit must report `F_s`, electrical input power including leakage, the measured or calculable `dC_s/dx`, and the reaction path. At ±0.10 mN the independently measurable prediction is that sign follows electrode selection and magnitude follows the traceable voltage/capacitance-gradient model within the frozen guard band.

## Evidence hierarchy

Use, in order:

1. peer-reviewed primary description and uncertainty table for the exact apparatus;
2. national-metrology-institute technical publication or report;
3. manufacturer-controlled drawing/data sheet for the exact revision;
4. accredited calibration certificate/scope for electrical and dimensional references;
5. supplier pages only for availability and current Canadian pricing.

The NIST Electrostatic Force Balance literature establishes the relevant principle: force is derived from measured voltage and capacitance gradient in an electronic null balance, with published micronewton-scale realizations. It is contextual evidence, not automatic evidence that an opposed, signed student-reproducible implementation passes this protocol.

Sources:

- NIST, *The NIST Electrostatic Force Balance Experiment*: https://www.nist.gov/publications/nist-electrostatic-force-balance-experiment
- Pratt et al., *SI realization of small forces using an electrostatic force balance*: https://www.nist.gov/publications/si-realization-small-forces-using-electrostatic-force-balance
- NIST, *Small Mass and Small Force Metrology*: https://www.nist.gov/programs-projects/small-mass-and-small-force-metrology-nist
- JCGM 100:2008 uncertainty framework: https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf

## Frozen extraction table

The audit must fill every row for the exact candidate and revision.

| Field | Required evidence |
| --- | --- |
| geometry and sign | drawings, selected electrode for each sign, receiver and complete support reaction |
| voltage | setpoint/readback range, certificate, calibration date, uncertainty, stability and covariance |
| capacitance gradient | direct measured/calculable `dC/dx`, traceable length/capacitance chain, fit interval and residuals |
| alignment/gap | x/y/z position, tilt, parallelism, Abbe/cosine terms and uncertainty |
| contact/patch potential | measurement or numerical bound for `V_CPD`, spatial/time variation and sign dependence |
| leakage/charging | leakage current/power, dielectric absorption, retained charge, discharge/null protocol and uncertainty |
| environment | temperature, humidity, pressure/airflow, acoustic/vibration and drift data |
| coupling | fields at the force readout, guards/shields/grounds, cable-force null and receiver-absent null |
| reversal | repeated -0.10/0/+0.10 mN electrical selection plus physical fixture reversal |
| uncertainty | signed, covariance-aware standard and expanded budget at both ±0.10 mN |
| rights | license or explicit permission for all construction source; third-party exclusions retained |
| BOM | manufacturer/part number, quantity, live CAD price, stock, shipping/tax estimate and existing-tool offsets |

## Frozen uncertainty terms

For `F = 1/2 V_e^2 G`, where `V_e = V - V_CPD` and `G = dC/dx`, first-order propagation must include

`u_F^2 = (V_e G)^2 u_Ve^2 + (1/2 V_e^2)^2 u_G^2 + 2(V_e G)(1/2 V_e^2) cov(V_e,G) + sum(u_artifact,i^2)`.

The candidate table must separately bound:

- voltage reference/readback and `V_CPD`;
- capacitance-gradient realization, fit and interpolation;
- gap, position, alignment and cross-axis force;
- left/right asymmetry and electrode selection;
- leakage, retained charge, dielectric absorption and patch-potential memory;
- thermal state, humidity/air pressure, airflow, acoustic and vibration response;
- shielding/grounding, readout coupling and cable force;
- zero recovery, creep, temporal drift and repeatability.

Correlations and shared references must be represented with covariance. Unknown covariance is not zero.

## Frozen sequence and controls

Document evidence for ten randomized cycles of bracketed zero, -0.10 mN, zero, +0.10 mN and zero, with equal approach directions and both electrode-order permutations. The audit requires:

1. both electrodes de-energized;
2. receiver absent;
3. same-side repeated actuation;
4. signed electrode selection;
5. physical fixture reversal;
6. matched electrical/thermal dummy;
7. grounded/shielding and cable-routing variants;
8. logged environment, gap and alignment;
9. charge-discharge wait and zero-recovery test;
10. blinded analysis with all failed/saturated cycles retained.

No high-voltage construction or operating procedure is authorized. Any candidate requiring hazardous voltage, vacuum or other specialist controls is rejected for the personal prototype unless a qualified supervisor, compliant enclosure/interlocks and formal safety review are documented.

## Acceptance, falsification and stopping rules

Accept for later procurement consideration only if all of the following are demonstrated for both signs:

- signed ±0.10 mN data in the final geometry;
- `u_c <= 1.5 µN`, `U95(k=2) <= 3.0 µN` and `|E| + U95 <= 5.0 µN`;
- sign asymmetry after physical reversal <= 2.0 µN;
- every required control remains within its frozen allocation;
- complete traceability and covariance-aware uncertainty;
- construction rights and a complete delivered Canadian BOM of CAD $500–$1,000.

Stop the audit without a pass/fail force estimate if the exact revision, either sign, `dC/dx`, `V_CPD`, a mandatory artifact term or covariance is unavailable. Reject the candidate if a required term is numerically above allocation, the reaction path is undefined, signed reversal relies only on voltage polarity, rights prohibit reproduction, the BOM is incomplete/over budget, or the safety gate fails.

## Evidence status

This document freezes an audit method. It contains no candidate outcome, physical calibration, measured force, hardware recommendation or propulsion evidence.

## NEXT ONE TEST

Apply this frozen table once to the NIST electrostatic-force-balance primary literature and exact accessible construction record. Determine whether its published one-sided/concentric architecture can lawfully and quantitatively support an opposed signed realization without inventing a mirror electrode, uncertainty term, right or BOM item. Stop on the first mandatory missing gate; make no purchase.
