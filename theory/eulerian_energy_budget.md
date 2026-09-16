# Gaussian Eulerian source-energy budget

For the standard flat-slice Alcubierre metric used in this repository, the Hamiltonian constraint gives

`E = -v^2[(f_y)^2+(f_z)^2]/(32 pi)` in `G=c=1`.

For the localized Gaussian `f=exp[-(x^2+y^2+z^2)/sigma^2]`, direct integration over all space gives

`E_total = -v^2 sqrt(pi) sigma/(32 sqrt(2))`.

Thus this prescribed geometry requires nonpositive Eulerian energy wherever transverse wall gradients are present. The integrated requirement is even under velocity reversal, scales as `v^2`, and for this self-similar Gaussian family scales linearly with the length scale `sigma`. Since the Gaussian has no independent bubble-radius and wall-thickness parameters, this result must not be misreported as the thin-wall `R^2/delta` scaling of a top-hat-like Alcubierre profile.

Dimensional audit: in geometric units local `E` has dimension `L^-2`; `d^3x` gives integrated geometric energy dimension `L`. Restoring SI for a geometric integrated energy length uses `E_SI=(c^4/G) E_geom` (joules).

This is a source requirement of a prescribed metric, not evidence that such stress-energy can be constructed or that it provides propulsion.
