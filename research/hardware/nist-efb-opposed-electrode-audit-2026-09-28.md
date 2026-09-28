# NIST electrostatic-force-balance opposed-electrode audit — 2026-09-28

**Protocol:** [opposed-electrode preregistration](opposed-electrode-electrostatic-audit-preregistration-2026-09-28.md)  
**Candidate:** NIST Electrostatic Force Balance (EFB), primary 2002 apparatus record plus NIST follow-on records  
**Outcome:** STOP at first mandatory missing gate; no signed force estimate, selection or purchase

## Exact evidence considered

1. Kramar, Newell and Pratt, *The NIST Electrostatic Force Balance Experiment* (2002), NIST publication record: https://www.nist.gov/publications/nist-electrostatic-force-balance-experiment
2. Seugling et al., *Realizing and Disseminating the SI Micronewton With the Next Generation NIST Electrostatic Force Balance* (2004), NIST publication record: https://www.nist.gov/publications/realizing-and-disseminating-si-micronewton-next-generation-nist-electrostatic-force
3. NIST, *Small Mass and Small Force Metrology at NIST*: https://www.nist.gov/programs-projects/small-mass-and-small-force-metrology-nist

The 2002 primary record states that the active electrodes are concentric cylinders: an outer reference electrode and an inner electrode suspended and guided by a rectilinear flexure. It reports a near-linear capacitance gradient of 1 pF/mm at 5 mm working overlap. The 2004 NIST record states that the EFB compares deadweight and mechanical-probe forces with force derived from capacitance gradient and voltage, and reports initial comparisons at 20 µN and 200 µN in a 1000 µPa vacuum. The current NIST program page documents use of the EFB over 50 µg to 20 mg artifacts.

These records support the electrostatic force-realization principle and relevant scale. They do not automatically document the preregistered signed opposed-electrode architecture.

## Frozen table application

| Frozen field | Accessible exact evidence | Status |
| --- | --- | --- |
| external reaction boundary | Outer reference electrode and flexure-supported inner electrode are laboratory-supported parts; equal-and-opposite reaction closes through the apparatus support | contextual pass |
| force principle | Force derived from voltage and measured capacitance gradient in an electronic null balance | contextual pass |
| candidate identity | NIST EFB; 2002 primary apparatus record | pass |
| geometry and sign | One concentric-cylinder actuator is described. No separately characterized electrodes on opposite sides of the receiver are documented for -0.10 mN and +0.10 mN selection | **mandatory gate missing — STOP** |

## Stopping-rule result

The audit stops at the first mandatory missing gate: **published geometry and sign evidence**.

The frozen protocol forbids treating voltage reversal as force reversal because the constant-voltage electrostatic force remains attractive. The accessible NIST primary record documents one concentric actuator, not a left/right or otherwise opposed pair with both reaction paths and sign conventions characterized. Creating a mirror copy, assigning it the same capacitance gradient or uncertainty, and assuming independent construction rights would be new design work rather than evidence extraction.

Accordingly:

- no signed ±0.10 mN estimate was calculated;
- no left/right asymmetry, contact-potential, covariance or reversal term was set to zero;
- downstream uncertainty, construction-rights, BOM, Canadian pricing and safety gates were not adjudicated;
- no hardware was selected, purchased, built, energized or tested.

## Evidence status

This is a documentary rejection under a preregistered gate. It does not invalidate the NIST EFB as a national-metrology instrument. It establishes only that the accessible published one-actuator record cannot, without invented geometry, demonstrate the requested student-reproducible opposed signed calibrator.

It is not propulsion evidence, a thrust measurement or a physical calibration.

## NEXT ONE TEST

Preregister a paper-only photon-pressure calibration audit at 0.10 mN, including the external momentum reservoir, required optical power, absorber versus externally supported reflector scaling, traceable power measurement, beam-loss/thermal/alignment controls, uncertainty, safety, construction rights and CAD $500–$1,000 BOM gates. Do not select or purchase a laser.
