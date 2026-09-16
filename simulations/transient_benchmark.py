"""A reproducible toy characteristics printout, NOT observational data."""
from src.transient_dust import evolve_characteristic

p = dict(bubble_velocity_m_s=100., upstream_density_kg_m3=1.225,
         half_width_m=5., wall_m=2., steps=400)
print('Prescribed 1-D Eulerian dust; fixed geometry; no pressure or thrust')
print('Initial uniform rho=1.225 kg/m3; t=0.03 s; v_s=100 m/s')
for xi0 in (-8., 0., 8.):
    s = evolve_characteristic(xi0, 0.03, **p)
    print(f'xi0={xi0:+.1f} m; xi(t)={s.xi_m:+.8f} m; '
          f'rho(t)={s.density_kg_m3:.8f} kg/m3; J={s.jacobian:.8f}')
