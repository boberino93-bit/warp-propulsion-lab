# Acceleration-order local momentum conservation

**Status: DERIVED-CONDITIONAL.** This is a leading acceleration-order consistency check on the prescribed Alcubierre source, not a complete nonlinear source model or propulsion mechanism.

Use the repository convention `ds^2=-dt^2+(dx-v(t)f dt)^2+dy^2+dz^2`, unit lapse and flat spatial metric. The momentum constraint gives `j_x=-v(f_yy+f_zz)/(16 pi)`.

At fixed spatial coordinates, differentiating the explicit velocity factor gives `(partial_t j_x)_a=-a(f_yy+f_zz)/(16 pi)`.

The v0.3.5 acceleration-only stress tensor has `S_xx=0`, `S_xy=a f_y/(16 pi)`, `S_xz=a f_z/(16 pi)`, hence `(partial_j S_xj)_a=+a(f_yy+f_zz)/(16 pi)`.

Therefore the acceleration-order local momentum conservation residual cancels pointwise: `(partial_t j_x)_a+(partial_j S_xj)_a=0`.

This is stronger than the previous all-space boundary cancellation: the local acceleration stress is exactly the momentum-flux channel required to change the geometry's local source momentum density at this order. It does **not** reveal an external reaction channel or net thrust. Instead, it closes the acceleration-only bookkeeping internally within the prescribed stress-energy distribution.

Scope warning: translating-shape terms proportional to `v^2`, nonlinear shift/advection terms, energy conservation, and a physical matter/field constitutive model are outside this bounded test. Full covariant `nabla_mu T^{mu nu}=0` follows from the Einstein tensor by the contracted Bianchi identity for an exact metric, but that identity alone does not show how realizable matter produces the required tensor.

Dimensional audit in geometric units: `j_x ~ L^-2`; coordinate time has dimension `L`, so `partial_t j_x ~ L^-3`. Since `a=dv/dt ~ L^-1` and `f_yy+f_zz ~ L^-2`, the derived terms scale as `L^-3`.
