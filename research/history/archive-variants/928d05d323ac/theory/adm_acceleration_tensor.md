# Acceleration-only spatial stress tensor

**Status:** DERIVED-CONDITIONAL. Fixed prescribed Alcubierre geometry; not a material source model or engine.

Use geometric units, unit lapse, flat spatial metric and `beta_x=-v(t) f`. With the repository convention,

`K_ij = -v/2 (delta_ix f_j + delta_jx f_i)`.

Only `partial_t K_ij` contains the coordinate acceleration `a=dv/dt`; the acceleration-only part is

`A_ij = -a/2 (delta_ix f_j + delta_jx f_i)`.

The ADM evolution source term is `-8 pi [S_ij - 1/2 delta_ij(S-E)]`. The Hamiltonian constraint contains no acceleration-only term, so `E_acc=0`. Taking the trace reproduces the previous result `S_acc=-a f_x/(4 pi)`. Solving componentwise gives

- `S_xx,acc = 0`
- `S_yy,acc = S_zz,acc = -a f_x/(8 pi)`
- `S_xy,acc = a f_y/(16 pi)`
- `S_xz,acc = a f_z/(16 pi)`
- `S_yz,acc = 0`.

The exact cancellation in `S_xx,acc` is a stronger negative result than the trace alone: acceleration does not require a direct longitudinal normal stress in this slicing, but does require transverse normal stresses and longitudinal-transverse shear.

The coordinate stress-divergence channel along x is

`partial_j S_xj,acc = a(f_yy+f_zz)/(16 pi)`

for spatially uniform `a`. Its all-space integral vanishes for smooth localized `f` because it is a boundary term. A nonlocalized profile can retain boundary force, which is external momentum exchange rather than reactionless thrust.

This calculation is slicing/source-decomposition dependent and is not by itself a complete covariant force law. A realizable source must still satisfy stress-energy conservation and include whatever fields/matter create the metric.
