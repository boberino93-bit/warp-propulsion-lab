# Acceleration-dependent integrated Eulerian source power

For the repository one-scale Gaussian `f=exp(-r^2/sigma^2)`, v0.3.9 established in geometric units

`E_total(v,sigma) = -v^2 sqrt(pi) sigma/(32 sqrt(2))`.

Holding `sigma` fixed and allowing `v=v(t)`, `a=dv/dt`, direct differentiation gives

`P_acc = dE_total/dt = -v a sqrt(pi) sigma/(16 sqrt(2))`.

This is the time derivative of the prescribed metric's integrated Eulerian source-energy inventory. It is not by itself electrical/mechanical input power, because no constitutive source or apparatus has been specified. It vanishes at instantaneous rest or zero acceleration, changes sign when acceleration reverses at fixed velocity, and is invariant when both `v` and `a` reverse. In geometric units E_total has dimension L, so P_acc is dimensionless because v is dimensionless and a has L^-1 while sigma has L.

The Gaussian boundary assumption is smooth decay at spatial infinity and fixed sigma. A changing sigma adds an independent `partial E_total/partial sigma * sigma_dot` term and is outside this bounded test.
