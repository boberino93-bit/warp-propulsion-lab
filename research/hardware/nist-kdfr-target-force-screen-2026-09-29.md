# NIST Kibble Dynamic Force Reference screen — 2026-09-29

## Decision

**REJECTED for the present ±0.10 mN calibration-demonstrator track at the first mandatory target-force evidence gate.**

This is a negative public-evidence screen, not a finding that the KDFR concept cannot operate at lower force.

## Candidate and momentum boundary

The NIST Kibble Dynamic Force Reference (KDFR) is an externally supported electrodynamic force source. An AC-driven coil and magnet experience equal and opposite Lorentz forces; the instrument body and mount close the reaction path while a transfer block applies force to an external device under test. It is a calibration source, not a propulsion mechanism.

The published corrected force model is

```text
F = ((U_meas - I Z) I / Δv_mc) - M_m a_m - Ξ(Δx_mb, Δv_mb)
```

so the measurable force depends on simultaneous voltage, current and relative velocity plus coil-impedance, magnet-inertia and flexure corrections.

## Frozen-gate audit

| Mandatory field | Public evidence | Result |
| --- | --- | --- |
| Signed ±0.10 mN data | The 2024 NIST paper describes AC operation but specifies a **10 N target amplitude**, 100 Hz–10 kHz and 1% target uncertainty. It publishes no target-specific ±0.10 mN cycles. | **FAIL — stop** |
| Complete uncertainty at ±0.10 mN | Not evaluated after first failure. The paper identifies impedance, inertia, flexure and accelerometer terms still requiring characterization at its own target. | STOPPED, not waived |
| Public raw records | Not evaluated after first failure. | STOPPED, not waived |
| Reusable construction/source rights | Not evaluated after first failure. The NIST page identifies a patent; that is not an open hardware-source licence. | STOPPED, not waived |
| Canadian BOM and CAD 500–1,000 ceiling | Not evaluated after first failure. | STOPPED, not waived |

The force ratio between the published 10 N design target and 0.0001 N is 100,000:1. No linear extrapolation over that ratio was made.

## Controls and falsification boundary

A future candidate would still need randomized signed `-0.10/0/+0.10 mN` cycles, physical/electrical reversal, bracketed nulls, thermal/EM/cable/airflow/vibration controls, raw integrity records, covariance-aware uncertainty and independent traceability. This screen is falsified if a primary NIST record publishes those target-specific results for the same implementation.

## Sources

- NIST, “Kibble Dynamic Force Reference,” updated 2023-08-28: https://www.nist.gov/noac/technology/mass-force-and-acceleration/kibble-dynamic-force-reference
- J. H. Strait and A. Chijioke, “Progress toward the Kibble Dynamic Force Reference,” CPEM 2024, NIST publication record/PDF: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957415
- NIST, “MEASURING UP: Kibble Dynamic Force Reference,” 2023-07-18: https://www.nist.gov/news-events/news/2023/07/measuring-kibble-dynamic-force-reference

## Evidence status

No hardware was selected, purchased, built or tested. No calibration, force measurement, thrust measurement or propulsion discovery occurred.
