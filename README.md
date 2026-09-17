# Warp / Medium Interaction & Propulsion Research Lab

**Project version:** 0.2.0 research snapshot on `main`; newer experimental work is in stacked, unmerged PRs. **Public educational project; no functioning novel propulsion mechanism, working warp drive, measured thrust or breakthrough claimed.**

**Primary goal:** identify, model, and eventually independently demonstrate a functioning propulsion mechanism. It must exchange momentum with an identifiable reservoir, account for energy input, yield reproducible net thrust beyond uncertainty, and support independent replication.

**Project originator:** Robert (public full-name/credit details not confirmed). **AI contribution:** ChatGPT-assisted organization, code, calculations, critical review and drafting, not independent peer review. See [CREDITS.md](CREDITS.md).

## Students and contributors

Start with the [student guide](STUDENTS.md), [contribution instructions](CONTRIBUTING.md) and [hardware acquisition plan](docs/HARDWARE_ACQUISITION_PLAN.md). The proposed personal prototype has a CAD $500–$1,000 budget, but no reference design, bill of materials, purchase, build, measured sensitivity or university affiliation has been verified. First reproduce a published thrust stand and calibrate known forces before investigating new mechanisms.

**Licensing:** [LICENSE.md](LICENSE.md) sets MIT for original project-owned software, CERN-OHL-S-2.0 for original hardware design source and CC BY 4.0 for original educational/research documentation. Third-party material retains its own rights. The repository is public; this does not imply external endorsement.

## Research navigation

- [Research charter and gates](docs/CHARTER.md)
- [Hypotheses and falsification](docs/HYPOTHESES.md)
- [Research log](docs/RESEARCH_LOG.md) and [error log](docs/ERROR_LOG.md)
- [First model: 1-D steady pressureless matter](theory/one_dimensional_dust.md)
- [Finite-time conditional model](theory/finite_time_dust.md)
- [Session logs](research/sessions/)
- [Propulsion candidates](docs/PROPULSION_CANDIDATES.md)
- [References](literature/REFERENCES.md)
- [Experimental protocol](validation/EXPERIMENT_PROTOCOL.md)
- [Roadmap](docs/ROADMAP.md) and [hourly handoff](docs/HOURLY_HANDOFF.md)

## Reproduce baseline tests (Python 3.10+, standard library only)

```sh
python -m unittest discover -s tests -v
python simulations/benchmark.py
python -m simulations.transient_benchmark
```

These tests check documented SI dimensional bookkeeping, momentum/energy benchmarks, steady flux identity, limiting cases, continuity residual, finite-time characteristic invariants, RK4 convergence and material-interval mass quadrature. They do **not** validate a warp drive or solve Einstein's equations. Numerical benchmark output is not experimental data.

## Model boundaries

1. Established physics baseline: rocket and photon thrust and free-body accounting.
2. Mathematical toys: prescribed Alcubierre-type shift in 1+1D; steady and finite-time dust moving with the Eulerian congruence, without pressure or matter backreaction.
3. Future: relativistic fluids and solids, full stress-energy, Einstein constraints, source/actuator model and calibrated test rig.
4. UAP claims are separate unverified hypotheses, not measured inputs.

A writable metric is not a manufacturable engine. Bobrick & Martire (2021) analyze the need for propulsion even for warp shells (see references).

## Provenance and continuity

The initial 0.2.0 snapshot was created when GitHub write access was unavailable; subsequent research exists in stacked PRs. Do not treat `main` as the latest experiment, silently overwrite divergent logs or confuse simulations with physical measurements. Library snapshots and hourly research sessions may have additional lineage; verify commit and session provenance before combining. Public attribution and third-party redistribution must follow CREDITS.md and LICENSE.md.
