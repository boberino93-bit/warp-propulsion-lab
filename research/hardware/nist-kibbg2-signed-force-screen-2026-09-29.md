# NIST KIBB-g2.0 signed-force reference screen (2026-09-29)

## Scope

This paper-only screen applies the frozen ±0.10 mN acquisition gate to one candidate: NIST's second-generation tabletop Kibble balance, KIBB-g2.0. No purchase, contact, build, calibration, force measurement, affiliation, or propulsion claim is made.

Official sources:
- NIST technology page, created 2023-06-12 and updated 2025-07-24: https://www.nist.gov/noac/technology/mass-force-and-acceleration/tabletop-kibble-balance-gram-level-mass-realization
- NIST technical feature, released 2023-03-28 and updated 2025-02-03: https://www.nist.gov/news-events/news/2023/03/mass-revolution-kibble-balances-all

## Physical boundary, scaling and prediction

KIBB-g2.0 is a laboratory reaction-force mass-metrology instrument. The mass, flexure, electromagnetic coils, magnets and frame exchange momentum through the laboratory support and Earth. It is not a propulsion device.

At standard gravity, the target force corresponds to:

`m = F/g0 = 0.000100000 N / 9.80665 m/s² = 10.197162130 mg`.

NIST describes force mode as an upward electromagnetic force proportional to coil current counteracting the downward gravitational force on a mass; velocity mode characterizes the electromechanical factor. The independently measurable observables are mass load, coil current, induced voltage and displacement/velocity.

## Frozen gate

| Gate | Public evidence | Decision |
| --- | --- | --- |
| Range and traceability | NIST reports direct realization from 1 mg to 20 g, which includes 10.197 mg, with traceability to electrical standards and the Planck constant. | Pass for range/boundary only |
| Demonstrated randomized signed ±0.10 mN cycles | The public record describes an upward electromagnetic force balancing downward gravity. It does not publish randomized `-0.10/0/+0.10 mN` applied-force cycles, complete apparatus reversal, or an equivalent signed protocol at the target. | **Fail — stop** |
| Complete uncertainty at signed ±0.10 mN | Not evaluated after the first mandatory failure. NIST's “tens of micrograms”/ASTM Class 3 description is not a signed-target component budget. | Not reached |
| Raw signed calibration package and hashes | Not evaluated after stop. | Not reached |
| Explicit reusable construction/source rights | Not evaluated after stop. NIST lists a patent and commercialization agreement; neither is an open-source construction grant. | Not reached |
| Complete Canadian BOM within CAD 500–1,000 | Not evaluated after stop. | Not reached |

## Required controls not established by this record

The acquisition gate requires signed reversal plus null, sham, thermal, electromagnetic, cable, airflow, vibration, alignment, drift, hysteresis and creep controls; raw cycle order and hashes; covariance-aware uncertainty; and independently checkable falsification. Those requirements cannot be inferred from a one-direction mass-realization description.

## Evidence status

KIBB-g2.0 is rejected for the current demonstrator at the first mandatory signed-cycle gate. This is a retained negative public-evidence screen, not criticism of its stated mass-metrology performance. No hardware was selected or purchased and no thrust or propulsion evidence exists.

## Next one test

Screen NIST's published Kibble Dynamic Force Reference implementation for randomized signed ±0.10 mN data, a complete target-specific uncertainty budget, public raw records and explicit reusable construction/source rights; stop at the first mandatory failure and make no purchase.
