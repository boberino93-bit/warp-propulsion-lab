# 1+1D prescribed shift: a conditional steady-dust result

Take a slice through a prescribed Alcubierre-type line element with lapse 1 (c=1 in the geometry):

\[ds^2=-dt^2+[dx-v_s f(x-v_s t)dt]^2.\]

For the Eulerian observers normal to constant-t slices, the coordinate velocity is \(dx/dt=v_s f\). This is **a specified congruence**, not a proof that arbitrary initially resting material follows it or that the Einstein equations admit the prescribed source. Assume number/rest-mass current \(J^\mu=\rho n^\mu\), no pressure, no transverse motion, no backreaction, and \(\sqrt{-g}=1\) in c=1 units. Then

\[\nabla_\mu J^\mu=0\quad\Rightarrow\quad\partial_t\rho+\partial_x(\rho v_s f)=0.\]

For constant \(v_s\ne0\) and steady \(\rho=\rho(\xi)\) with \(\xi=x-v_s t\):

\[\frac{d}{d\xi}\{\rho v_s(f-1)\}=0.\]

Use upstream boundary \(f\to0\), \(\rho\to\rho_0\). Flux equals \(-v_s\rho_0\), so:

\[\boxed{\rho(\xi)=\rho_0/[1-f(\xi)]},\qquad f<1.\]

The SI version of the continuity equation is the same when v_s is expressed in m/s and rho in kg/m^3; using the c=1 line element with SI coordinates requires replacing dt appropriately (e.g. c dt in the lapse term). Flux has units kg/(m^2 s). Dimensional analysis alone does not verify physical applicability.

**Critical limitations:** the exact f=1 interior cannot support a finite steady density with nonzero upstream flux; f approaching 1 signals a failure of global steady assumptions or indefinite accumulation, NOT an established infinite physical density. Finite-time characteristic evolution, pressure, shock, fluid sound speed, off-axis flow, and metric source/backreaction are unresolved. The defined tanh top-hat has f_max=tanh(R/w)<1, so numerical examples may produce large finite model densities, strongly dependent on R/w. Density is measured for the particular Eulerian observer field, not an invariant concentration independent of frame.

**Checks:** substitute expression into flux; flux is a constant \(-v_s \rho_0\), hence residual zero analytically. With f=0 recover rho=rho0. With v_s=0 the division by speed in the derivation is invalid and only rho independent of time follows from continuity. Tests verify identities for subluminal toy parameters but cannot demonstrate GR source realism.
