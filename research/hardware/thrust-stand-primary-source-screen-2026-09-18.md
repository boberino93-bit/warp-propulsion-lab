# Primary-source thrust-stand screen — 2026-09-18

## Decision

Neither screened publication clears the acquisition gate. No design is selected and no hardware is authorized for purchase.

The DLR/AST balance is the closer metrology match to the project's 0.1–1 mN calibration goal, but the paper does not provide a complete costed bill of materials, redistributable construction files, or an explicit open-hardware license. Its in-situ calibration voice coil also uses the same electromagnetic actuation principle as the measurement actuator; the authors identify calibration by a different physical principle as future work.

The Georgia Tech stand is a useful, well-described impulse instrument, but its demonstrated quantity is impulse from pulsed CubeSat thrusters, not calibrated steady force in the 0.1–1 mN band. Dynamic hammer calibration was future work, and the paper does not publish a complete costed BOM or open construction package.

“Published” is therefore not treated as “student-reproducible,” and absent prices are not estimated.

## Frozen screen criteria

A candidate must document:

1. the momentum boundary and reservoir;
2. demonstrated calibration behavior covering 0.1–1 mN, or a justified traceable path to it;
3. an independent calibration method and uncertainty;
4. null, reversal, thermal, electromagnetic, cable, airflow, and drift controls;
5. enough source material to reproduce the apparatus legally;
6. a complete, live-priced Canadian-dollar BOM within CAD 500–1,000, excluding the already-owned 3D printer, soldering station, and multimeter.

Failure of any item blocks selection and purchase.

## Candidate A — Georgia Tech torsional impulse stand

Primary source: Terry Stevenson and E. Glenn Lightsey, “Design and Operation of a Thrust Test Stand for University Small Satellite Thrusters,” AIAA 2018-2117 (2018), DOI: https://doi.org/10.2514/6.2018-2117. Author manuscript: https://repository.gatech.edu/server/api/core/bitstreams/a09c15f3-24b7-43b5-b069-220c4152d692/content

- **Measured quantity and momentum boundary:** angular impulse of a torsional arm from a pulsed chemical thruster. The expelled propellant and chamber/support structure are external momentum reservoirs.
- **Architecture:** two flex pivots, a Macro Sensors DC-750-125 LVDT, and NI USB-6002 acquisition at 1 kHz in a 61 cm cubed vacuum chamber.
- **Demonstrated performance:** the design reference is 40 mN for 3 ms (120 µN·s). Reported examples include 1.08 ± 0.04 mN·s and 0.21 ± 0.012 mN·s. These are impulse results, not a demonstration of steady 0.1–1 mN force.
- **Calibration and uncertainty:** geometry and inertia are propagated; nozzle position is reported to ±0.4 mm, moment-of-inertia uncertainty at 2–6%, and angular-velocity-change uncertainty at 0.1–1%. A dynamic swinging-hammer calibration is described as future work, so the published apparatus lacks the requested completed independent calibration.
- **Controls and drift:** the long natural period supports pulse analysis, but ringing can remain detectable for 15 minutes and firings were spaced about 60–65 seconds. The paper does not establish the full reversal/thermal/EM/cable/airflow control set required here.
- **Reproducibility, rights, and cost:** the article contains schematics and component names, but no complete BOM, downloadable CAD set, or open-hardware license. The vacuum system and instrumentation are not live-priced in the paper. Budget compliance cannot be verified and is not inferred.

**Screen outcome: reject for this acquisition round.** It is an impulse reference, not a demonstrated steady microforce stand, and the calibration/source/BOM gates remain open.

## Candidate B — AST/DLR low-drift thrust balance

Primary source: Hans-Peter Harmann, Heiko Dartsch, and Ellen Werner, “Low Drift Thrust Balance with High Resolution,” IEPC-2015-257 / ISTS-2015-b-257 (2015): https://electricrocket.org/IEPC/IEPC-2015-257_ISTS-2015-b-257.pdf

- **Measured quantity and momentum boundary:** closed-loop force balance for thrusters. The demonstrated cold-gas test expels propellant; the vacuum facility, flexible supply tube, and stand support close the external momentum boundary.
- **Architecture:** counterbalanced displacement-compensated parallelogram pendulum, capacitive displacement sensor, voice-coil actuator, and a second nominally identical voice coil for in-situ calibration.
- **Demonstrated performance:** stated range 0.1–1000 mN and optimized range 1–250 mN. Ten-mN plateaus were stable substantially better than 0.1 mN. A 27-hour ambient run remained within ±250 µN drift and included a 40 µN, 25 mHz pilot tone. Cold-gas firings measured 42.3–43.1 mN.
- **Calibration and uncertainty:** two voice-coil constants are determined on a microscale. This is useful in-situ calibration, but not independent in physical principle; the paper lists a different-principle calibration as future development.
- **Controls and drift:** a plastic enclosure reduces airflow. Temperature correlates with drift. Flexible feed-line coupling is acknowledged in the cold-gas configuration. The publication does not demonstrate this project's full reversal, cable, EM, sham, and thermal-control matrix.
- **Reproducibility, rights, and cost:** the authors state that AST designed the mechanical parts and key electronics and that standard components were used, but publish neither part-number BOM nor downloadable CAD/source files. No explicit open-hardware license is provided. A complete CAD 500–1,000 BOM therefore cannot be verified.

**Screen outcome: reject for this acquisition round.** Its range is relevant, but the independent-calibration, construction-rights, and complete-cost gates remain open.

## Comparison

| Gate | Georgia Tech | AST/DLR |
|---|---|---|
| Demonstrated 0.1–1 mN steady-force calibration | No; impulse stand | Range includes it, but detailed demonstration concentrates above 1 mN |
| Independent completed calibration | No; dynamic calibration future work | No; second voice coil, different-principle calibration future work |
| Full controls required by this project | Incomplete | Incomplete |
| Redistributable CAD/source package | Not published | Not published |
| Explicit open-hardware license | Not identified | Not identified |
| Complete live-priced BOM | Not published | Not published |
| CAD 500–1,000 verified | No | No |
| Acquisition decision | Stop | Stop |

## Evidence status

This screen compares published apparatus claims only. It reports no local build, calibration, measured thrust, affiliation, or propulsion discovery. The project's 35 µN value remains a synthetic analysis threshold and is not a hardware performance claim.

## NEXT ONE TEST

Resolve the acquisition gate for one candidate with explicit redistributable construction files and licensing: verify a complete Canadian-supplier BOM (including calibration hardware, tax, and shipping) and reject it if the total exceeds CAD 1,000 or if published calibration does not cover 0.1–1 mN. Do not purchase anything during that test.
