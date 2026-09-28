# Preregistration — 0.10 mN photon-pressure calibration audit

**Frozen:** 2026-09-28 12:35 UTC  
**Status:** paper-only documentary protocol; no laser selected, purchased, operated or tested  
**Target:** externally applied signed calibration force of ±0.10 mN

## One bounded question

Can one published photon-pressure implementation provide independently traceable, reversible ±0.10 mN force at a device-under-test interface with `U95 <= 3.0 µN` and `|E| + U95 <= 5.0 µN`, while satisfying controls, lawful construction rights, a delivered Canadian BOM of CAD $500–$1,000 and the personal-prototype safety gate?

The audit must stop at the first missing mandatory gate. Published power-meter capability does not automatically establish a safe, reproducible force calibrator.

## Boundary, momentum reservoir and ideal scaling

For normally incident absorbed optical power,

`F_abs = P_abs / c`.

For ideal specular reflection from an **externally supported** mirror at normal incidence,

`F_refl = 2 P_inc / c`.

More generally, the axial force model must include measured absorption `A`, reflectance `R`, transmittance `T`, incidence angle `theta`, polarization and all escaped beams. The audit may not substitute the ideal factor of two for a measured optical momentum budget.

At `F = 0.10 mN = 1.0e-4 N`, with exact `c = 299792458 m/s`, the ideal lower-bound powers are:

- complete absorption: `P = Fc = 29,979.2458 W`;
- ideal external reflection: `P = Fc/2 = 14,989.6229 W`.

These are scaling constraints, not operating setpoints or build instructions.

The beam source, receiver, turning/absorbing optics and their mounts define the external momentum reservoir. A source and mirror wholly inside one free, self-contained system exchange momentum internally and produce zero net external force on that complete system. A valid calibration applies the reaction through an external support and measures the force at the specified receiver interface.

## Primary context

NIST's Photoforce project states that reflected photon momentum produces force proportional to optical power. NIST has demonstrated photon-momentum radiometry above 1 kW and an electrostatic-force-balance/HALO implementation at 0.1–5 kW, with a reported lowest expanded power uncertainty of 0.12% at 5 kW. These records establish the principle and relevant metrology; they do not establish this audit's ±0.10 mN, safety, rights or cost gates.

Sources:

- NIST Photoforce Project: https://www.nist.gov/programs-projects/photoforce-project
- Williams et al., *Axial force radiometer for primary standard laser power measurements using photon momentum* (2021): https://www.nist.gov/publications/axial-force-radiometer-primary-standard-laser-power-measurements-using-photon-momentum
- Simonds et al., *High-Power Radiation-Pressure-based Laser Metrology using an Electrostatic Force Balance* (2023): https://www.nist.gov/publications/high-power-radiation-pressure-based-laser-metrology-using-electrostatic-force-balance
- NIST HALO project: https://www.nist.gov/programs-projects/high-amplification-laser-pressure-optic-halo
- JCGM 100:2008: https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf

## Frozen evidence table

| Field | Mandatory exact evidence |
| --- | --- |
| system boundary | source, receiver, every outgoing beam/absorber and complete external support reaction |
| optical power | traceable incident/absorbed/reflected/transmitted power at the receiver, calibration date and uncertainty |
| momentum coefficient | measured `A,R,T,theta`, polarization, scatter and wavelength dependence; no assumed ideal mirror |
| sign | two externally supported opposed beam directions or physical reversal with independently characterized paths |
| receiver | exact coating, aperture, thermal state, deformation and force-transfer interface |
| losses | clipping, scatter, back-reflection, window/air absorption and escaped-beam capture |
| alignment | spot position, incidence angle, pointing drift, torque/cross-axis coupling and uncertainty |
| thermal | absorbed-power heating, radiometric/convection forces, expansion, drift and matched thermal dummy |
| environment | pressure, temperature, humidity, airflow, acoustic and vibration records |
| electromagnetic | source/readout coupling, grounding/shielding and source-on beam-blocked null |
| reversal/nulls | randomized -0.10/0/+0.10 mN, source-off, beam-blocked, receiver-absent and physical reversal |
| uncertainty | signed covariance-aware budget at both signs |
| rights | license or explicit permission for construction sources, preserving third-party exclusions |
| BOM | manufacturer/part number, quantity, live CAD price, stock, shipping/tax and existing-tool offsets |
| safety | qualified laser-safety review, controlled area, enclosure/interlocks, beam dump and applicable compliance evidence |

## Frozen uncertainty model

For an idealized single reflected beam, `F = 2 P K / c`, where `K` is the measured momentum-transfer coefficient incorporating angle and optical properties. First-order propagation must include:

`u_F^2 = (2K/c)^2 u_P^2 + (2P/c)^2 u_K^2 + 2(2K/c)(2P/c) cov(P,K) + sum(u_artifact,i^2)`.

The artifact sum must separately bound alignment/pointing, beam clipping/scatter, thermal/radiometric effects, receiver deformation, support transfer, cross-axis torque, environmental drift, readout coupling, zero recovery and reversal asymmetry. Unknown covariance is not zero.

Acceptance at both signs requires `u_c <= 1.5 µN`, `U95(k=2) <= 3.0 µN`, `|E| + U95 <= 5.0 µN`, sign asymmetry after physical reversal `<= 2.0 µN`, and every null/control within its allocation.

## Frozen sequence

Document evidence for ten randomized cycles of bracketed zero, negative, zero, positive and zero, balanced across direction order and approach. Require:

1. source off;
2. source on with beam blocked before the receiver;
3. receiver absent with terminal beam dump unchanged;
4. matched electrical and thermal dummy;
5. opposed-direction selection;
6. complete fixture reversal;
7. power/beam-position logs at the receiver;
8. airflow, temperature and vibration logs;
9. cable/ground/shield variants;
10. blinded analysis retaining failed, clipped and saturated cycles.

## Safety and stopping rules

This document gives no construction or operating instructions. Tens-of-kilowatts-class optical power is hazardous and outside an unsupervised personal prototype. Reject any candidate that requires exposed high-power beams, lacks a qualified laser-safety program or cannot demonstrate compliant enclosure, interlocks and beam termination.

Stop without a force estimate if the exact optical momentum coefficient, external reaction boundary, either sign, traceable power at the receiver, mandatory artifact term or covariance is unavailable. Reject on an incomplete/over-budget BOM, unavailable reproduction rights, guard-band failure or safety failure.

## Evidence status

This preregisters a documentary audit and ideal scaling only. It is not a design selection, procurement authorization, laser procedure, physical calibration, thrust measurement or propulsion result.

## NEXT ONE TEST

Apply this table once to NIST's published HALO/EFB photon-momentum implementation. Stop at the first missing mandatory ±0.10 mN, signed-reversal, rights, BOM or personal-prototype safety gate; do not extrapolate its 0.1–5 kW measurements to 15–30 kW and make no purchase.
