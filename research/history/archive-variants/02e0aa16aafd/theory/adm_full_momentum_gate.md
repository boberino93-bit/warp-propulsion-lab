# Translating-shape gate for complete x-momentum conservation

**Status: conditional diagnostic, not a complete conservation derivation.** Geometric units `G=c=1`.

The momentum constraint used through v0.3.6 is

`j_x = -v (f_yy+f_zz)/(16 pi)`.

For a rigid profile `f(x-x_s(t),y,z)`, `partial_t f = -v f_x`. Therefore at a fixed coordinate point

`partial_t j_x = -a (f_yy+f_zz)/(16 pi) + v^2 partial_x(f_yy+f_zz)/(16 pi)`.

v0.3.6 showed that the first term is cancelled pointwise by the acceleration-dependent stress divergence. If one incorrectly assumes the remaining conservation law is the flat Cartesian expression `partial_t j_x + partial_j S_xj=0`, the omitted translating profile leaves

`R_naive = v^2 partial_x(f_yy+f_zz)/(16 pi)`.

For a Gaussian this is generically nonzero locally, even though its volume integral is a boundary term and vanishes for a localized profile. Thus the simple partial-derivative equation used to isolate acceleration order cannot be promoted to the complete nonlinear ADM momentum law. The shift/advection and spacetime-connection terms in `n_mu nabla_nu T^{mu nu}=0` / spatial projection must be retained. A nonzero `R_naive` is a bookkeeping warning, **not reaction thrust**.
