# Acceleration-linear Eulerian energy closure

For lapse 1, flat spatial metric, shift `beta_x=-v(t) f`, and the repository ADM convention,
`E=-v^2(f_y^2+f_z^2)/(32 pi)`.  Isolate only terms linear in `a=dv/dt` in
`(partial_t-L_beta)E + D_i j^i = K E + K_ij S^ij`.

At fixed spatial coordinates, neither `L_beta E`, `D_i j^i`, nor `K E` contains an explicit acceleration term. Thus
`(partial_t E)_a=-v a (f_y^2+f_z^2)/(16 pi)`.

Using `K_xy=-v f_y/2`, `K_xz=-v f_z/2` and the established acceleration stresses
`S_xy=a f_y/(16 pi)`, `S_xz=a f_z/(16 pi)` (with `S_xx=0`), tensor contraction counts symmetric off-diagonal terms twice:
`(K_ij S^ij)_a=2 K_xy S_xy+2 K_xz S_xz=-v a(f_y^2+f_z^2)/(16 pi)`.
Hence the acceleration-linear energy equation closes pointwise.

For `f=exp(-r^2/sigma^2)`, the established integral of `f_y^2+f_z^2` is `pi^(3/2) sigma/sqrt(2)`, giving
`Integral (partial_t E)_a d^3x=-v a sqrt(pi) sigma/(16 sqrt(2))`, exactly the v0.3.11 derivative of total Eulerian source energy.

This is prescribed-geometry source bookkeeping. It does not identify wall-plug power, a material source, reaction reservoir, or propulsion mechanism.
