# Corrections and open review flags (append-only)

- E001 — Earlier conversational claim that matter must form pressure pulses/shocks in water: **not derived** from the metric; depends on material stress-energy, initial/boundary conditions, and specified geometry. Treat as speculation.
- E002 — rho=rho0/(1-f) from a special 1D stationary continuity equation was previously described too broadly. It applies only to an Eulerian dust current, constant nonzero bubble speed, prescribed shift, uniform upstream rest density, and a valid steady-state solution. It is ill-defined at f=1; finite-time and transverse dynamics must be solved separately.
- E003 — Earlier conventional drag/power estimate near 19 km/s was a crude dimensional estimate and may not equal deposited power; cannot infer a physical warp-medium power coupling from that estimate.
- E004 — No experimentally established UAP propulsion, warp metric source, or causal link to nuclear electronics disruptions. They cannot be used as validated model inputs.
- E005 — Automated self-review is not independent peer review; hourly sessions may lack file-write continuity. Persist results manually in snapshots and do not pretend hourly changes reached this Git repository automatically.

- E006 — **Initial vs boundary condition correction (2026-09-16):** the earlier `rho0/(1-f)` formula is a special steady flow with a distant upstream boundary, *not* the solution everywhere after specifying uniform `rho(x,0)=rho0`. Finite-time characteristic density is `rho(t)=rho_initial(xi0)[1-f(xi0)]/[1-f(xi(t))]` for `f<1` and the specified Eulerian dust congruence. Earlier claims about immediate huge center densities from uniform initial matter were unsupported. Code/tests and session log added; still no pressure or GR backreaction.
- E007 — **Remote publishing not verified (2026-09-16):** GitHub connector rejected access in this session. No remote commit, PR or remote CI run occurred. Canonical progress resides in the v0.2.0 Library snapshot until an accessible repository is confirmed.

- E008 — 2026-09-16 08:23 UTC: video-review wording corrected. Complete supplied transcripts and sparse frames were reviewed, not continuous audio/video. Transcript completeness and numerical transcription accuracy remain unverified.
- E009 — Sonar 2500 m/25 s is 100 m/s average; 3000 mph peak requires additional history. Endpoint facts allow different peaks. Human impossibility / alien attribution does not follow from lack of a known demonstrated mechanism.
- E010 — E007 records a historical failure; archive import 23e3bace1b76638e0bebd65bdd4c33a2211ee75e was subsequently verified remotely. Prior history retained.
