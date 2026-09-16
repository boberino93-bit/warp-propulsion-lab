# Acceleration-linear Eulerian energy closure

For lapse 1, flat spatial metric, shift `beta_x=-v(t) f`, and the repository ADM convention, `E=-v^2(f_y^2+f_z^2)/(32 pi)`. Isolate terms linear in `a=dv/dt` in `(partial_t-L_beta)E + D_i j^i = K E + K_ij S^ij`.

At fixed spatial coordinates, neither `L_beta E`, `D_i j^i`, nor `K E` contains an explicit acceleration term, so `(partial_t E)_a=-v a(f_y^2+f_z^2)/(16 pi)`.

Using `K_xy=-v f_y/2`, `K_xz=-v f_z/2`, `S_xy=a f_y/(16 pi)`, and `S_xz=a f_z/(16 pi)`, symmetric off-diagonal contraction gives `(K_ij S^ij)_a=2K_xyS_xy+2K_xzS_xz=-v a(f_y^2+f_z^2)/(16 pi)`. Thus the acceleration-linear energy equation closes pointwise.

For `f=exp(-r^2/sigma^2)`, the established integral of `f_y^2+f_z^2` is `pi^(3/2) sigma/sqrt(2)`, yielding `Integral (partial_t E)_a d^3x=-v a sqrt(pi) sigma/(16 sqrt(2))`, exactly the v0.3.11 derivative of total Eulerian source energy.

This is prescribed-geometry source bookkeeping, not wall-plug power, a material source, reaction reservoir, or propulsion mechanism.
