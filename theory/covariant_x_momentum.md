# Exact covariant x-momentum gate for rigid translation

For the repository convention `ds^2=-dt^2+(dx-v f dt)^2+dy^2+dz^2`, `det(g)=-1`. The exact mixed-index identity is

`nabla_mu T^mu_x = partial_mu T^mu_x - (1/2) T^{ab} partial_x g_ab = 0`.

An independent symbolic calculation constructs the metric, inverse, Christoffels, Ricci tensor, Einstein tensor, raises indices, and simplifies both terms. For rigid `f(x-vt,y,z)` it gives, before division by `8 pi`,

`partial_mu G^mu_x = (v^2/2) f_x (f_yy+f_zz)`

and

`(1/2) G^{ab} partial_x g_ab = (v^2/2) f_x (f_yy+f_zz)`.

They cancel pointwise in the covariant divergence. In stress-energy units each side is `v^2 f_x(f_yy+f_zz)/(16 pi)`.

For a Gaussian on the x-axis this is `v^2 x f^2/(2 pi sigma^4)`. The deliberately truncated v0.3.7 residual was `v^2 x f/(2 pi sigma^4)`: they differ by a factor `f`. Therefore the v0.3.7 residual cannot be interpreted as the missing connection term or as thrust; it mixed an incomplete ADM partial balance with a different conservative projection. Both exact sides are odd and integrate to zero for a localized symmetric profile.

This is a fixed-geometry identity, not a constitutive source model or engine.
