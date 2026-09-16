# Finite-time 1-D characteristics: extension of the prescribed-shift dust toy

**Status:** DERIVED-CONDITIONAL and COMPUTATION-VERIFIED (limited tests). This is **not** a full relativistic hydrodynamic model or evidence of an engine. Source snapshot: project v0.1.0. Implementation: `src/transient_dust.py`; tests: `tests/test_transient_dust.py`.

## Inputs and spacetime

The old model prescribes, with `c=1` in the geometry, 

\[ ds^2=-dt^2+[dx-v_s f(\xi)dt]^2, \qquad \xi=x-v_st. \]

Only the Eulerian congruence is modeled, `dx/dt=v_s f`. For an initial uniform **Eulerian-frame** rest-mass density at lab time `t=0`, `rho(x,0)=rho_0>0`, with no pressure or transverse motion and no backreaction, the continuity equation is

\[\partial_t\rho+\partial_x(\rho v_s f)=0.\]

It is a kinematic transport equation of a **prescribed**, idealized flow. In SI, `x` and `xi` are metres, `v_s` is m/s, time is seconds, density is kg/m³, and `f` is dimensionless; the lapse term of the 1+1 line element must be written with appropriate factors of `c` when using SI coordinates.

## Time-dependent initial-value solution

Let `xi_0` label a parcel's location at `t=0`, with `xi(t=0)=xi_0`. A time-dependent method of characteristics gives:

\[\dot\xi=v_s[f(\xi)-1],\qquad \frac{d\log\rho}{dt}=-v_s f'(\xi).\]

The flow-map Jacobian `J = partial xi(t;xi_0)/partial xi_0` obeys

\[\dot J=v_s f'(\xi)J,\qquad J(0)=1,\qquad \rho(t)=\rho_0/J(t).\]

There is also a **separate analytic invariant** along each characteristic whenever `f<1`:

\[\rho(t)[1-f(\xi(t))]=\rho_0[1-f(\xi_0)].\]

Thus the exact characteristic relation is

\[\boxed{\rho(t)=\rho_0\frac{1-f(\xi_0)}{1-f(\xi(t))}}.\]

Crucially, the old `rho_0/[1-f(xi)]` **steady** profile is recovered along a parcel only when its initial shape is negligible (`f(xi_0) ~= 0`), *not* for a uniformly populated bubble at the initial instant. `rho_0` in the steady formula is an upstream boundary value; `rho_0` in this initial-value setup is the uniform initial Eulerian density. Their numerical values can coincide while their physical conditions differ.

For the sample `v_s=100 m/s`, `R=5 m`, `w=2 m`, `rho_0=1.225 kg/m³`, `t=0.03 s`:

- Leading-side initial `xi_0=+8 m`: final `xi=+5.53552944 m`, density `1.84988746 kg/m³` (initial `1.225`), a model-conditional density increase.
- Trailing-side `xi_0=-8 m`: density `1.16993816 kg/m³`, a model-conditional density decrease.
- Initially at center `xi_0=0 m`: density `1.22403217 kg/m³`, *not* the old steady center estimate `~91.5 kg/m³`. The initial condition matters dramatically.

These are densities for the specific Eulerian congruence in a fixed test geometry; there is no equation of state, pressure, acoustic response, curvature-source model, energy deposition, material boundary or thrust computation.

## Reproducible checks and scope

The solver integrates `xi` and `log(J)` as **two coupled ODEs** using fourth-order Runge–Kutta. Checks include gradient against a finite difference, analytic density invariant, density × Jacobian, reversal of the time step, zero-speed limit, step refinement, and a separately quadrature-integrated mass for a deformed material interval. On `[-12,12] m`, `t=0.03 s`, the 241-sample trapezoidal result was `29.4011058969 kg/m²` against initial `29.4000000000 kg/m²` (relative quadrature error `3.76e-5`); this is an integration-discretization check, **not** an observed measurement. Automated mass test requires error < `5e-5` relative and improvement when spatial samples double.

These checks verify internal code/continuity consistency, **not** that a metric is dynamically realizable or that any fluid or solid responds this way. For `f=1` the invariant cannot be divided by `1-f`; the old stationary nonzero-throughput solution does not exist as a finite density there. A smooth `f<1` finite-time calculation avoids that division but does not resolve pressure, three-dimensional escape, late-time accumulation, or a full stress-energy budget. No claim of a universal singularity, decoupling, transmedium propulsion or UAP explanation follows.

## Connection to primary propulsion goal

The calculation supplies a countercheck to the claim that *prescribing* a moving geometry automatically allows silent passage through matter: even a particular allowed test-dust congruence can show density variation. It **does not** compute mechanical pressure, drag, energy transfer, self-consistent geometry or a momentum-exchange propulsion mechanism. The *next* technical gate is deriving covariant stress-energy/energy and momentum flux in this prescribed metric with clear boundary conditions, before attributing fluid forces or thrust to it.

## Scientific context

- Alcubierre (1994): https://doi.org/10.1088/0264-9381/11/5/001 — prescribed geometry and exotic source requirements.
- McMonigal, Lewis, O'Byrne (2012): https://doi.org/10.1103/PhysRevD.85.064024 — test-particle/geodesic interactions; not full hydrodynamics.
- Bobrick & Martire (2021): https://doi.org/10.1088/1361-6382/abdf6e — physical warp-drive definitions and explicit conclusion that warp shells require propulsion.

The characteristic equations here are an original calculation within the stated toy assumptions, not a claim of literature novelty; no line-by-line novelty review was performed.
