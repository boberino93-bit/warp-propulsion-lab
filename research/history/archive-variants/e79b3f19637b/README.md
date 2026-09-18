# Warp / Medium Interaction & Propulsion Research Lab

**Project version:** 0.2.0 research snapshot (finite-time toy extension; 2026-09-16 UTC)

**Primary goal:** identify, model, and eventually independently demonstrate a *functioning propulsion mechanism*. A functioning mechanism must exchange momentum with an identifiable reservoir (exhaust, radiation, external medium/field, etc.), account for energy input, yield reproducible net thrust outside measurement uncertainty, and support independent replication. There is presently **no claimed novel propulsion mechanism, working warp drive, or breakthrough**.

**Project originator:** Robert (public name/credit details to be confirmed before external publication). **AI contribution:** ChatGPT-assisted organization, code, calculations, critical review and drafting; outputs are not external peer review. See [CREDITS.md](CREDITS.md).

## Start here

- [Research charter and gates](docs/CHARTER.md)
- [Hypotheses and falsification](docs/HYPOTHESES.md)
- [Research log](docs/RESEARCH_LOG.md) and [error log](docs/ERROR_LOG.md)
- [First model: 1-D, steady, pressureless matter](theory/one_dimensional_dust.md)
- [Finite-time characteristic model, explicitly conditional](theory/finite_time_dust.md)
- [Per-session logs and recovery instructions](research/sessions/)
- [Propulsion candidate matrix](docs/PROPULSION_CANDIDATES.md)
- [Literature references](literature/REFERENCES.md)
- [Experimental protocol](validation/EXPERIMENT_PROTOCOL.md)
- [Roadmap](docs/ROADMAP.md), [hourly handoff](docs/HOURLY_HANDOFF.md)

## Reproduce initial tests (Python 3.10+, standard library only)

```sh
python -m unittest discover -s tests -v
python simulations/benchmark.py
python -m simulations.transient_benchmark
```

Tests check dimensional bookkeeping through explicitly documented SI conventions, momentum/energy benchmarks, steady flux identity, limiting cases, continuity residual, finite-time characteristic invariants, RK4 convergence and material-interval mass quadrature. They do **not** validate a warp drive or solve Einstein's equations. `simulations/benchmark.py` generates demonstrative numerical values, not experimental data.

## Model boundaries

1. Established physics baseline: rocket and photon thrust, free-body accounting.
2. Mathematical toys: a **prescribed** Alcubierre-type shift in 1+1D, steady **and finite-time** dust moving with the Eulerian congruence, no pressure, no matter backreaction.
3. Future: finite-time characteristics, relativistic fluids and solids, full stress-energy, Einstein constraints, source/actuator model, test rig.
4. UAP claims belong to a **separate hypothesis comparison**, not inputs treated as measured truths.

**Important:** A metric that can be written down is not a manufacturable engine. Bobrick & Martire (2021) explicitly analyze the need for propulsion even for warp shells (DOI in references).

## Continuity and publication

A snapshot of this repository can be saved to the user's ChatGPT Library. Automated hourly responses cannot be assumed to edit this repository, share a durable filesystem or know findings of every prior run. See [hourly handoff](docs/HOURLY_HANDOFF.md). At the time of the v0.2.0 session, GitHub write access was unavailable; do not assume the remote was updated. No license is granted for redistribution yet; decide licensing and preferred public attribution before publishing. No externally reviewed results are claimed.
