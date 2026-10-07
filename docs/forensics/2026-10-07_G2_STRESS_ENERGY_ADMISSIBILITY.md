# Forensic Analysis G2 — Physical Stress-Energy and Admissibility

**Date:** 2026-10-07  
**Project:** Warp Propulsion Lab  
**Gate:** G2 — source physics / stress-energy admissibility  
**Status:** `OPEN — CONDITIONAL AND CONTESTED`  
**Evidence class:** mixture of `ESTABLISHED`, `DERIVED-CONDITIONAL`, and `UNKNOWN`.

## Question

Given a warp-drive-type geometry that clears G1, can the required Einstein tensor be sourced by stress-energy that is physically admissible under the stated theory, observer set, boundary conditions and resource assumptions?

This is the first gate at which "mathematically representable" can begin to approach "physically permissible." It is still not an engineering gate.

## Governing relation

For standard general relativity with cosmological term omitted for local analysis,

`G_{μν} = (8πG/c^4) T_{μν}`.

A prescribed metric determines an Einstein tensor. The inverse problem is then not merely "is some component positive?" but whether the full inferred `T_{μν}` can correspond to a defensible matter/field model and satisfy the relevant consistency conditions.

## Evidence in tension

### Original Alcubierre construction

The original solution requires exotic matter / negative energy density in the relevant frame. That is an explicit warning in the source paper, not a later criticism added from outside the proposal.

### Bobrick & Martire 2021

Bobrick and Martire exhibit broad warp-drive classes and report subluminal, spherically symmetric positive-energy examples. They also stress that warp shells require propulsion. This supports continued investigation of **subluminal** physical warp geometries, but it does not settle every energy condition for every observer or every geometry.

### Santiago, Schuster & Visser 2021/2022

Santiago, Schuster and Visser challenge positive-energy warp-drive claims by emphasizing that the weak energy condition is an all-timelike-observer statement, not merely a check of energy density seen by one preferred Eulerian congruence. Their analysis concludes that physically reasonable warp drives generically violate the null energy condition within standard GR.

Reference: J. Santiago, S. Schuster and M. Visser, *Generic warp drives violate the null energy condition*, arXiv `2105.03079`.

### Fuchs et al. 2024

Fuchs and collaborators numerically construct a constant-velocity **subluminal** warp-drive solution formed from a positive-ADM-mass matter shell plus a warp-like shift distribution, and report satisfaction of all standard energy conditions for their construction.

Reference: J. Fuchs et al., *Constant Velocity Physical Warp Drive Solution*, arXiv `2405.02709` (2024).

This result is important evidence but must be treated as a candidate construction to reproduce and reconcile with generic no-go arguments, not as a blanket proof that "warp drives need no exotic matter."

## Forensic reconciliation rule

Conflicting literature is not resolved by counting papers.

For each apparently conflicting result, the project must compare:

- exact definition of "warp drive";
- subluminal versus superluminal regime;
- symmetry assumptions;
- asymptotics and total ADM mass;
- observer congruence;
- pointwise versus averaged energy conditions;
- stress-energy eigenvalues and type;
- whether all timelike/null directions were tested;
- whether the geometry is stationary, constant-velocity, accelerating or dynamically formed;
- whether a material equation of state or field Lagrangian is supplied;
- whether the source is merely inferred from Einstein's equation or independently realizable.

A positive Eulerian energy density alone does not establish WEC/DEC. A no-go theorem proved under a narrower definition does not automatically rule out every broader construction. Both overextensions are prohibited.

## Mandatory source tests

A G2 candidate must publish or reproduce, at minimum:

1. `G_{μν}` and inferred `T_{μν}` in a declared orthonormal/tetrad basis;
2. energy density and principal stresses/eigenvalues;
3. NEC sampling or analytic proof over all relevant null directions;
4. WEC/DEC/SEC disposition with observer quantifiers stated explicitly;
5. total mass/energy measure appropriate to the asymptotics;
6. source localization and falloff;
7. conservation check `∇_μ T^{μν}=0`;
8. a candidate matter/field interpretation or an explicit statement that none is known;
9. formation/control assumptions;
10. sensitivity to bubble radius, wall thickness, velocity and acceleration.

For numerical solutions, grid convergence and constraint residuals are mandatory. "Solver returned a metric" is not sufficient.

## Quantum and resource constraints

If negative energy remains in a candidate, the project must not treat quantum-field examples of local negative energy as an unlimited engineering resource. The candidate must identify what quantum state or field model is intended and assess applicable quantum-inequality, duration/magnitude, backreaction and stability constraints.

If a candidate avoids negative local energy by adding large positive mass-energy, the project must account for that positive resource honestly. Moving difficulty from "negative energy" to "enormous ordinary mass/pressure" is not a solution unless the resulting source can plausibly be realized and controlled.

## Adversarial failure modes

### F1 — Preferred-observer laundering

Failure: one observer measures positive energy density, therefore WEC is declared satisfied.

Disposition: reject. WEC quantifies over all timelike observers.

### F2 — Subluminal result promoted to FTL

Failure: a positive-energy subluminal construction is cited as evidence that superluminal warp is physically permitted.

Disposition: reject unless a separate superluminal analysis satisfies its own gate.

### F3 — Einstein-tensor inversion treated as material recipe

Failure: a mathematically computed `T_{μν}` is described as a buildable material.

Disposition: reject. The source must be connected to an actual matter/field model or remain `UNKNOWN`.

### F4 — Energy conditions treated as the only physics

Failure: clearing energy conditions is treated as sufficient for feasibility.

Disposition: reject. Stability, causality, formation, control, total resources and actuator dynamics remain open.

### F5 — Literature-vote resolution

Failure: paper count or author prestige substitutes for assumption-by-assumption reconciliation.

Disposition: reject; create an explicit comparison matrix.

## Current forensic verdict

**G2 remains open.** The literature establishes that the source problem is substantially harder than G1 and that conclusions depend strongly on geometry class and regime.

The defensible current statement is:

> Some subluminal warp-like geometries have been proposed with positive-energy or all-energy-condition-satisfying stress-energy, while generic analyses identify severe energy-condition obstructions for broad warp-drive classes. These results require reproducible, assumption-matched reconciliation before the project can classify any specific candidate as physically admissible.

No project artifact currently establishes a laboratory-realizable stress-energy source for a warp bubble.

## Next decisive work

1. reproduce the Bobrick-Martire and Fuchs subluminal constructions under one energy-condition checker;
2. reproduce the Santiago-Schuster-Visser null-direction test under the same conventions;
3. build a table showing exactly where their definitions/assumptions overlap or differ;
4. require every future metric candidate to emit a machine-readable G2 source report;
5. keep superluminal and subluminal claims in separate evidence lanes.

**Promotion rule:** G2 cannot be passed by a prescribed metric, a single positive energy-density plot, or a citation to a subluminal example. Promotion requires a complete source audit under the exact candidate assumptions.
