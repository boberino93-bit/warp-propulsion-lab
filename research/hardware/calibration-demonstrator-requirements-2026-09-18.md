# Preregistration — procurement-neutral 0.1–1 mN calibration demonstrator

Status: **FROZEN REQUIREMENTS when merged**. This is an acquisition gate, not a hardware selection, build, calibration result or thrust measurement.

## Bounded question

What must a low-risk calibration demonstrator prove before this project may select a sensor or thrust-stand design for a CAD $500–$1,000 personal prototype?

The demonstrator must show traceable, signed force calibration across 0.1–1 mN with uncertainty small enough to distinguish the lowest required force, while bounding reversal, drift, thermal, electromagnetic, cable and airflow artifacts. The historic 35 µN synthetic threshold is excluded: it is not measured hardware capability.

## Measurement boundary and candidate reference

The device under test (DUT) includes the sensing element, structure, fixture, wiring, acquisition electronics, filtering and analysis used to report force. The independent reference force must not be inferred from the DUT output.

A permissible reference is either:

1. a traceably calibrated mass acted on by documented local gravitational acceleration, with `F_ref = m × g_local`, fixture geometry and buoyancy included in uncertainty; or
2. another force generator or transfer standard whose calibration certificate covers 0.1–1 mN and provides an unbroken SI traceability statement and uncertainty within this gate.

No specific sensor, supplier or force-generation method is selected here. A reference outside its certified range, an uncalibrated hobby weight, an actuator commanded without independent force verification, or a second channel sharing the DUT's calibration cannot satisfy independence.

For scale only, using standard gravity 9.80665 m/s², 0.1 mN corresponds to 10.1972 mg and 1 mN to 101.972 mg. Actual force must use documented local `g`, not silently substitute standard gravity.

## Frozen calibration schedule

After a preregistered warm-up and stabilization interval:

- signed setpoints: 0, ±0.10, ±0.25, ±0.50, ±0.75 and ±1.00 mN;
- ten complete cycles;
- randomized nonzero order within each cycle using a recorded seed;
- a zero before and after every nonzero point;
- identical dwell and sampling windows for positive, negative and zero loads;
- all raw time series, environmental channels, reference certificates, configuration, code and exclusions retained;
- no adjustment, filtering or rejection rule changed after the first calibration result is viewed.

Positive/negative force must be produced by a genuine physical reversal of the reference load path or complete DUT orientation under the same fixture geometry. Multiplying one direction by -1 in software is not reversal evidence.

## Uncertainty model and numerical acceptance gate

Follow JCGM GUM terminology. At each signed setpoint, report mean indication, reference value, error `E = F_indicated − F_ref`, standard uncertainty components, combined standard uncertainty `u_c`, coverage factor and expanded uncertainty `U95` (normally `k = 2`, with any different coverage method justified).

The budget must include, where applicable:

- reference mass/force uncertainty and traceability;
- local-gravity uncertainty;
- fixture angle, alignment, lever ratio and load-position uncertainty;
- air buoyancy for mass-derived force;
- DUT resolution/quantization;
- repeatability and within-cycle noise;
- zero interpolation and time drift;
- nonlinearity and fit uncertainty;
- signed hysteresis/reversal asymmetry;
- temperature sensitivity;
- electromagnetic pickup or actuator leakage;
- cable restoring force and routing variation;
- airflow/acoustic/vibration response;
- sampling, timing and numerical processing.

Frozen tolerance:

`T(F) = max(0.020 mN, 0.10 × |F|)`

A signed point passes only if both:

`U95 ≤ T(F)`

and the guard-banded error satisfies

`|E| + U95 ≤ T(F)`

Therefore the 0.10 mN point must have expanded uncertainty no greater than 0.020 mN and enough remaining guard band for observed bias. This project-chosen research gate is not represented as an international standard or a manufacturer's specification.

Additional whole-run gates:

- indicated resolution no coarser than 0.010 mN;
- peak-to-peak interpolated zero drift no greater than 0.020 mN in any complete cycle;
- no missing or replaced cycle;
- all positive and negative points pass independently;
- calibration residuals show no preregistered trend test failure versus order, temperature or time;
- all ten cycles and all controls complete within the fixed run; no optional stopping.

## Required control matrix

| Control | Frozen requirement | Failure condition |
| --- | --- | --- |
| Null/sham | Run the complete acquisition sequence with no reference force while preserving timing and any actuator commands | A sham produces a guard-banded nonzero response above 0.020 mN |
| Signed reversal | Independently apply every positive and negative setpoint | Either sign fails the point gate or reversal asymmetry is not included in uncertainty |
| Thermal | Log sensor/structure temperature; repeat a preregistered heat-only sham representative of candidate power without thrust production | Response is confounded with temperature or thermal contribution cannot be bounded |
| Electromagnetic | Repeat with the candidate's electrical command/load present but mechanically unable to apply reference force; document grounding and shielding state | EM-only response exceeds 0.020 mN or differs unpredictably with reversal |
| Cable | Freeze routing, photograph it, then perform a preregistered bounded routing perturbation | Cable effect exceeds 0.020 mN or is omitted from uncertainty |
| Airflow/acoustic | Use an enclosure or still-air control and log enclosure state; compare fan/ventilation off/on only if safe | Airflow/acoustic response exceeds 0.020 mN or enclosure state is unrecorded |
| Vibration | Log or otherwise bound support vibration during calibration and sham blocks | A vibration-correlated response survives the guard band |
| Analysis blind | Freeze code/config before unblinding signed labels where practical; retain hashes | Post-outcome processing changes are undisclosed |

A future propulsion article must still specify its own momentum reservoir, power, thrust scaling, nulls and independent prediction. Passing this demonstrator would validate only a measurement method.

## Stop and falsification rules

Stop without selecting hardware if any traceability document is missing, a reference is used outside scope, safety review is absent, projected complete BOM exceeds CAD $1,000, any required control cannot be performed, or the run exceeds a preregistered safe resource limit.

The acquisition gate is falsified as satisfied if any signed point or whole-run gate fails, any record is missing/duplicated, configuration differs between paired controls, or uncertainty is reduced by silently omitting a component. Failed and null outputs must be retained. There is no purchase authorization in this document.

## Evidence status and sources

This matrix is an original project requirement informed by metrology guidance, not a claim that a physical device has passed it.

- BIPM/JCGM, [Guide to the Expression of Uncertainty in Measurement and JCGM publications](https://www.bipm.org/en/committees/jc/jcgm), including the 2026 nonlinearity amendment where relevant.
- NIST, [SI base and derived units](https://www.nist.gov/pml/owm/metric-si/si-units), for SI traceability and the newton as a derived unit.
- NIST, [Uncertainty Machine](https://uncertainty.nist.gov/), as a public implementation reference for measurement models and uncertainty propagation.
- Georgia Tech, [torsional impulse stand, AIAA 2018-2117](https://doi.org/10.2514/6.2018-2117), previously screened as a published stand design.
- AST/DLR, [low-drift thrust balance, IEPC-2015-257](https://electricrocket.org/IEPC/IEPC-2015-257_ISTS-2015-b-257.pdf), previously screened as a published balance design.

Third-party publications remain under their original rights and are linked, not copied.

## NEXT ONE TEST

Using this frozen matrix only, produce a procurement-neutral reference-force feasibility calculation for the 0.10 mN point: quantify mass, local-gravity, alignment and buoyancy contributions and determine whether an independently certifiable reference can meet the 0.020 mN expanded-uncertainty ceiling. Do not select or buy a sensor.
