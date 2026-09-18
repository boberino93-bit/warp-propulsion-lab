"""SI conversion of prescribed one-scale Gaussian Alcubierre Eulerian energy; not actuator power."""
import math
C=299792458.0
G=6.67430e-11
K=math.sqrt(math.pi)/(32*math.sqrt(2))
Q=K*C*C/G

def energy_j(sigma_m, velocity_m_s):
    if sigma_m<=0 or not math.isfinite(sigma_m) or not math.isfinite(velocity_m_s):
        raise ValueError('finite velocity and positive finite sigma required')
    return -Q*sigma_m*velocity_m_s**2

def inventory_rate_w(sigma_m, velocity_m_s, acceleration_m_s2):
    if not math.isfinite(acceleration_m_s2):
        raise ValueError('finite acceleration required')
    energy_j(sigma_m,velocity_m_s)
    return -2*Q*sigma_m*velocity_m_s*acceleration_m_s2
