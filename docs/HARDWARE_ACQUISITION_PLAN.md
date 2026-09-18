# Hardware acquisition plan — experimental propulsion track

Status: planning only; no hardware purchased, built, calibrated or tested. Robert plans an initial personal prototype documented for university-student reproduction. No university affiliation is claimed.

## Decision and constraints

- Adapt and reproduce an existing published, independently documented thrust-stand design rather than inventing a new instrument from scratch. Survey university/NASA/JPL publications and open hardware projects; verify original design files, measured noise/drift, calibration, rights and replicability. An upstream design keeps its own license and is **not** automatically relicensed under this project's CERN-OHL-S-2.0 license. See [LICENSE.md](../LICENSE.md).
- Initial budget: CAD $500–$1,000 including parts, consumables, shipping/taxes where possible. Existing equipment: 3D printer, soldering station, multimeter. Personal prototype first; document for subsequent student reproduction.
- First target: physically calibrate approximately 0.1–1 mN, magnitude and sign, with documented uncertainty. Earlier 35 µN detection threshold is synthetic, not measured performance or procurement guarantee.
- No purchasing before comparing published designs and reviewing a complete costed BOM and realistic sensitivity/error budget.

## Acquisition gates

1. Find at least two credible published designs; record primary references, upstream license and permitted modifications, CAD/electronics/software availability, actual measured performance, constraints and total build cost.
2. Produce a BOM with manufacturer/part number, quantity, CAD unit and extended cost, supplier, stock, tax/shipping, substitutions and existing-tool offsets. Verify live prices before purchase.
3. Specify rigid base/enclosure, suitable sensor or torsion balance, independently characterized mechanical calibration, environmental monitoring, logging and reversible fixture. Verify geometry, load path, sign and resolution.
4. Complete safety review: no improvised pressure vessels, high voltage, high-power lasers or vacuum equipment. Use low-risk established reaction-thrust examples only after calibration and suitable supervision.
5. Freeze acceptance criteria before tests: 0.1–1 mN reference forces, correct sign, repeatability, combined-uncertainty agreement, sham/reversal/null controls. Measure power and expelled mass/velocity as applicable and close full-system momentum boundary.
6. Release original project-owned CAD, BOM, build guide, schematics, calibration, uncertainty, raw data, analysis and student exercises with the category-specific licenses in LICENSE.md. Preserve third-party terms, credits and negative results; no claimed endorsement.

## Primary-source screen result — 2026-09-18

The [first two-candidate screen](../research/hardware/thrust-stand-primary-source-screen-2026-09-18.md) found that neither the Georgia Tech pulsed torsional stand nor the AST/DLR low-drift balance currently clears every acquisition gate. The missing items include a completed independent calibration in the target band, complete redistributable construction source with explicit rights, and a live-priced full BOM. No design was selected and no purchase was authorized.

## Immediate next hardware task

Resolve the construction-rights, calibration, and complete-cost gates for one openly reproducible published candidate. Price all required components from Canadian suppliers, including calibration hardware, tax, and shipping; reject above CAD $1,000 or without demonstrated 0.1–1 mN calibration. Do not purchase hardware during this test.
