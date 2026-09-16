# Covariant dust flux in the prescribed 1+1 shift geometry

**Status:** DERIVED-CONDITIONAL. This is a kinematic fixed-background calculation, not a source solution of Einstein's equations and not a propulsion mechanism.

Use geometric units `c=1` and

\[ds^2=-dt^2+(dx-\beta\,dt)^2,\qquad \beta(t,x)=v_s f(x-v_st).\]

The metric components are `g_tt=beta^2-1`, `g_tx=-beta`, `g_xx=1`; `det(g)=-1`. The unit future Eulerian normal is

\[n^\mu=(1,\beta),\qquad n_\mu=(-1,0).\]

The earlier modeled dust congruence is exactly `u^mu=n^mu`, so for rest energy density `epsilon` its stress-energy is

\[T^{\mu\nu}=\epsilon n^\mu n^\nu
=\epsilon\begin{pmatrix}1&\beta\\\beta&\beta^2\end{pmatrix}.\]

## Observer-explicit energy and momentum

For the Eulerian observer `n^mu`,

\[E=T_{\mu\nu}n^\mu n^\nu=\epsilon,\qquad
j_\mu=-\gamma_{\mu\alpha}T^{\alpha\beta}n_\beta=0.\]

Thus the dust has **zero local 3-momentum in the Eulerian orthonormal frame**. The coordinate component `T^{tx}=epsilon beta` is not by itself a locally measured thrust flux; it is the coordinate representation of the moving Eulerian congruence.

## Covariant conservation gate

Dust conservation requires

\[\nabla_\mu T^{\mu\nu}=u^\nu\nabla_\mu(\epsilon u^\mu)+\epsilon u^\mu\nabla_\mu u^\nu=0.\]

For this unit-lapse ADM form, `n_mu=-partial_mu t`, and the Eulerian acceleration is `a_mu=D_mu ln(alpha)=0` because `alpha=1`. Hence `n^mu` is geodesic. Since `sqrt(-g)=1`, mass/energy continuity is

\[\nabla_\mu(\epsilon n^\mu)=\partial_t\epsilon+\partial_x(\epsilon\beta)=0,\]

which is exactly the finite-time continuity equation already solved. Therefore the prescribed Eulerian dust tensor is covariantly conserved **as test matter on this fixed 1+1 geometry** whenever that continuity equation holds.

This does **not** show the metric is sourced by that dust. A self-consistent GR model must separately satisfy `G_{mu nu}=8 pi G T_{mu nu}` (with restored powers of `c`). In 1+1 Einstein gravity the Einstein tensor is identically zero, so this reduced metric cannot determine a physical 3+1 source budget. The 1+1 calculation is only a transport/observer bookkeeping check.

## Flux through surfaces

For a constant-`x` worldline, the coordinate energy-current crossing rate associated with `J^mu=-T^{mu nu}n_nu=epsilon n^mu` has spatial component

\[J^x=\epsilon\beta.\]

For a moving constant-`xi=x-v_s t` boundary, conservation over a moving interval gives the relative current

\[J^x-v_sJ^t=\epsilon(\beta-v_s)=\epsilon v_s(f-1).\]

Using the finite-time invariant,

\[\epsilon(t)[1-f(t)]=\epsilon_0[1-f_0],\]

so along a characteristic this relative flux equals

\[-v_s\epsilon(t)(1-f_t)=-v_s\epsilon_0(1-f_0).\]

This is a conservation identity for test dust crossing a moving coordinate boundary, not force on the boundary. A mechanical momentum exchange requires a material interaction, pressure/stress, non-geodesic forcing, or a dynamical field/source sector. None is present here.

## Falsifiable conclusion

Within the exact assumptions of the v0.2.0 toy model, the proposed dust itself supplies no local Eulerian momentum density and needs no non-gravitational 4-force: it follows the prescribed geodesic Eulerian congruence. Therefore this model cannot yet provide a reaction force or propulsion mechanism. Any claim of propulsion must add and account for the physical source that creates/changes the 3+1 geometry, or an explicit interaction that transfers momentum to matter/fields, and close the global energy-momentum budget.

## Literature context

- Alcubierre (1994), *The warp drive: hyper-fast travel within general relativity*, DOI 10.1088/0264-9381/11/5/001.
- Bobrick & Martire (2021), *Introducing physical warp drives*, DOI 10.1088/1361-6382/abdf6e.

No literature novelty is claimed for this derivation.
