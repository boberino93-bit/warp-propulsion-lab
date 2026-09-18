# Warp / Medium Interaction & Propulsion Research Lab

**Project version:** 0.1.0 (initial reproducible scaffold; 2026-09-16 UTC)

**Primary goal:** identify, model, and eventually independently demonstrate a *functioning propulsion mechanism*. A functioning mechanism must exchange momentum with an identifiable reservoir (exhaust, radiation, external medium/field, etc.), account for energy input, yield reproducible net thrust outside measurement uncertainty, and support independent replication. There is presently **no claimed novel propulsion mechanism, working warp drive, or breakthrough**.

**Project originator:** Robert (public name/credit details to be confirmed before external publication). **AI contribution:** ChatGPT-assisted organization, code, calculations, critical review and drafting; outputs are not external peer review. See [CREDITS.md](CREDITS.md).

## Start here

- [Research charter and gates](docs/CHARTER.md)
- [Hypotheses and falsification](docs/HYPOTHESES.md)
- [Research log](docs/RESEARCH_LOG.md) and [error log](docs/ERROR_LOG.md)
- [First model: 1-D, steady, pressureless matter](theory/one_dimensional_dust.md)
- [Propulsion candidate matrix](docs/PROPULSION_CANDIDATES.md)
- [Literature references](literature/REFERENCES.md)
- [Experimental protocol](validation/EXPERIMENT_PROTOCOL.md)
- [Roadmap](docs/ROADMAP.md), [hourly handoff](docs/HOURLY_HANDOFF.md)

## Reproduce initial tests (Python 3.10+, standard library only)

```sh
python -m unittest discover -s tests -v
python simulations/benchmark.py
```

Tests check dimensional bookkeeping through explicitly documented SI conventions, momentum/energy benchmarks, steady flux identity, limiting cases, and continuity residual. They do **not** validate a warp drive or solve Einstein's equations. `simulations/benchmark.py` generates demonstrative numerical values, not experimental data.

## Model boundaries

1. Established physics baseline: rocket and photon thrust, free-body accounting.
2. Mathematical toy: a **prescribed** Alcubierre-type shift in 1+1D, dust moving with the Eulerian congruence, no pressure, no matter backreaction.
3. Future: finite-time characteristics, relativistic fluids and solids, full stress-energy, Einstein constraints, source/actuator model, test rig.
4. UAP claims belong to a **separate hypothesis comparison**, not inputs treated as measured truths.

**Important:** A metric that can be written down is not a manufacturable engine. Bobrick & Martire (2021) explicitly analyze the need for propulsion even for warp shells (DOI in references).

## Continuity and publication

A snapshot of this repository can be saved to the user's ChatGPT Library. Automated hourly responses cannot be assumed to edit this repository, share a durable filesystem or know findings of every prior run. See [hourly handoff](docs/HOURLY_HANDOFF.md). GitHub publishing is NOT performed. No license is granted for redistribution yet; decide licensing and preferred public attribution before publishing. No externally reviewed results are claimed.
