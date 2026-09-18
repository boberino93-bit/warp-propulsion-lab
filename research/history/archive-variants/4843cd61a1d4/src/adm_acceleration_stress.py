"""Acceleration-dependent trace-source diagnostic for prescribed Alcubierre ADM data.

Geometric units c=G=1. Standard ADM convention used elsewhere in this repository:
K_ij=(D_i beta_j+D_j beta_i)/2 for time-independent flat gamma_ij.
For beta_x=-v(t) f(x-x_s(t),y,z), K=-v f_x.
The trace evolution equation gives
  4*pi*(E+S) = (partial_t - L_beta)K - K_ij K^ij
for alpha=1, R=0. Only the explicit acceleration contribution is
  (E+S)_a = -a f_x/(4*pi).
"""
import math


def acceleration_trace_source(acceleration_geom, fx):
    """Acceleration-only contribution to E+S in geometric units."""
    if not (math.isfinite(acceleration_geom) and math.isfinite(fx)):
        raise ValueError("finite acceleration and gradient required")
    return -acceleration_geom * fx / (4.0 * math.pi)


def gaussian_integrated_acceleration_trace(acceleration_geom, sigma, half_width, n=101):
    """Numerically integrate the acceleration trace term for a 3-D Gaussian.

    Uses midpoint quadrature. Odd x parity should cancel to roundoff on a
    symmetric grid; the analytic infinite-domain integral is exactly zero.
    """
    if not (math.isfinite(acceleration_geom) and sigma > 0 and half_width > 0 and n >= 3):
        raise ValueError("finite acceleration, positive scales, n>=3 required")
    h = 2.0 * half_width / n
    total = 0.0
    invs2 = 1.0/(sigma*sigma)
    for i in range(n):
        x = -half_width + (i+0.5)*h
        for j in range(n):
            y = -half_width + (j+0.5)*h
            for k in range(n):
                z = -half_width + (k+0.5)*h
                f = math.exp(-0.5*(x*x+y*y+z*z)*invs2)
                fx = -x*invs2*f
                total += acceleration_trace_source(acceleration_geom, fx)
    return total*h**3
