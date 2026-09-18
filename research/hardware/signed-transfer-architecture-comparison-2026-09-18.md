# Signed-transfer architecture uncertainty comparison — 2026-09-18

## Decision

Neither complete-DUT inversion nor a symmetric filament/flexure transfer is verified for construction. Both fail because their architecture-specific uncertainty terms lack measured evidence. No component, supplier or design is selected and no purchase is authorized.

## Boundary and prediction

The calibration boundary includes the reference mass, Earth's gravitational reaction, transfer fixture, stand, DUT mounting, cables and supporting frame. The external Earth/frame reservoir closes momentum accounting. This is calibration-force transfer, not propellantless thrust.

For a signed reference of magnitude 0.1 mN, a valid architecture must produce opposite indicated signs when the reference reverses, return to zero after unloading, and fit:

`U95 = 2 sqrt(sum(u_i^2)) <= 0.005 mN`.

## Frozen allocation

These are maximum standard-uncertainty allocations, not measured performance.

| Component | Standard allocation (mN) | Required evidence |
| --- | ---: | --- |
| mass/gravity/buoyancy reference | 0.000101166 | individual certificate and site corrections |
| alignment | 0.000100000 | surveyed load axis in both signs |
| reversal repeatability | 0.000900000 | randomized repeated sign cycles |
| zero return | 0.000900000 | bracketed unloaded readings |
| hysteresis | 0.000900000 | increasing/decreasing signed sequence |
| architecture-specific transfer | 0.001800000 | measured mechanism-specific bound |

RSS gives `u_c = 0.002385421 mN` and `U95 = 0.004770843 mN`, leaving only `0.000229157 mN` below the ceiling. Allocations are not proof that a mechanism meets them.

## A: complete-DUT inversion

The sensor/DUT assembly rotates 180 degrees while the mass reference remains gravitational. This avoids an intermediate transfer ratio but changes DUT, cable and thermal-field orientation with sign. Required evidence includes kinematic reseating, lever-arm/centre-of-mass stability, cable-force characterization, gravity-vector and thermal nulls, and randomized reversal/zero-return data. No measured bound exists for their combined contribution, so the 0.0018 mN architecture term is unverified.

## B: symmetric filament/flexure transfer

The DUT remains fixed while a mirrored filament/flexure path applies opposing forces; the support frame receives the reaction. This preserves DUT orientation but requires signed transfer-ratio calibration plus measured flexure/filament stiffness, creep, friction/stiction, off-axis coupling and hysteresis. No measured combined bound exists, so its 0.0018 mN architecture term is unverified.

## Controls and falsification

Both concepts require ten randomized signed cycles, bracketed zeros, sham and fixture-only reversal, cable-routing nulls, thermal logging, EM-disabled runs, airflow shielding and vibration monitoring. Reject if a required term is missing, `U95 > 0.005 mN`, or reversal changes more than the reference direction.

## Evidence status

This freezes requirements and arithmetic only. No fixture was built and no calibration or thrust measurement ran. Executable arithmetic is in `simulations/signed_transfer_budget.py`.

## Sources

- JCGM 100:2008: https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf
- BIPM SI Brochure: https://www.bipm.org/en/publications/si-brochure
- NIST Handbook 44: https://www.nist.gov/pml/owm/nist-handbook-44-current-edition

## NEXT ONE TEST

Audit one published symmetric flexure/filament low-force transfer with repeated signed calibration data. Map transfer ratio, hysteresis, creep, alignment and friction/stiction into this table; reject any missing term or `U95 > 0.005 mN`. Make no purchase.
