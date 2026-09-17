# Student guide — Open Propulsion Lab

**Status:** educational research project in preparation. The repository is currently private, public licensing is not finalized, and no student access or institutional affiliation is claimed. The thrust stand has not been built or experimentally validated. Read the [hardware acquisition plan](docs/HARDWARE_ACQUISITION_PLAN.md) before purchasing parts.

## What you can study

The primary objective is to test propulsion claims using conservation of momentum, measured energy input, calibrated forces, uncertainty analysis and reproducible controls. Warp metrics are secondary theoretical work, not build instructions or evidence of a functioning engine. The photon-pressure, reaction-mass and calibration examples are established physics. Simulation outputs are not measurements.

## Suggested student pathway

1. Review README, CHARTER, EXPERIMENT_PROTOCOL, the latest session and research/error logs; identify the exact model and provenance of any number you quote.
2. Reproduce the software baseline with Python 3.10+ and `python -m unittest discover -s tests -v`. Record your commit SHA, Python version, command, full result and any failures. An unmerged research PR may contain newer work than `main`; do not silently combine divergent logs.
3. Before hardware acquisition, compare at least two published thrust-stand designs, independently check their sources and licenses, and cost a CAD $500–$1,000 bill of materials. Existing tools available to the originator: 3D printer, soldering station and multimeter. No specific instrument has been selected or priced yet.
4. Build only after a qualified supervisor or responsible builder reviews mechanical, electrical and laboratory safety. No improvised pressure vessels, unreviewed high voltage, high-power lasers or vacuum equipment.
5. First reproduce known-force calibration over approximately 0.1–1 mN and measure real noise/drift, reversal and sham responses. The 35 µN figure in earlier sessions is synthetic and is **not** demonstrated hardware sensitivity.
6. Only then test a low-risk, established reaction-mass example with measured mass flow, exhaust velocity, electrical power and an explicit full-system momentum boundary. Publish raw data and negative results, not just plots or successful runs.

## What to submit

For each proposed experiment or change, include a question that can fail, a complete free-body diagram and reaction reservoir, prediction with units, references, instrumentation and independent calibration, safety review, null/reversal/thermal/EM/cable/airflow controls, uncertainty budget, raw data or reproducible simulation code, and clear pass/fail criteria. Distinguish a proposal from a simulation, a measured result and an independently replicated result.

## Contributing and credit

Read [CONTRIBUTING.md](CONTRIBUTING.md). Submit issues or pull requests with exact reproducibility information once the repository is accessible. Do not represent yourself as affiliated with a university or claim an endorsement without authorization. Cite original papers and identify your own contributions. Repository visibility and the applicable software/documentation/hardware licenses must be explicitly resolved before public redistribution; GitHub visibility alone does not grant reuse rights.
