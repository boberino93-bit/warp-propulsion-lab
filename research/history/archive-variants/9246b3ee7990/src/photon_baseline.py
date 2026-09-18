import math
C=299792458.0

def photon_thrust(power_w, reflectivity=0.0):
    if power_w < 0 or not (0.0 <= reflectivity <= 1.0): raise ValueError
    return (1.0+reflectivity)*power_w/C

def power_for_thrust(force_n, reflectivity=0.0):
    if force_n < 0 or not (0.0 <= reflectivity <= 1.0): raise ValueError
    return force_n*C/(1.0+reflectivity)

def snr(force_n, noise_sigma_n):
    if noise_sigma_n <= 0: raise ValueError
    return force_n/noise_sigma_n
