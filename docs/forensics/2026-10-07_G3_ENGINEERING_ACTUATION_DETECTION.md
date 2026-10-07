# Forensic Analysis G3 — Engineering, Actuation, and Detection

**Date:** 2026-10-07  
**Project:** Warp Propulsion Lab  
**Gate:** G3 — realizable actuator and measurable physical effect  
**Status:** `UNKNOWN / NOT DEMONSTRATED`  
**Evidence class:** no project evidence currently supports a functioning warp actuator or measured engineered warp curvature.

## Question

Assuming a candidate clears G1 and has a defensible G2 source model, can humans actually create, modulate, control and independently detect the required physical configuration?

This gate is where a spacetime proposal becomes an engineering and metrology problem.

## Required separation: propulsion signal versus curvature signal

A measured force is not automatically evidence of spacetime engineering.

The project must distinguish at least four possible observables:

1. **ordinary thrust / reaction force** — momentum transferred to matter, radiation, fields or environment;
2. **near-field electromagnetic/mechanical coupling** — apparent force caused by cables, magnetic gradients, electrostatics, vibration, thermal expansion, airflow or support deformation;
3. **gravitational/metric effect** — an invariantly interpretable change in clock rate, phase, geodesic deviation, light propagation or acceleration compatible with the predicted metric/source;
4. **analysis artifact** — filtering, drift subtraction, timing leakage, cherry-picking, sensor saturation or statistical bias.

A candidate "warp actuator" must predict which channel should respond and how the other channels are controlled.

## Why the existing force-metrology program matters

The project's frozen signed-force program is directly useful as a **metrology qualification track**. It already demands reversible signed references, uncertainty budgets, nulls, environmental controls and raw-data provenance.

That program should be preserved, but its interpretation must be bounded:

- passing a `0.1–1 mN` force calibration gate validates an instrument, not a warp theory;
- observing anomalous force would first trigger artifact and momentum-boundary investigation;
- only an observable specifically predicted by a G1+G2 model can count as evidence for the corresponding spacetime claim;
- independent replication is required before any extraordinary interpretation.

The current hardware plan therefore remains a prerequisite for trustworthy small-force work but is not itself a warp-drive experiment.

## Engineering chain that must close

A G3 candidate needs an explicit causal chain:

`power/control input -> physical source state -> predicted stress-energy -> predicted metric/field -> predicted observable -> calibrated sensor response`.

Every arrow must be modeled or measured. Missing arrows are not filled by analogy.

At minimum the actuator model must specify:

- source materials/fields and geometry;
- drive waveform and power;
- thermal load and waste heat;
- expected stresses and mechanical motion;
- electromagnetic emissions/couplings;
- momentum exchange path;
- predicted spatial and temporal signature;
- safe shutdown state;
- failure modes;
- scaling law with a falsifiable null limit.

## Measurement hierarchy

### Stage 0 — instrument qualification

Demonstrate traceable signed reference forces and/or reference displacements/phase shifts with full uncertainty. No device-under-test claims.

### Stage 1 — null apparatus characterization

Operate the complete setup with sham loads, dummy power, cable-motion controls, thermal cycling, magnetic/electric field monitoring, vibration monitoring, pressure/airflow control and randomized blinded schedules.

### Stage 2 — conventional source validation

Use a known actuator with closed momentum accounting to prove the apparatus recovers the correct sign, magnitude, time response and scaling.

### Stage 3 — candidate-device test

Run a preregistered candidate protocol with raw data locked before interpretation. Analyze thrust-like and curvature-like observables separately.

### Stage 4 — invariant-effect follow-up

Only if Stage 3 yields a repeatable anomaly consistent with a specific G1+G2 prediction should the project deploy dedicated interferometric, timing, accelerometric or geodesic-deviation measurements.

### Stage 5 — independent replication

Separate operator, apparatus and preferably separate laboratory. Replication must use the preregistered signature, not a post-hoc redefinition.

## Artifact budget

Every candidate must explicitly bound, measure or randomize against:

- thermal expansion and thermal gradients;
- outgassing and radiometric forces;
- convection and airflow;
- acoustic coupling;
- ground and structural vibration;
- cable forces and connector torque;
- magnetic fields and gradients;
- electrostatic charging;
- RF pickup and rectification;
- power-supply transients;
- center-of-mass shifts;
- support creep/hysteresis;
- sensor nonlinearity and saturation;
- digitizer timing/aliasing;
- software filtering and baseline subtraction;
- operator expectation and unblinding.

Unknown artifact terms count against the claimed effect; they are not assumed zero.

## Detection standard for a metric claim

A force residual alone cannot pass this standard.

A metric/curvature claim must identify an observable tied to invariant or operationally defined spacetime behavior, such as a predicted differential proper-time/phase shift, geodesic deviation, light-path change or acceleration field with a specified spatial pattern.

The predicted signature must include:

- magnitude;
- sign;
- spatial dependence;
- temporal dependence;
- response to source reversal/modulation;
- distance scaling;
- null configuration;
- systematic-error discriminants.

A signal that lacks these predeclared features is an anomaly, not confirmation.

## Adversarial failure modes

### F1 — Tiny-force = warp

Failure: unexplained thrust is called spacetime curvature.

Disposition: reject; first close momentum and artifact budgets.

### F2 — Sensor resolution = experiment sensitivity

Failure: catalog resolution is treated as achieved uncertainty.

Disposition: reject; sensitivity is established only by calibrated end-to-end performance.

### F3 — Signless positive-only calibration

Failure: instrument is qualified only with one-direction loads.

Disposition: reject under the existing signed-force gate.

### F4 — Post-hoc signature selection

Failure: after seeing data, the theory prediction is altered to match the anomaly.

Disposition: classify as exploratory and require a new preregistered confirmatory run.

### F5 — Correlated replication

Failure: same code, same sensor family, same operator or same raw dataset is counted as independent confirmation.

Disposition: record correlation and do not inflate independent support.

### F6 — G3 bypasses G2

Failure: an unexplained lab anomaly is used to infer a warp source without a defensible stress-energy/metric prediction.

Disposition: preserve the anomaly as data; do not promote the interpretation.

## Current forensic verdict

**No warp actuator has passed G3 in this project.** No functioning warp drive, engineered warp bubble, independently replicated anomalous thrust, or metric signature is claimed.

The strongest immediate program is therefore not "build a warp engine." It is:

1. qualify the measurement system with known signed references;
2. construct candidate source models only after G2;
3. preregister an observable that distinguishes the candidate from ordinary coupling;
4. demand independent replication.

## Next decisive work

1. finish a traceable signed calibration architecture in the existing target band;
2. add a curvature-observable requirements matrix beside the force matrix;
3. require every candidate actuator to publish a complete causal chain from input power to predicted observable;
4. design null/reversal/blinding procedures before candidate hardware testing;
5. do not purchase or build speculative high-energy hardware until a specific G2 source and safe G3 observable justify it.

**Promotion rule:** an anomaly may become `EXPERIMENTAL` only for the measured quantity itself. It does not become evidence for warp propulsion until the preregistered G1→G2→G3 causal prediction survives artifact controls and independent replication.
