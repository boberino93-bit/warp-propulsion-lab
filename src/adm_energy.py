"""Hamiltonian-constraint Eulerian energy for prescribed 3+1 Alcubierre shift.

Geometric units G=c=1. REQUIRED SOURCE diagnostic, not an engine.
"""
import math


def eulerian_energy_from_gradients(v_over_c, dfdx, dfdy, dfdz):
    """Return geometric-unit T(n,n) in inverse length squared.

    All spatial gradients are inverse lengths. dfdx cancels in K^2-KijKij.
    """
    for value in (v_over_c, dfdx, dfdy, dfdz):
        if not math.isfinite(value):
            raise ValueError('finite inputs required')
    return -(v_over_c ** 2) * (dfdy ** 2 + dfdz ** 2) / (32 * math.pi)


def radial_energy(v_over_c, x, y, z, fprime):
    """Radial profile derivative fprime=df/dr; center requires fprime=0."""
    r2 = x*x+y*y+z*z
    if r2 == 0:
        if fprime != 0:
            raise ValueError('nonzero radial derivative at origin is nonsmooth')
        return 0.0
    return eulerian_energy_from_gradients(v_over_c, fprime*x/math.sqrt(r2),
                                          fprime*y/math.sqrt(r2), fprime*z/math.sqrt(r2))
