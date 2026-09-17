"""Ideal reaction-mass baseline. Pressure-matched nozzle only."""
C=299792458.0

def thrust(mdot, ve):
    if mdot < 0 or ve < 0: raise ValueError
    return mdot*ve

def jet_power(mdot, ve):
    if mdot < 0 or ve < 0: raise ValueError
    return 0.5*mdot*ve**2

def propellant_rate_g_min(mdot):
    if mdot < 0: raise ValueError
    return mdot*1000*60

def photon_power_equivalent(force, reflect=False):
    if force < 0: raise ValueError
    return force*C/(2 if reflect else 1)
