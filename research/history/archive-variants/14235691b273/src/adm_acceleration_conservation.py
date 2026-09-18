"""Leading acceleration-order local momentum conservation for prescribed Alcubierre ADM source.

Geometric units G=c=1.  This isolates terms proportional to a=dv/dt in
partial_t j_x + partial_j S_xj.  It is not a complete nonlinear conservation
law or a material source model.
"""
import math

PI = math.pi


def momentum_time_derivative_acceleration(a, fyy, fzz):
    """Acceleration-only part of partial_t j_x at fixed spatial point.

    From j_x=-v(f_yy+f_zz)/(16*pi), differentiating v contributes this term.
    Shape-translation terms proportional to v^2 are outside this bounded gate.
    """
    vals=(a,fyy,fzz)
    if not all(math.isfinite(q) for q in vals):
        raise ValueError("inputs must be finite")
    return -a*(fyy+fzz)/(16.0*PI)


def stress_divergence_acceleration(a, fyy, fzz):
    """Acceleration-only partial_j S_xj from the v0.3.5 stress tensor."""
    vals=(a,fyy,fzz)
    if not all(math.isfinite(q) for q in vals):
        raise ValueError("inputs must be finite")
    return a*(fyy+fzz)/(16.0*PI)


def local_momentum_residual_acceleration(a, fyy, fzz):
    """Acceleration-order residual partial_t j_x + partial_j S_xj."""
    return (momentum_time_derivative_acceleration(a,fyy,fzz)
            + stress_divergence_acceleration(a,fyy,fzz))
