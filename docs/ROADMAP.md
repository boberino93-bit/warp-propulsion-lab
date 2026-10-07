# Roadmap and deliverables

- M0 (this snapshot): explicit mission, sourcing, attribution, derivation, baseline code and runnable tests. **Scaffold delivered; no new propulsion discovery.**
- M1: audit exact 1D metric/congruence derivation against GR notation; finite-time characteristic initial-value solution, density near f=1; numerical convergence & manufactured solutions.
- M2: identify tractable propulsion concept with clear external momentum transfer or a falsifiable theory of its absence; baseline power-vs-thrust and artifact budget.
- M3: 2D/3D relativistic test-fluid treatment on a fixed metric using well-tested solver; air/water equations of state; boundary conditions and uncertainty.
- M4: solid stress and electromagnetism as separately specified couplings; distinguish metric-induced effects from unspecified engine side effects.
- M5: self-consistent stress-energy/Einstein constraints and feasibility of an actuator; physical resource limits.
- M6: preregistered laboratory demonstration of a proposed mechanism (if one emerges); independent replication, optional paper submission.

At each milestone: inputs, assumptions, code version, units, observables, null case, residuals, alternative explanation, confidence and reviewer comments. No calendar guarantee or forecast of a breakthrough.

## 2026-09-16 transient-model increment

M1 partially advanced: implemented finite-time initial-value characteristics and independent checks in `src/transient_dust.py`, `tests/test_transient_dust.py`, `theory/finite_time_dust.md`. **Not** a completed M1: no derivation of coupled matter stress-energy, pressure, Einstein constraints or field source. Next gate: covariant stress-energy and energy/momentum flux, plus independently checked initial/boundary conditions.

## 2026-10-07 warp three-gate forensic program

The project now separates warp feasibility into three independent promotion gates rather than one binary "warp drive possible?" question.

### W1 / G1 — geometry normalization

Deliverables:

- reproduce Alcubierre, Natário and selected generalized warp metrics in one declared 3+1 convention;
- compute common curvature/invariant and causal diagnostics;
- distinguish coordinate presentation from nontrivial curvature;
- emit a machine-readable geometry→Einstein-tensor/source requirement.

**Stop rule:** a valid metric cannot be promoted to a physical-source or engine claim.

### W2 / G2 — source reconciliation

Deliverables:

- reproduce representative Bobrick-Martire, Santiago-Schuster-Visser and Fuchs-type source/energy-condition results;
- evaluate them with one transparent observer-aware checker;
- record exact differences in geometry definition, subluminal/superluminal regime, symmetry, ADM mass, observer set, pointwise/averaged condition, and source interpretation;
- require conservation, resource and candidate matter/field accounting.

**Stop rule:** positive energy density in one frame, or a subluminal construction, cannot be promoted to a universal or superluminal feasibility claim.

### W3 / G3 — actuation and metrology

Deliverables:

- preserve the existing signed-force calibration program as instrument qualification;
- add a separate curvature-observable requirements matrix;
- require a complete `input -> source -> T_mu_nu -> metric -> observable` causal chain before candidate testing;
- preregister null/reversal/blinding and artifact controls;
- require independent replication before mechanism-level promotion.

**Stop rule:** unexplained force is an anomaly in the measured quantity, not evidence of warp curvature.

The controlling directive and forensic reports are linked from `README.md`.
