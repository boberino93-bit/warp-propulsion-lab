# Corrections and open review flags (append-only)

- E001 — Earlier conversational claim that matter must form pressure pulses/shocks in water: **not derived** from the metric; depends on material stress-energy, initial/boundary conditions, and specified geometry. Treat as speculation.
- E002 — rho=rho0/(1-f) from a special 1D stationary continuity equation was previously described too broadly. It applies only to an Eulerian dust current, constant nonzero bubble speed, prescribed shift, uniform upstream rest density, and a valid steady-state solution. It is ill-defined at f=1; finite-time and transverse dynamics must be solved separately.
- E003 — Earlier conventional drag/power estimate near 19 km/s was a crude dimensional estimate and may not equal deposited power; cannot infer a physical warp-medium power coupling from that estimate.
- E004 — No experimentally established UAP propulsion, warp metric source, or causal link to nuclear electronics disruptions. They cannot be used as validated model inputs.
- E005 — Automated self-review is not independent peer review; hourly sessions may lack file-write continuity. Persist results manually in snapshots and do not pretend hourly changes reached this Git repository automatically.

- E006 — **Initial vs boundary condition correction (2026-09-16):** the earlier `rho0/(1-f)` formula is a special steady flow with a distant upstream boundary, *not* the solution everywhere after specifying uniform `rho(x,0)=rho0`. Finite-time characteristic density is `rho(t)=rho_initial(xi0)[1-f(xi0)]/[1-f(xi(t))]` for `f<1` and the specified Eulerian dust congruence. Earlier claims about immediate huge center densities from uniform initial matter were unsupported. Code/tests and session log added; still no pressure or GR backreaction.
- E007 — **Remote publishing not verified (2026-09-16):** GitHub connector rejected access in this session. No remote commit, PR or remote CI run occurred. Canonical progress resides in the v0.2.0 Library snapshot until an accessible repository is confirmed.
- E008 — **Coordinate flux is not local thrust (2026-09-16):** `T^{tx}=epsilon beta` / `J^x=epsilon beta` in the prescribed shift coordinates must not be interpreted as Eulerian locally measured momentum density. For the modeled congruence `u=n`, the Eulerian momentum density is zero. Relative current across constant-`xi` surfaces is a conservation/boundary-crossing quantity, not force on a vehicle.
- E009 — **Test matter is not the geometry source (2026-09-16):** showing `nabla_mu T^{mu nu}=0` for geodesic dust on the fixed 1+1 background does not satisfy the 3+1 Einstein equations or provide the stress-energy required to create the shift geometry. A source/field energy-momentum budget remains missing.

- E011 — Distinct v0.3.0 Library (24 tests) and remote interview (25 tests) trees were reconciled additively through GitHub PR #1; neither old count validates combined tree.
- E012 — Eulerian test-dust momentum zero is not the geometry source. 3+1 Hamiltonian constraint demands negative source energy where transverse gradients are nonzero; momentum/stress sources remain unknown.
- E013 — Initial ADM checkout lacked remote interview tests (28 passed); copied remote test verbatim and reran 32 tests successfully locally; GitHub CI requires separate confirmation.
- E014 — Premature PR creation produced HTTP 422; new research branch subsequently created from verified merge SHA. No main modification from failed attempts.

## 2026-09-16 09:29 UTC — GitHub connector disabled mid-run
Attempted required @GitHub main-HEAD inspection first; connector returned disabled before any repository read/write. No remote state, CI, branch, commit, PR or merge is claimed for v0.3.2. Continued from newest verified Library snapshot and saved non-overwriting Library artifacts. Remote reconciliation is mandatory next run before merging anything.

- E015 — **Accelerating-slice constraint scope (2026-09-16 10:30 UTC):** absence of explicit `dv/dt` from the ADM momentum constraint must not be described as zero acceleration cost or a complete conservation result. Acceleration can enter ADM evolution equations/spatial stresses and energy flux. First v0.3.3 numerical boundary-cancellation test used an unnecessarily tight finite-domain threshold and failed (`2.538e-4` vs `2e-4`); corrected by expanding the Gaussian integration domain, then reran the complete suite successfully.
- E016 — **GitHub unavailable again (2026-09-16 10:30 UTC):** required @GitHub initial read returned disabled. No remote HEAD, branch, commit, PR, CI or merge is claimed for v0.3.3; Library is the persistence target pending reconciliation.
- E015 — **v0.3.2/v0.3.3 remote persistence gap:** those sessions correctly recorded @GitHub as unavailable and were preserved only in Library at the time. On 2026-09-16 11:30 UTC GitHub access recovered; main was independently verified at `d39625d57826f65e386a9470e8b259a68b659661`. The newer Library lineage is being reconciled through a branch/PR rather than overwriting main. Historical no-remote-success statements remain valid for their original sessions.

## 2026-09-16 12:27 UTC — no derivation/test correction required

- No failing regression in this bounded advance. Sign convention was constrained by requiring the tensor trace to reproduce the independently tested v0.3.4 trace source term before interpreting components.
- Reminder: `partial_j S_ij` in this slicing is not by itself a covariant total force. It is used only as a boundary/momentum-accounting diagnostic; full stress-energy conservation remains the next gate.

## 2026-09-16 13:30 UTC — conservation scope guard
- Potential error avoided: treating the acceleration-only decomposition as the complete covariant conservation law. The new identity checks only terms proportional to `a=dv/dt`; `v^2` translation/advection terms and energy conservation remain untested.
- Falsification control: reversing the derived stress-divergence sign produces a nonzero residual, so the cancellation is sign-sensitive rather than hard-coded as zero.

## 2026-09-16 14:26 UTC — scope correction to acceleration-order conservation equation
The v0.3.6 expression `partial_t j_x + partial_j S_xj=0` was intentionally an acceleration-order isolation. v0.3.7 confirms it cannot be used as the complete nonlinear ADM/covariant momentum equation: rigid translation leaves a local `v^2 partial_x(f_yy+f_zz)/(16 pi)` residual. Required correction is to retain the full shift/advection/connection terms before interpreting any nonlinear residual physically.

## 2026-09-16 15:30 UTC — projection mismatch correction
v0.3.7's residual was intentionally labeled incomplete. v0.3.8 independently shows it is **not** equal to the exact connection/source term: on the Gaussian x-axis exact/naive = `f`. Cause: the truncated ADM partial balance and exact mixed-index conservative projection use different bookkeeping variables. Do not cancel them term-for-term or interpret either local term as thrust.

## 2026-09-16 16:26 UTC — Gaussian scale is not independent wall thickness
v0.3.9 uses a self-similar Gaussian with one length `sigma`; its integrated energy scales as `sigma`. Do not generalize this to thin-wall top-hat profiles, where radius and wall thickness are independent and the scaling differs. The full Eulerian flux/work identity remains open.

## 2026-09-16 17:30 UTC — constant-speed energy/power interpretation
v0.3.9 established a nonzero negative integrated Eulerian source-energy inventory. Do **not** equate that inventory with continuous power consumption at constant rigid-translation speed. v0.3.10's exact Eulerian projection has nonzero local work/redistribution but its localized symmetric Gaussian integral vanishes and total Eulerian energy is time-independent at fixed v. Acceleration-dependent power remains uncalculated and is the next test.

## 2026-09-16 18:29 UTC — acceleration power interpretation guard
Do not identify `dE_total/dt` for the prescribed Gaussian metric with physical wall-plug or actuator power until a constitutive source/control model is supplied. PR #9 CI, previously only queued, was verified successful in run 35128839518; PR #9 remains unmerged because the merge action was blocked by the connector safety layer.
