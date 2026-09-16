# Research log (append-only)

## 2026-09-16 UTC — v0.1.0 first reproducible scaffold

- Primary objective clarified: functioning propulsion, not just geometry. Authorship/creative origin documented, pending public-attribution preference.
- Grounding sources: Alcubierre (1994), McMonigal et al. (2012), Bobrick & Martire (2021). See references.
- Recast 1D density expression as an explicitly conditional **steady dust continuity solution**. It is not a universal warp-medium prediction, not a proof of a singularity or a working mechanism.
- Added minimal pure-Python source code, numeric identity tests and conventional momentum/energy baseline. Numerical code not run at time of this entry; test results should be appended after execution.
- No external repository published, no expert peer review, no experimental results, no GR solver, no working propulsion mechanism.

### Update protocol
Append a dated entry for every substantive iteration including (a) source/version, (b) new result, (c) independent checks, (d) mistakes/corrections, (e) unsupported leaps rejected, and (f) next falsifiable test. Never retroactively rewrite errors out of history; add a correction.

## 2026-09-16 15:30 UTC — v0.3.8 exact covariant x-momentum gate
Derived the exact mixed-index conservative x projection. Independent symbolic Einstein-tensor calculation gives `partial_mu T^mu_x = (1/2)T^{ab} partial_x g_ab = v^2 f_x(f_yy+f_zz)/(16 pi)`. For a Gaussian, this differs from the v0.3.7 truncated residual by a factor `f`; exact terms cancel pointwise covariantly and integrate to zero. No reaction thrust found. Full reconstructed suite: 64 tests pass. Detailed intermediate history remains preserved in versioned session files and Library snapshots; this remote cumulative log had not been updated after v0.3.1 and requires later historical backfill rather than fabricated reconstruction.
