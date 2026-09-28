# NIST HALO/EFB photon-pressure gate audit — 2026-09-28

## Question

Does the published NIST HALO/EFB record clear the frozen documentary gate for a signed ±0.10 mN photon-pressure calibrator suitable for the planned CAD $500–$1,000 personal prototype?

Frozen protocol: `research/hardware/photon-pressure-calibrator-audit-preregistration-2026-09-28.md`.

## Primary records inspected

- NIST HALO project page, updated 2025-04-10: https://www.nist.gov/programs-projects/high-amplification-laser-pressure-optic-halo
- Artusio-Glimpse et al., *Metrologia* 58 (2021) 055010, NIST-hosted manuscript: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=932088
- Artusio-Glimpse et al., “Direct Realization of the Optical Watt from Planck's Constant,” NIST publication record: https://www.nist.gov/publications/direct-realization-optical-watt-plancks-constant
- NIST Photoforce project overview: https://www.nist.gov/programs-projects/photoforce-project

## Frozen gate application

The NIST record demonstrates a real external momentum boundary: a high-power 1070 nm beam reflects repeatedly from a force-sensing mirror supported by a balance, while the remaining beam exits toward a dump. HALO uses 14 reflections at approximately 45 degrees and NIST reports optical-power measurements rather than a self-contained mirror/source claim.

The 2021 record reports 500 W–10 kW input-power measurements and expanded relative uncertainties of 0.46% at 1 kW and 0.26% at 10 kW. The later direct-realization record reports 100 W–5 kW and 0.12% expanded uncertainty at 5 kW, validated against a thermal primary standard. These are relevant photon-momentum metrology results, not a demonstration of the frozen calibrator.

## First mandatory failed gate — signed ±0.10 mN reversal

The inspected implementation directs one input beam through a fixed multi-reflection path onto one sensing mirror. The records do not demonstrate either:

1. two independently characterized opposed beam directions producing both +0.10 mN and -0.10 mN on the same measurement axis, or
2. a complete physical reversal whose two optical paths, transfer ratios and asymmetry are measured under the frozen `<= 2.0 µN` sign-asymmetry limit.

Laser on/off square-wave injections and changing the number of reflections are not signed force reversal. A positive optical-power measurement therefore cannot be relabeled as a bidirectional ±0.10 mN calibration.

Per the preregistered stopping rule, the audit stops here. Rights, complete construction source, Canadian delivered BOM, and qualified personal-prototype safety gates were not promoted to pass/fail findings after the first mandatory failure.

## Safety and scope

The NIST apparatus is a laboratory kilowatt-class laser metrology system. The cited architecture uses up to 10 kW input and a 1.2 m3 optical structure inside a 2.3 m3 air shield. It is outside an unsupervised personal prototype. No construction or operating instructions, laser selection, extrapolation to 15–30 kW, supplier choice, purchase, build, force measurement, or propulsion claim is made.

## Evidence status

**Rejected for the current signed calibrator gate.** This is a documentary null result. It does not dispute NIST's laser-power metrology result; it only finds that the published record does not establish the project's different bidirectional ±0.10 mN, rights, BOM and personal-safety requirements.

## NEXT ONE TEST

Preregister a bounded paper-only screen of low-risk mechanical or electromagnetic reference-force methods that can inherently reverse sign at ±0.10 mN, using the unchanged uncertainty, rights, Canadian BOM and personal-prototype safety gates. Do not select or purchase hardware.
