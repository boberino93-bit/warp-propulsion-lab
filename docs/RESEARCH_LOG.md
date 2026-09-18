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

## 2026-09-16 08:23 UTC — interview evidence audit

Starting remote 23e3bace1b76638e0bebd65bdd4c33a2211ee75e verified. See [session](../research/sessions/2026-09-16-0823-UTC.md). Demonstrated sonar endpoint non-identifiability: 2500 m in 25 s gives 100 m/s relative average, not a unique peak. Added four kinematic checks; 25 total tests pass. Accounted for all interview example families without assuming independent evidence or assigning unsupported alien probabilities. No propulsion mechanism established. Previous covariant stress-energy calculation remains next.

## 2026-09-16 08:28 UTC — v0.3.0 covariant dust research imported

Starting v0.2.0 Library archive and session; GitHub was unavailable during original session. For prescribed 1+1 shift, Eulerian comoving test dust has `T^{mu nu}=epsilon n^mu n^nu`, Eulerian local momentum zero and coordinate `T^{tx}=epsilon beta` not thrust. Unit lapse gives geodesic normal, so stress-energy conservation reduces to the previous continuity equation. Moving-boundary relative flux is `-v_s epsilon(1-f)` and follows the characteristic invariant; not a reaction force. Initial import error in test corrected; 24 local snapshot tests passed, not merged-tree tests. Original archive retained in Library. Distinct remote interview work retained. PR #1 merged theory and three tests to main at `3e8914054b3b4864dbaeaa11025350f2b882355d`. See [session](../research/sessions/2026-09-16-0828-UTC.md).

## 2026-09-16 08:42 UTC — 3+1 Hamiltonian source-energy gate

Starting verified merged main `3e8914054b3b4864dbaeaa11025350f2b882355d`. Independently contracted ADM extrinsic curvature for flat 3-slices, lapse 1 and shift `beta^x=-v f`. Required Eulerian energy `E=-v²[(partial_y f)²+(partial_z f)²]/(32 pi)` in G=c=1, nonpositive; longitudinal gradient cancels. Added four tests; extracted Library snapshot plus new tests: 28/28 pass, but that checkout lacks four remote interview tests, so merged-tree test count is NOT yet verified. See [session](../research/sessions/2026-09-16-0842-UTC.md). Next: momentum constraint and observer-explicit source momentum, boundary accounting, then full combined suite and persistence checks.

## 2026-09-16 15:30 UTC — v0.3.8 exact covariant x-momentum gate
Derived the exact mixed-index conservative x projection. Independent symbolic Einstein-tensor calculation gives `partial_mu T^mu_x = (1/2)T^{ab} partial_x g_ab = v^2 f_x(f_yy+f_zz)/(16 pi)`. For a Gaussian, this differs from the v0.3.7 truncated residual by a factor `f`; exact terms cancel pointwise covariantly and integrate to zero. No reaction thrust found. Full reconstructed suite: 64 tests pass. Intermediate v0.3.2-v0.3.7 history remains preserved in versioned session files and Library snapshots; this remote cumulative log had not been appended during those sessions and should be backfilled from those preserved records in a dedicated reconciliation pass rather than guessed.

## 2026-09-16 16:26 UTC — v0.3.9 Gaussian Eulerian energy-budget gate
Starting verified GitHub main `18dbaf18fe4de853457736625e213fc8da5a8801` and v0.3.8 Library snapshot. Integrated the exact Hamiltonian-constraint Eulerian energy density for `f=exp(-r^2/sigma^2)`: `E_total=-v^2 sqrt(pi) sigma/(32 sqrt(2))` in geometric units. Requirement is nonpositive, even in velocity reversal, quadratic in speed and linear in Gaussian scale. Independent cylindrical quadrature agrees. This quantifies the global source-energy requirement but does not yet derive the full local Eulerian energy-flux/work projection.


## 2026-09-18 01:32 UTC — v0.3.37 long-memory structure slice

Starting merged main `982bbfd3b2f9a634aed4fe92ac6f9ba9969c11fd`. Under the frozen 15.585078155794357 µN synthetic calibration threshold, the preregistered `persistence_power=0.5` holdout changed only the multiscale AR(1) correlations (`rho_hold=sqrt(rho_base)`) while normalizing each trace to 5 µN sample standard deviation. Result: 125/10,000 null false positives (1.2500%; 95% Wilson upper 1.48723819%) and 10,000/10,000 synthetic detections at an injected 20 µN; the <=2% Wilson-upper criterion passed. Three focused tests passed. This is not hardware measurement or propulsion evidence. See [session](../research/sessions/2026-09-18-0132-UTC.md). Next: complementary frozen 10,000-trial `persistence_power=2.0` slice.


## 2026-09-18 02:30 UTC — v0.3.38 complementary long-memory structure slice

Starting merged main `d6f908d3a2e58fcfa1752054c6606b715b411772`. The preregistered shorter-memory holdout changed only `persistence_power` to 2.0 under the unchanged 15.585078155794357 µN threshold and 10,000-trial Wilson criterion. Result: 115/10,000 null false positives (1.1500%; 95% Wilson upper 1.37852927%) and 10,000/10,000 synthetic detections at an injected 20 µN; PASS. No code or hardware changed, and this is not measured thrust or a validated physical tolerance. See [session](../research/sessions/2026-09-18-0230-UTC.md). Next: primary-source comparison of two published thrust stands before any design selection or purchase.


## 2026-09-18 07:31 UTC — v0.3.39 primary-source thrust-stand acquisition gate

Starting merged main `3c409bd52c5386d55cc0623d676f1fa83d441c61`. Compared the Georgia Tech pulsed torsional stand (AIAA 2018-2117) and AST/DLR low-drift balance (IEPC-2015-257) against the frozen calibration, controls, rights, reproducibility, and CAD 500–1,000 gates. Georgia Tech demonstrates impulse rather than steady 0.1–1 mN force and leaves dynamic calibration as future work. AST/DLR states a 0.1–1000 mN range, but its in-situ voice-coil calibration is not independent in physical principle and the paper leaves a different-principle method for future work. Neither source supplies a complete live-priced BOM, redistributable construction package, or explicit open-hardware license. Both candidates therefore fail this acquisition round; no design was selected and no purchase was made. See [screen](../research/hardware/thrust-stand-primary-source-screen-2026-09-18.md) and [session](../research/sessions/2026-09-18-0731-UTC.md). Next: resolve the open construction-rights, full-BOM, and demonstrated-calibration gates for one candidate before any selection.


## 2026-09-18 08:29 UTC — v0.3.40 open-source stand acquisition gate

Starting merged main `23b9d03173195304067569e3e5456122e391024c`. Screened the MIT-licensed Pablo18011 RC Motor Thrust Stand at upstream commit `e5593bd01c35a8805df4f7739a2e728ce212812c`. Its 5 kg load cell is documented only as a gram-scale hobby propeller instrument; the source publishes no traceable calibration, raw results, noise/drift, hysteresis or uncertainty across the required 0.1–1 mN range (0.010197–0.101972 g, about 2.04–20.4 ppm full scale). The parts list lacks orderable identifiers and required calibration/control hardware, so a complete Canadian BOM cannot be priced without silently designing substitutions. Candidate rejected; no design selection or purchase. See [gate](../research/hardware/open-source-stand-gate-2026-09-18.md) and [session](../research/sessions/2026-09-18-0829-UTC.md). Next: freeze the calibration-demonstrator requirements matrix before sensor selection.

## 2026-09-18 — Calibration-demonstrator requirements frozen

Preregistered a procurement-neutral 0.1–1 mN acquisition gate with independent traceability, signed randomized cycles, bracketed zeros, complete uncertainty and artifact controls. The lowest point requires `U95 ≤ 0.020 mN` and `|E| + U95 ≤ 0.020 mN`. This is a project requirement, not a hardware result. No component was selected or purchased. Session: `research/sessions/2026-09-18-0930-UTC.md`.
