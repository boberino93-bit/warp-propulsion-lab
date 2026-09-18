# Published spring-leaf transfer audit — Frieler & Groll (2018)

Date: 2026-09-18 UTC  
Decision: **REJECT for the frozen 0.10 mN signed-transfer demonstrator**

## Candidate and provenance

T. Frieler and R. Groll, “A torsional sub-milli-Newton thrust balance based on a spring leaf strain gauge sensor,” *Review of Scientific Instruments* 89, 075101 (2018), DOI [10.1063/1.4996419](https://doi.org/10.1063/1.4996419). The publisher record and PubMed abstract were checked on 2026-09-18.

This is a published torsional balance with a strain-gauged spring-leaf flexure, passive eddy-current damping, and an automated pulley/known-mass calibration mechanism. The record states that single and multiple atmospheric and in-situ calibration runs are supported and describes calibration as linear and repeatable. It reports a 225 mN range, estimated resolution within 15 µN, and example measurements from 29 µN to 37.04 mN.

## Frozen-gate mapping

The prior comparison reserves no more than `U95 = 0.005 mN` (5 µN) for the complete reference-plus-transfer path and requires repeated signed calibration with bounded ratio, friction/stiction, creep, and hysteresis.

| Frozen requirement | Published evidence found | Gate |
|---|---|---|
| Relevant symmetric/flexural low-force architecture | Torsional beam with spring-leaf flexure and pulley/weight transfer | relevant |
| Repeated calibrations | Multiple runs and automatic averaging are stated | partial |
| Signed positive/negative cycles with bracketed zeros | Not reported in the accessible record | fail |
| Independent certificate/value/uncertainty for each calibration mass | Not reported | fail |
| Transfer ratio and pulley/filament geometry uncertainty | No complete uncertainty allocation found | fail |
| Friction/stiction and loading-direction hysteresis | “Linearity and repeatability” are qualitative in the accessible record; no signed component bound usable here | fail |
| Flexure creep/anelastic return and temperature coefficient at 0.10 mN | No bound usable in the frozen table | fail |
| `U95 <= 0.005 mN` for reference plus transfer | Not demonstrated | fail |
| Lowest-point `U95 <= 0.020 mN` | The reported 15 µN value is an estimated resolution, not an expanded uncertainty. Even if treated optimistically as a single uncertainty scale, it consumes 75% of the 20 µN ceiling before traceability, pulley ratio, alignment, buoyancy, hysteresis, creep, drift, and repeatability are added. | not established |

## Boundary and falsification

The balance measures reaction thrust transferred through the facility-supported torsional structure; it does not constitute propellantless propulsion. The candidate would clear this specific gate only with raw repeated signed ±0.10 mN cycles, bracketed zeros, traceable individual calibration values, and a complete uncertainty budget showing the reference-plus-transfer `U95 <= 5 µN`. Those items were not demonstrated in the accessible source record.

No numerical value was imputed for an unreported term, and the qualitative “excellent” calibration description was not converted into uncertainty. No hardware was selected, purchased, built, calibrated, or tested.

## Result

The paper is strong evidence that a spring-leaf balance with automated mass calibration can operate in the sub-millinewton regime. It is not sufficient evidence that its pulley/flexure transfer satisfies this project’s much narrower signed 0.10 mN and 5 µN allocation. Candidate rejected for acquisition under the frozen gate.
