# Acceleration-only spatial stress tensor

**Status:** DERIVED-CONDITIONAL. Fixed prescribed Alcubierre geometry; not a material source model or engine.

Use geometric units, unit lapse, flat spatial metric and `beta_x=-v(t) f`. With the repository convention, `K_ij=-v/2(delta_ix f_j+delta_jx f_i)`. The acceleration-only part of `partial_t K_ij` is `A_ij=-a/2(delta_ix f_j+delta_jx f_i)`.

The ADM evolution source term is `-8 pi[S_ij-1/2 delta_ij(S-E)]`. The Hamiltonian constraint has no acceleration-only term, so `E_acc=0`. Taking the trace reproduces `S_acc=-a f_x/(4 pi)`. Solving componentwise gives:

- `S_xx,acc=0`
- `S_yy,acc=S_zz,acc=-a f_x/(8 pi)`
- `S_xy,acc=a f_y/(16 pi)`
- `S_xz,acc=a f_z/(16 pi)`
- `S_yz,acc=0`.

The exact `S_xx,acc` cancellation is stronger than the trace alone: acceleration requires transverse normal stresses and longitudinal-transverse shear, but no direct longitudinal normal stress in this slicing.

For spatially uniform `a`, `partial_j S_xj,acc=a(f_yy+f_zz)/(16 pi)`. Its all-space integral vanishes for smooth localized `f` as a boundary term. A nonlocalized profile can retain boundary force, which represents external momentum exchange rather than reactionless thrust.

This source decomposition is slicing dependent and is not itself a covariant total-force law. A realizable source must satisfy stress-energy conservation and include the fields/matter that generate the geometry.
