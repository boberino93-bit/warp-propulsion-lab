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

## 2026-09-16 UTC — v0.2.0 practice session, finite-time initial-value dust

- **Starting source:** v0.1.0 archive recovered from ChatGPT Library; original Git tree `fbd716d`. Previous 11 tests and bibliography reviewed; no earlier hourly findings accessible in repository.
- **One concrete advance:** derived finite-time characteristics `xi_dot = v_s(f-1)`, `dlog(rho)/dt = -v_s f'`, `dlog(J)/dt=v_s f'`, and analytic invariant `rho(t)(1-f_t)=rho_initial(1-f_initial)` for 1D fixed shift and the Eulerian dust congruence. Documented in `theory/finite_time_dust.md`, implemented in `src/transient_dust.py`.
- **Model result:** uniform initial Eulerian density does not imply the previous stationary density profile throughout the bubble. With `xi0=8 m`, `t=0.03 s`, `v_s=100 m/s`, `R=5 m`, `w=2 m`, initial density 1.225 kg/m3, front density rises to ~1.84988746 kg/m3; behind from `xi0=-8 m` it falls to ~1.16993816 kg/m3; central parcel is ~1.22403217 kg/m3 rather than the large stationary central density. Toy model only, no real fluid shocks or experimental measurement.
- **Checks:** 21 unit tests pass (original 11 + 10 new), including RK4 convergence, independent characteristic invariant, finite-difference gradient, time reversal and numerical material-interval quadrature. Initial mass per unit area in `[-12,12] m`: 29.4 kg/m2; quadrature 29.4011058969 kg/m2, relative error 3.76e-5. See session file for exact test output and limitations.
- **Literature check:** reviewed publisher abstracts/metadata for Alcubierre (1994), McMonigal et al. (2012) and Bobrick & Martire (2021); no originality claim or full-text literature review. Bobrick & Martire state a physical warp shell still requires propulsion.
- **GitHub outcome:** GitHub connector became unavailable at time of this attempt; no remote write or confirmation. Saved updated snapshot to ChatGPT Library for continuation. Preserve original v0.1.0.
- **Next falsifiable test:** derive an explicit covariant stress-energy flux and lab-frame energy/momentum budget for the specified dust congruence under fixed-background assumptions; compare against the analytic characteristic invariant before inferring any force or thrust.

## 2026-09-16 UTC — v0.3.0 covariant test-dust flux gate

- **Starting source:** verified v0.2.0 Library archive/session; GitHub connector still disabled, so remote HEAD remains unknown and no remote write was attempted.
- **One advance:** made the v0.2.0 dust stress-energy observer-explicit for the prescribed 1+1 shift. For `u^mu=n^mu=(1,beta)`, `T^{mu nu}=epsilon n^mu n^nu`; Eulerian measured energy is `epsilon` and Eulerian local momentum density is zero. Unit lapse makes the Eulerian normal geodesic, so `nabla_mu T^{mu nu}=0` reduces to the already-solved continuity equation for this pressureless test dust.
- **Boundary accounting:** constant-x coordinate current has `J^x=epsilon beta`; relative to a constant-xi boundary it is `epsilon(beta-v_s)=-v_s epsilon(1-f)`, conserved along characteristics by the v0.2.0 invariant. This is matter crossing a moving boundary, not a force on a device.
- **Critical negative result:** this test-dust sector supplies no reaction-force mechanism. The 1+1 reduction cannot establish the 3+1 Einstein source/energy budget; a physical propulsion claim must model the geometry-generating source or explicit matter/field interaction and global momentum balance.
- **Checks:** first new test run exposed an import-name error; corrected it. Final local run: **24 tests passed** in 0.300 s. No GitHub CI.
- **Next falsifiable test:** lift the prescribed shape to the standard 3+1 Alcubierre ADM metric and compute/check the Eulerian source quantities from the Einstein constraints (`rho_E`, momentum density `S_i`, stresses where feasible) for the exact shape convention, then integrate/sign-check energy density and identify source scaling with `v_s`, radius and wall thickness. Do not infer realizability from the metric alone.

## 2026-09-16 08:23 UTC — remote interview evidence audit (reconciled)

Remote commit d69aceb preserved. Interview transcripts and sparse frames were considered, not continuous video; original sonar data unavailable. Endpoint 2500 m/25 s implies 100 m/s average, not a unique peak; four remote tests added. See GitHub research/sessions/2026-09-16-0823-UTC.md for full original provenance.

## 2026-09-16 08:42 UTC — v0.3.1 reconciliation and ADM source-energy gate

Remote PR #1 merged v0.3.0 covariant dust theory and three tests with the independent interview audit, merge SHA 3e8914054b3b4864dbaeaa11025350f2b882355d. Re-derived standard 3+1 Alcubierre Eulerian source energy from Hamiltonian constraint: E=-v²(f_y²+f_z²)/(32pi) in geometric units; not a physical source mechanism. Four tests added. Extracted Library plus copied remote interview tests plus four new tests: 32 tests passed in 0.286s locally. GitHub CI status must be separately checked. Next one test: momentum constraint with sign convention and source/boundary bookkeeping.
