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

## 2026-09-16 09:29 UTC — v0.3.2 ADM momentum-constraint gate

- **Starting source:** newest verified Library snapshot `warp-propulsion-lab-v0.3.1-reconciled.zip`; its latest session named the ADM momentum constraint as NEXT ONE TEST. @GitHub was attempted first but the connector became disabled during this run, so remote HEAD/CI/write could not be verified.
- **One advance:** derived the prescribed Alcubierre source momentum density for `beta_x=-v f`, flat spatial metric and `K_ij=(D_i beta_j+D_j beta_i)/2`: `S_x=-v(f_yy+f_zz)/(16pi)`, `S_y=v f_xy/(16pi)`, `S_z=v f_xz/(16pi)`. Opposite extrinsic-curvature convention flips all signs.
- **Global bookkeeping:** for smooth localized `f` with derivatives vanishing at the boundary, each volume-integrated component reduces to boundary terms and vanishes. Local required source momentum is nonzero, but this constraint supplies no hidden net reaction momentum for an isolated bubble.
- **Checks:** added Gaussian analytic derivatives and four regression tests (formula/sign under declared convention, linear velocity scaling, parity, expanding-domain integrated cancellation). Full reconstructed suite: **36 tests passed in 0.275 s** locally.
- **Literature:** Pfenning & Ford's Alcubierre analyses remain strong primary background on negative-energy restrictions; newer source-fluid papers were treated as context rather than evidence of realizability.
- **Persistence:** GitHub unavailable this run; preserve this version in Library and retry remote reconciliation next run. Do not claim remote sync or CI.
- **Next falsifiable test:** derive/check the remaining spatial stress components or an equivalent local conservation identity and explicitly compute whether time-dependent bubble acceleration introduces nonzero integrated source momentum/flux once boundary and field/source terms are included. This is the gate toward a full-system momentum budget.

## 2026-09-16 10:30 UTC — v0.3.3 accelerating-slice momentum gate

- **Starting source:** v0.3.2 Library snapshot; @GitHub was attempted first but connector returned disabled, so remote HEAD/write/CI are not claimed.
- **One advance:** for `beta_x=-v(t) f(x-x_s(t),y,z)`, flat spatial metric and unit lapse, the ADM momentum constraint is instantaneous and contains `v(t)` but no explicit acceleration `dv/dt`. The v0.3.2 source formulas therefore remain valid with `v -> v(t)`.
- **Global result:** for smooth localized shape derivatives vanishing at infinity, integrated source momentum remains a boundary cancellation on every slice. Acceleration does not create net integrated momentum through the momentum constraint alone.
- **Important limit:** this does not close conservation. Acceleration enters time derivatives/evolution equations and the required spatial stresses/energy flux; those must be derived before interpreting the geometry as propulsion.
- **Checks:** four tests added. First full run failed one overly tight finite-domain numerical tolerance (`2.538e-4` vs `2e-4`); expanded the integration domain rather than weakening the physical claim. Final full suite: **40 tests passed in 0.296 s** locally.
- **Literature:** Alcubierre (1994) remains the primary metric source; McMonigal, Lewis & O'Byrne (2012) explicitly treat accelerating/decelerating bubble interactions with test particles, not a realizable geometry source.
- **Next falsifiable test:** derive at least one independent ADM evolution-equation spatial-stress combination for time-dependent `v(t)` and isolate terms proportional to acceleration. Integrate the corresponding conservation/boundary contribution and test whether total source+field momentum closes without an external momentum flux.

## 2026-09-16 11:30 UTC — v0.3.4 acceleration trace-stress gate

- **Starting state:** @GitHub main HEAD independently verified as `d39625d57826f65e386a9470e8b259a68b659661`; Library v0.3.3 is newer and contains the unmerged v0.3.2/v0.3.3 work. Full v0.3.3 suite rerun before modification: 40 tests passed.
- **One advance:** used the ADM trace evolution equation for unit lapse/flat spatial metric. With `beta_x=-v(t)f` and `K=-v f_x`, the acceleration-only source combination is `(E+S)_acc=-a f_x/(4pi)` in geometric units.
- **Global result:** this local acceleration-dependent stress/energy-trace term is front/back antisymmetric for a symmetric localized bubble, and its volume integral is the boundary term `-a/(4pi) int partial_x f d^3x`, zero for decaying `f`. It therefore supplies no nonzero integrated reaction term by itself.
- **Limits:** this is one stress combination, not the full `S_ij`, energy flux, or a complete global gravitational momentum definition. No propulsion mechanism inferred.
- **Checks:** five new tests cover formula/sign, acceleration scaling, parity, local-nonzero/global-cancellation, and geometric-unit dimensional scaling. Full suite: **45 tests passed in 0.451 s** locally.
- **Next falsifiable test:** derive at least the longitudinal component `S_xx` (preferably all diagonal `S_ij`) from the ADM evolution equations or an independently checked Einstein tensor for time-dependent `v(t)`, then test whether acceleration-dependent source force/flux closes to boundary terms under a localized shape.

## 2026-09-16 12:27 UTC — v0.3.5 acceleration spatial-stress tensor

- Verified @GitHub main HEAD `4e1cdd76271dd4370b8cd49774a88c672ada59b4`; v0.3.4 Library lineage was current. Baseline 45 tests passed.
- Resolved acceleration-only ADM spatial stress: `Sxx=0`, `Syy=Szz=-a f_x/(8pi)`, `Sxy=a f_y/(16pi)`, `Sxz=a f_z/(16pi)`, `Syz=0`, reproducing prior trace `S=-a f_x/(4pi)`.
- x stress divergence is `a(f_yy+f_zz)/(16pi)` and integrates to zero for smooth localized shape; nonlocalized control retains boundary force. No surviving isolated reaction force found.
- Added five checks; full suite 50 tests passed locally. See session `research/sessions/2026-09-16-1227-UTC.md`.
- Next: covariant stress-energy conservation / energy-flux requirement for accelerating source.

## 2026-09-16 13:30 UTC — v0.3.6 acceleration-order conservation closure
- Starting remote HEAD: `40b48d11cfb642e5ce1b2e126cd949fdaef57372`; Library v0.3.5 matched the latest session lineage.
- One bounded advance: combined the existing momentum-constraint density `j_x=-v(f_yy+f_zz)/(16 pi)` with the v0.3.5 acceleration stress. The explicit acceleration term in `partial_t j_x` cancels `partial_j S_xj` pointwise.
- Propulsion result: negative. At acceleration order, the prescribed source closes local x-momentum bookkeeping internally; no external reaction momentum or net thrust appears.
- Validation: five new tests, including a wrong-sign falsification control and geometric dimensional scaling; full suite 55/55 passed locally.
- Literature context: exact Einstein-source conservation is guaranteed by the contracted Bianchi identity; recent warp-source papers continue to analyze stress-energy realizability/energy conditions, not demonstrate an engine.
- Next test: include the omitted translating-shape/nonlinear `v^2` terms and test the full x-momentum conservation equation numerically/analytically before addressing energy conservation.

## 2026-09-16 14:26 UTC — v0.3.7 translating-shape momentum gate

- Verified @GitHub main HEAD `f366a20cc565745028de5777a1acd910665f4c6d` and matched latest Library v0.3.6 before work; baseline 55/55 tests passed locally.
- Included the rigid-profile translation contribution to `partial_t j_x`. After the previously verified acceleration-order cancellation, the naive Cartesian partial balance leaves `R_naive=v^2 partial_x(f_yy+f_zz)/(16 pi)`.
- For a localized Gaussian this residual is locally nonzero, even in velocity, scales as `v^2 L^-3`, and integrates to zero as a boundary term. This falsifies extending the acceleration-only equation `partial_t j_x+partial_j S_xj=0` as the complete nonlinear conservation law.
- Interpretation: the missing shift/advection/connection terms of covariant/ADM stress-energy conservation must be included. The residual is not evidence of thrust.
- Added four regression/falsification tests; full local suite 59/59 passed. No experimental, peer-review or independent-replication claim.
- Next: derive the full spatial projection of `nabla_mu T^{mu nu}=0` in the repository's lapse/shift/sign convention and show explicitly whether the `v^2` residual is cancelled by shift/advection/connection terms.

## 2026-09-16 15:30 UTC — v0.3.8 exact covariant x-momentum gate
Derived the exact mixed-index conservative x projection. Independent symbolic Einstein-tensor calculation gives `partial_mu T^mu_x = (1/2)T^{ab} partial_x g_ab = v^2 f_x(f_yy+f_zz)/(16 pi)`. For a Gaussian, this differs from the v0.3.7 truncated residual by a factor `f`; exact terms cancel pointwise covariantly and integrate to zero. No reaction thrust found. Full reconstructed suite: 64 tests pass.

## 2026-09-16 16:26 UTC — v0.3.9 Gaussian Eulerian energy-budget gate
Starting verified GitHub main `18dbaf18fe4de853457736625e213fc8da5a8801` and v0.3.8 Library snapshot. Integrated the exact Hamiltonian-constraint Eulerian energy density for `f=exp(-r^2/sigma^2)`: `E_total=-v^2 sqrt(pi) sigma/(32 sqrt(2))` in geometric units. Requirement is nonpositive, even in velocity reversal, quadratic in speed and linear in Gaussian scale. Independent cylindrical quadrature agrees. This quantifies the global source-energy requirement but does not yet derive the full local Eulerian energy-flux/work projection.

## 2026-09-16 17:30 UTC — v0.3.10 exact Eulerian energy closure
From verified v0.3.9 scientific handoff (with later additive documentation backfill on main), independently reconstructed the Einstein tensor and derived `(partial_t-L_beta)E + D_i j^i = K E + K_ij S^ij` for rigid translation. `D_i j^i=0` and both remaining sides equal `-v^3(f_y f_xy+f_z f_xz)(f-1)/(16 pi)`. Gaussian local redistribution is odd in x and integrates to zero; total Eulerian energy is constant at fixed v. Five tests added; full Library-derived suite 74/74 passed locally in 0.443 s. No source construction or thrust. See `research/sessions/2026-09-16-1730-UTC.md`.

## 2026-09-16 17:30 UTC — v0.3.10 exact Eulerian energy closure
Exact rigid-translation Eulerian energy projection closes pointwise; local Gaussian redistribution is odd and integrates to zero. Five tests added; 74/74 local tests reported. PR #9 CI later verified successful. No constitutive source or propulsion mechanism.

## 2026-09-16 18:29 UTC — v0.3.11 acceleration-dependent integrated energy derivative
For fixed Gaussian scale, differentiated v0.3.9 source inventory to obtain `dE_total/dt=-v a sqrt(pi) sigma/(16 sqrt(2))`. Independent centered finite difference agrees. Five tests added; full reconstructed suite 79/79 passed locally. This is an effective source-inventory derivative, not demonstrated actuator/wall-plug power. Next: derive and integrate exact local acceleration-linear Eulerian energy terms.

## 2026-09-16 19:26 UTC — v0.3.12 local acceleration-energy closure
Starting from v0.3.11 Library/GitHub branch lineage, isolated terms linear in `a=dv/dt` in the exact Eulerian energy projection. `(partial_t E)_a=-v a(f_y^2+f_z^2)/(16 pi)` and the established acceleration shear stresses give `(K_ij S^ij)_a` exactly equal pointwise. Gaussian integration reproduces v0.3.11 `dE_total/dt=-v a sqrt(pi) sigma/(16 sqrt(2))`. Five tests added; full reconstructed suite 84/84 passed locally in 0.696 s. This closes acceleration-linear source bookkeeping but does not identify actuator power, a constitutive source, or thrust.

## 2026-09-16 20:27 UTC — v0.3.14 photon-reaction calibration baseline
Established an explicit open-system photon momentum baseline: F=P/c for emitted/absorbed photon momentum and up to 2P/c for ideal reflection on an externally supported mirror. Ideal 1 kW reflection is 6.671 microN. Defined a >=5 sigma photon-pressure calibration and force/power-slope agreement gate before unconventional thrust claims. Fresh reconstructed suite after six new tests: 90/90 passed in 0.457 s. Known physics only; no novel propulsion claim.

## 2026-09-16 21:29 UTC — v0.3.15
Established a pressure-matched reaction-mass thrust baseline, explicit external momentum boundary, reference 1 mN numerical case, artifact controls, and photon-pressure comparison. Full reconstructed suite 95/95 passed. See `research/sessions/2026-09-16-2129-UTC.md`.

## 2026-09-17 01:27 UTC — v0.3.19 thrust-stand artifact-floor eligibility gate
From verified GitHub main plus the unmerged stack through PR #16 and independently listed/read Library v0.3.18, defined `F_MDT=B_art+5 sigma_art`, with independent random null terms in quadrature and unknown-sign systematic thermal/EM/cable/airflow bounds added absolutely. Instrument eligibility additionally requires MDT below the weakest 0.1 mN calibrated reference. Synthetic example: sigma=5 microN, B=10 microN -> MDT=35 microN. No hardware or measured thrust. See session `research/sessions/2026-09-17-0127-UTC.md`.
