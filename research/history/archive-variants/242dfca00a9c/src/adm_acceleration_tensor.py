"""Acceleration-only spatial stress required by the ADM K_ij evolution equation.

Geometric units G=c=1, alpha=1, flat gamma_ij, shift beta_x=-v(t) f.
This isolates terms linear in coordinate acceleration a=dv/dt. It is a
fixed-geometry source diagnostic, not a material model or propulsion device.
"""
import math

PI = math.pi


def acceleration_stress_tensor(a, fx, fy, fz):
    """Return acceleration-only (Sxx,Syy,Szz,Sxy,Sxz,Syz).

    Using K_ij = -v/2 (delta_ix f_j + delta_jx f_i) and
    d_t K_ij|_a = -a/2 (delta_ix f_j + delta_jx f_i).
    The ADM evolution source term is
      -8*pi*(S_ij - 1/2 delta_ij*(S-E)),
    while E has no acceleration-only Hamiltonian contribution.
    """
    vals = (a, fx, fy, fz)
    if not all(math.isfinite(x) for x in vals):
        raise ValueError("inputs must be finite")
    q = a / (16.0 * PI)
    return (0.0, -2.0*q*fx, -2.0*q*fx, q*fy, q*fz, 0.0)


def acceleration_trace(a, fx):
    """Trace S_xx+S_yy+S_zz for the acceleration-only part."""
    return -a * fx / (4.0 * PI)


def acceleration_force_x(a, fyy, fzz):
    """Coordinate divergence d_j S_xj of acceleration-only stress.

    For constant a: d_x Sxx + d_y Sxy + d_z Sxz
      = a (f_yy + f_zz)/(16*pi).
    Its all-space integral vanishes for localized smooth f.
    """
    vals = (a, fyy, fzz)
    if not all(math.isfinite(x) for x in vals):
        raise ValueError("inputs must be finite")
    return a * (fyy + fzz) / (16.0 * PI)
