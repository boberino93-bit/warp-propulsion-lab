# Student guide — Open Propulsion Lab

**Status:** public educational research repository; original project-owned software, hardware design source and documentation are available under the scoped licenses in [LICENSE.md](LICENSE.md). The thrust stand is **not built or validated**. Read [hardware acquisition plan](docs/HARDWARE_ACQUISITION_PLAN.md) before buying parts. No university partnership or endorsement is claimed.

## Learning pathway

1. Read README, CHARTER, EXPERIMENT_PROTOCOL, latest session and research/error logs. Verify the provenance of every numerical claim. Primary objective: independently test propulsion using momentum conservation, measured power, calibrated force and uncertainty; warp models are secondary theoretical questions.
2. Reproduce the code with Python 3.10+ and `python -m unittest discover -s tests -v`; record exact commit SHA, Python version, commands and complete output. Research PRs may be newer than main and cumulative logs may diverge.
3. Compare at least two published thrust-stand designs and upstream licenses. Cost a complete CAD $500–$1,000 bill of materials before selecting or purchasing hardware. The originator already has a 3D printer, soldering station and multimeter. No design or prices are yet verified.
4. Obtain responsible-builder or qualified laboratory-supervisor safety review. Do not attempt improvised pressure vessels, unreviewed high voltage, high-power lasers or vacuum equipment.
5. Reproduce known-force calibration over approximately 0.1–1 mN and measure actual noise/drift, reversals and sham response. The earlier 35 µN detection figure is **synthetic, not measured**.
6. Only after calibration, test a low-risk established reaction-mass example with measured mass flow, exhaust velocity, input power and complete momentum boundary. Share raw data, uncertainty and negative results.

## How to participate

Read [CONTRIBUTING.md](CONTRIBUTING.md). Submit a focused issue or PR with falsifiable question, references, unit-checked prediction, full-system free-body diagram, instrumentation and independent calibration, safety review, null/reversal/thermal/EM/cable/airflow controls, preregistered pass/fail criteria, uncertainty and reproducible code or raw data. Label simulations, proposals, measurements and independent replication separately. Respect third-party licensing and credit; do not claim institutional affiliation without authorization.
