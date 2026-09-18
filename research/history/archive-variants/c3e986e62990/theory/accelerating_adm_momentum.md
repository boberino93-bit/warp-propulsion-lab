# Accelerating bubble: what the ADM momentum constraint can and cannot say

**Status: DERIVED-CONDITIONAL.** Fixed prescribed Alcubierre geometry; not a realizable source model or engine.

Take lapse `alpha=1`, flat spatial metric, and shift `beta_x=-v(t) f(x-x_s(t),y,z)`. On each spatial slice,

`K_ij=(D_i beta_j+D_j beta_i)/2`.

Because the ADM momentum constraint `D_j(K^{ij}-gamma^{ij}K)=8 pi S^i` contains spatial derivatives of the instantaneous extrinsic curvature, its source momentum density is exactly the stationary formula with `v -> v(t)`:

- `S_x=-v(t)(f_yy+f_zz)/(16 pi)`
- `S_y= v(t) f_xy/(16 pi)`
- `S_z= v(t) f_xz/(16 pi)`

under the repository's declared sign convention. There is **no explicit `dv/dt` term in this constraint**. For a smooth localized shape, every volume integral remains a boundary derivative and vanishes when derivatives vanish at infinity, even on an accelerating slice.

This is a useful negative result, but it does **not** prove acceleration costs no momentum or energy. Acceleration enters time derivatives of the geometry and therefore the ADM evolution equations / required spatial stresses and fluxes. Those terms are the next closure gate.

Primary grounding: Alcubierre (1994), DOI 10.1088/0264-9381/11/5/001. McMonigal, Lewis & O'Byrne (2012), DOI 10.1103/PhysRevD.85.064024, explicitly study variable-velocity bubble/test-particle interactions but do not supply a realizable geometry-generating source.
