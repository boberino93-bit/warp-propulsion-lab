# Forensic Analysis G1 — Mathematical Warp Geometry

**Date:** 2026-10-07  
**Project:** Warp Propulsion Lab  
**Gate:** G1 — mathematical existence / geometry  
**Status:** `SUPPORTED WITH STRICT SCOPE`  
**Evidence class:** `ESTABLISHED` for existence of warp-drive-type metrics in general relativity; `NOT ESTABLISHED` for physical constructibility or propulsion.

## Question

Can general relativity represent a spacetime geometry with the functional characteristics usually called a "warp bubble" — a compact transported region embedded in an asymptotically ordinary exterior — without treating the geometry itself as evidence that an engine can create it?

This gate deliberately asks only a mathematical question. It does **not** ask whether the required stress-energy is physically admissible, whether a source can be built, whether the bubble is stable or controllable, or whether a laboratory has generated such curvature.

## Claim decomposition

The phrase "warp drive is possible" hides several non-equivalent claims:

1. a metric can be written down;
2. the metric is a valid Lorentzian spacetime and the desired kinematic behavior follows from it;
3. the corresponding Einstein tensor can be computed;
4. a physically admissible stress-energy tensor can source it;
5. a realizable actuator can create and control that source;
6. an experiment can distinguish the resulting invariant spacetime effect from artifacts.

G1 concerns only items 1–3. Passing G1 conveys no credit toward items 4–6.

## Primary evidence

### Alcubierre 1994

Miguel Alcubierre constructed a spacetime metric in which a compact region can be translated relative to distant observers while a ship inside follows a timelike worldline locally. The original paper explicitly states that exotic matter is required. This establishes the narrow proposition that a warp-like spacetime is representable within the formalism of general relativity; it does not provide a source or actuator.

Reference: M. Alcubierre, *The warp drive: hyper-fast travel within general relativity*, Class. Quantum Grav. 11, L73–L77 (1994), DOI `10.1088/0264-9381/11/5/001`, arXiv `gr-qc/0009013`.

### Natário 2002

José Natário constructed a warp-drive spacetime with zero expansion, demonstrating that the popular "space expands behind and contracts ahead" description is not the defining mathematical feature of the entire warp-drive class. This is important forensic evidence against treating one coordinate narrative or one particular shape function as the mechanism itself.

Reference: J. Natário, *Warp drive with zero expansion*, Class. Quantum Grav. 19, 1157–1165 (2002), arXiv `gr-qc/0110086`.

### Bobrick & Martire 2021

Bobrick and Martire developed a broader spacetime classification that treats warp drives as material shells and discusses both subluminal and superluminal classes. Their framework reinforces the separation between "metric exists" and "engine exists": they explicitly argue that warp-drive shells still require propulsion.

Reference: A. Bobrick and G. Martire, *Introducing physical warp drives*, Class. Quantum Grav. 38, 105009 (2021), DOI `10.1088/1361-6382/abdf6e`, arXiv `2102.06824`.

## What is actually established

The following proposition survives adversarial narrowing:

> General relativity admits mathematically specified spacetime metrics with warp-drive-like kinematic properties.

That proposition is strong enough to justify continued theoretical study and weak enough to avoid smuggling in engineering feasibility.

The following stronger propositions do **not** follow:

- that a superluminal warp bubble is physically realizable;
- that any proposed stress-energy is allowed by nature;
- that a finite-energy source can be assembled;
- that the metric can be generated from initially ordinary laboratory conditions;
- that a bubble can be started, steered, stopped, or stabilized;
- that any measured force anomaly would constitute a warp metric;
- that UAP reports supply boundary conditions, source terms, or validation data.

## Coordinate and invariant checks

Any future G1 candidate must distinguish coordinate description from invariant physics. A numerical metric candidate is not promoted merely because its lapse, shift, or coordinate velocity "looks like" Alcubierre.

Required checks:

1. specify signature, coordinates, lapse, shift, spatial metric, and units;
2. verify the metric remains Lorentzian on the claimed domain;
3. compute curvature quantities rather than relying only on coordinate pictures;
4. identify asymptotic behavior and the compact/disturbed region;
5. inspect horizons, causal accessibility and geodesic behavior where relevant;
6. verify the candidate is not merely flat spacetime in unusual coordinates if nontrivial curvature is claimed;
7. state the observer congruence used for any energy-density or velocity statement.

A coordinate velocity above `c` is not itself an invariant demonstration of local superluminal motion. Conversely, local subluminal motion does not by itself resolve global causal or source-feasibility questions.

## Adversarial failure modes

### F1 — Metric-to-engine substitution

Failure: a valid line element is described as a propulsion mechanism.

Disposition: reject. A metric specifies geometry; an actuator requires a source model and dynamics.

### F2 — Coordinate narrative treated as mechanism

Failure: "expansion behind/contraction ahead" is treated as necessary or sufficient.

Disposition: reject. Natário-type constructions show warp-like transport is not uniquely characterized by that narrative.

### F3 — Prescribed geometry treated as dynamically generated

Failure: code prescribes a shift vector or shape function and the result is described as generated curvature.

Disposition: reject. Prescribing `g_{μν}` is not solving for a realizable source or initial-value evolution.

### F4 — Visualization treated as invariant evidence

Failure: a plotted bubble, field line, or coordinate displacement is promoted without curvature or causal diagnostics.

Disposition: block promotion until invariant checks exist.

### F5 — G1 result leaks into G2/G3

Failure: "GR allows the metric" becomes "nature permits the matter" or "we can build it."

Disposition: explicitly downgrade to G1 only.

## Reproducible qualification procedure

A candidate passes G1 only when all of the following are present:

- exact metric definition and domain;
- dimensional conventions and SI interpretation where applicable;
- independent symbolic or numerical consistency checks;
- at least one curvature/invariant diagnostic appropriate to the claim;
- explicit causal/horizon assumptions for any transport claim;
- source question left open unless separately solved under G2;
- no engineering claim.

If any item is missing, the result remains `DERIVED-CONDITIONAL` or `SPECULATIVE`.

## Current forensic verdict

**G1 passes at the class-existence level.** Warp-drive-like geometries are legitimate objects of general-relativistic analysis. This is not controversial in the narrow mathematical sense represented by the cited literature.

The project must therefore stop spending effort on proving merely that "a warp metric can be written." The productive G1 work is now comparative and discriminating: characterize geometry families, causal structure, invariants, stability-relevant features and source demands in forms that can feed G2.

## Next decisive work

1. reproduce selected Alcubierre/Natário/Bobrick-Martire metrics in a common 3+1 notation;
2. compute a shared invariant/causal diagnostic set;
3. define a machine-checkable interface from geometry to required Einstein tensor;
4. hand only those source requirements — not the desired conclusion — to G2.

**Promotion rule:** G1 may inform G2, but G1 can never by itself promote a candidate to "physically possible," "buildable," "propulsive," or "detected."
