"""Demonstrative calculations; not simulated metric evolution or empirical data."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.propulsion import ideal_rocket_thrust, ideal_jet_kinetic_power, photon_thrust
from src.medium import top_hat_shape, stationary_dust_density, relative_mass_flux

if __name__ == "__main__":
    mdot, ve, power = 0.1, 3000.0, 1000.0
    print(f"Ideal rocket: mdot={mdot} kg/s, ve={ve} m/s -> thrust={ideal_rocket_thrust(mdot,ve):.3f} N")
    print(f"Ideal rocket jet kinetic power={ideal_jet_kinetic_power(mdot,ve):.3f} W")
    print(f"Ideal photon rocket: radiated power={power} W -> thrust={photon_thrust(power):.9g} N")
    print("Dust toy: rho0=1 kg/m^3, bubble speed=100 m/s, R=5 m, wall=2 m")
    for xi in [-20, -5, 0, 5, 20]:
        f = top_hat_shape(xi,5,2)
        density=stationary_dust_density(1,f)
        print(f" xi={xi:>3} m, f={f:.8f}, rho={density:.6f} kg/m^3, "
              f"flux={relative_mass_flux(density,f,100):.6f} kg/(m^2 s)")
