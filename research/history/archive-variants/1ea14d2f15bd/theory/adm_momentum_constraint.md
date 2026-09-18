# Alcubierre ADM momentum-constraint source

**Status: DERIVED-CONDITIONAL.** This is the source momentum density required by a prescribed geometry, not a material model or propulsion mechanism.

Use geometric units `G=c=1`, spatial metric `gamma_ij=delta_ij`, lapse `alpha=1`, and

`ds^2=-dt^2+(dx-v f dt)^2+dy^2+dz^2`, so `beta_x=-v f`.

With convention `K_ij=(D_i beta_j+D_j beta_i)/2`, the nonzero components are `K_xx=-v f_x`, `K_xy=-v f_y/2`, `K_xz=-v f_z/2`, and `K=-v f_x`. The momentum constraint

`D_j(K^{ij}-gamma^{ij}K)=8 pi S^i`

gives

`S_x = -v(f_yy+f_zz)/(16 pi)`,
`S_y =  v f_xy/(16 pi)`,
`S_z =  v f_xz/(16 pi)`.

If the opposite sign convention for `K_ij` is adopted, every `S_i` flips sign. The physically important results here do not: the source momentum is locally nonzero, scales linearly with bubble velocity, depends on second spatial derivatives, and integrates to zero for a smooth localized profile when derivative boundary terms vanish.

For example, `integral S_x d^3x` is proportional to `-integral (f_yy+f_zz)d^3x`; integration by parts converts this to transverse derivative terms at infinity. `S_y` and `S_z` similarly reduce to boundary terms. Thus this constraint does not reveal a hidden net reaction momentum for an isolated localized prescribed bubble. It instead specifies a distributed local momentum requirement whose material/field realization remains unknown.

Dimensional audit: in geometric units `v/c` is dimensionless and second derivatives of `f` have units `L^-2`, hence `S_i` has `L^-2`, as does geometric stress-energy. Restoring SI stress-energy requires the Einstein-equation conversion factor and a declared momentum-density convention; that conversion is deliberately deferred rather than risk mixing energy density, momentum density and momentum flux units.

The numerical regression test uses a Gaussian profile and verifies the local formula, linear speed scaling, parity cancellation, and convergence of the volume-integrated `S_x` toward zero as the integration domain expands.
