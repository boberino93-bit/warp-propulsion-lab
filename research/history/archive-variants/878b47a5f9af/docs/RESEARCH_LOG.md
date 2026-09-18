# Research log (append-only)

## 2026-09-16 UTC — v0.1.0 first reproducible scaffold

- Primary objective clarified: functioning propulsion, not just geometry. Authorship/creative origin documented, pending public-attribution preference.
- Grounding sources: Alcubierre (1994), McMonigal et al. (2012), Bobrick & Martire (2021). See references.
- Recast 1D density expression as an explicitly conditional **steady dust continuity solution**. It is not a universal warp-medium prediction, not a proof of a singularity or a working mechanism.
- Added minimal pure-Python source code, numeric identity tests and conventional momentum/energy baseline. Numerical code not run at time of this entry; test results should be appended after execution.
- No external repository published, no expert peer review, no experimental results, no GR solver, no working propulsion mechanism.

### Update protocol
Append a dated entry for every substantive iteration including (a) source/version, (b) new result, (c) independent checks, (d) mistakes/corrections, (e) unsupported leaps rejected, and (f) next falsifiable test. Never retroactively rewrite errors out of history; add a correction.

## 2026-09-16 UTC — v0.1.0 verification pass

- `python -m unittest discover -s tests -v`: **11 tests passed** (mathematical identities, limits, input guards, ideal momentum/energy baselines). This does not verify Einstein equations or any empirical propulsion.
- `python simulations/benchmark.py` produced F_rocket=300 N, ideal jet kinetic P=450,000 W, F_photon(1 kW radiated)=3.33564095e-6 N, and stationary toy flux -100 kg/(m² s) at sampled positions for rho0=1 kg/m³ and v_s=100 m/s.
- Important: finite density near the shape center depends on chosen profile and does not show a feasible bubble. Relative mass flux calculation is algebraically tautological once stationary density is inserted: it is a consistency check, not an independent physical prediction.
- All source references were verified for bibliographic metadata against publisher records, but the entire papers have not undergone a line-by-line literature review.
