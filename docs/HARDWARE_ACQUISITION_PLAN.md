# Hardware acquisition plan — experimental propulsion track

Status: planning only; no hardware purchased, built, calibrated, or tested. This document records Robert's decision to build an initial personal prototype and make the resulting design suitable for university students. It does not supersede the research sessions or claim an experimentally demonstrated sensitivity.

## Decision and constraints

- Adapt and reproduce an existing **published, independently documented thrust-stand design** rather than inventing a new instrument from scratch. Survey original university/NASA/JPL papers and open hardware projects; verify actual design files, sensor specifications, calibration method, measured noise/drift, licensing, safety and replicability before selecting one. Do not claim a particular design meets the requirements without verification.
- Initial budget: **CAD $500–$1,000**, including necessary acquisition, consumables, taxes/shipping where possible. Existing equipment: **3D printer, soldering station, multimeter**. First unit: Robert's personal prototype; design/document for subsequent university-student reproduction.
- First target: physically calibrate forces over approximately **0.1–1 mN**, recovering magnitude and sign with a documented uncertainty budget. The earlier **35 µN minimum-detectable-thrust figure is synthetic**, not measured instrument performance or a procurement guarantee.
- Do not buy hardware until a published design has been compared with alternatives and a complete costed BOM and realistic sensitivity/error budget have been reviewed.

## Acquisition gates

1. Locate at least two credible published designs; record primary references, licensing, available CAD/electronics/software, demonstrated measured performance, operating constraints and total build cost. Select by evidence, safety and affordability, not novelty.
2. Produce a bill of materials with manufacturer/part number, quantity, CAD unit/extended price, supplier, availability, shipping/tax allowance, substitutions and existing-tool offsets. Verify current pricing and availability at purchasing time; avoid invented quotes.
3. Specify a rigid base/enclosure, suitable force transducer or torsion-balance architecture, independently characterized mechanical calibration, temperature and environmental monitoring, data logging and reversible fixture. Confirm mounting geometry, force direction, sensor loading and readout resolution before purchasing.
4. Perform a written safety review: no improvised pressure vessels, high voltage, high-power lasers or vacuum equipment. Use low-risk established reaction-thrust demonstrations only after apparatus validation and appropriate supervision.
5. Freeze acceptance criteria before tests: reference force 0.1–1 mN, correct polarity, repeatability, combined-uncertainty agreement and sham/reversal/null controls. Independently measure electrical input and expelled mass/velocity where applicable; close the full-system momentum boundary.
6. Publish build instructions, CAD, BOM, calibration protocol, uncertainty calculations, raw data, analysis code, known failures and student exercises under explicitly chosen appropriate licenses and attribution. Obtain consent before publicly attributing contributors or claiming university involvement.

## Immediate next hardware task

Research and compare existing published university/NASA/JPL thrust stands and open-source student builds against the budget and measurement requirements. Recommend one reproducible reference design with a verified parts list and a reasoned fallback. **No purchase authorization or design selection is implied by this planning document.**

Research-track continuity: this acquisition plan is separate from the latest session's NEXT ONE TEST (non-Gaussian artifact stress testing). Do not silently replace that test or modify cumulative research/error logs without reconciling the stacked PR lineage.
