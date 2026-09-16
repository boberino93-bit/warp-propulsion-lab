# Translating-shape gate for complete x-momentum conservation

**Status: conditional diagnostic, not a complete conservation derivation.** Geometric units `G=c=1`.

The momentum constraint used through v0.3.6 is `j_x=-v(f_yy+f_zz)/(16 pi)`. For a rigid profile `f(x-x_s(t),y,z)`, `partial_t f=-v f_x`, hence `partial_t j_x=-a(f_yy+f_zz)/(16 pi)+v^2 partial_x(f_yy+f_zz)/(16 pi)`.

v0.3.6 showed the acceleration term cancels the acceleration-dependent stress divergence. If one incorrectly promotes the remaining law to the flat Cartesian expression `partial_t j_x+partial_j S_xj=0`, the translating profile leaves `R_naive=v^2 partial_x(f_yy+f_zz)/(16 pi)`.

For a Gaussian this is locally nonzero but integrates to a boundary term that vanishes for a localized profile. Thus the simple partial-derivative equation cannot be the complete nonlinear ADM momentum law. Shift/advection and spacetime-connection terms in the covariant conservation projection must be retained. A nonzero `R_naive` is a bookkeeping warning, **not reaction thrust**.
