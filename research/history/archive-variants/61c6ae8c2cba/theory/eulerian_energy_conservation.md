# Exact Eulerian energy balance for rigid translation (v0.3.10)

Metric and conventions: `ds^2=-dt^2+(dx-v f dt)^2+dy^2+dz^2`, `alpha=1`, flat `gamma_ij`, `beta^x=-v f`, geometric units `G=c=1`, and rigid `f=F(x-vt,y,z)`. With `E=T_ab n^a n^b`, repository `j_i=-gamma_i^a n^b T_ab`, and spatial stress `S_ij`, the Eulerian projection is

`(partial_t-L_beta)E + D_i j^i = K E + K_ij S^ij`.

An independent SymPy construction of the metric inverse, Christoffels, Ricci tensor/scalar and Einstein tensor gives, before division by `8 pi`,

`E_G = -v^2(f_y^2+f_z^2)/4`,
`j_x,G=-v(f_yy+f_zz)/2`, `j_y,G=v f_xy/2`, `j_z,G=v f_xz/2`.

Hence `D_i j^i=0` identically by equality of mixed derivatives. Direct contraction of the Einstein-derived spatial stress with the repository extrinsic curvature gives exact pointwise closure

`(partial_t-L_beta)E = K E + K_ij S^ij = -v^3 (f_y f_xy+f_z f_xz)(f-1)/(16 pi)`

in stress-energy units. This term has dimension `L^-3`: it is a local energy-transfer/work-rate density in geometric spacetime units, not an ordinary SI power density without the appropriate conversion.

For `f=exp[-(x^2+y^2+z^2)/sigma^2]`, `f_y f_xy+f_z f_xz=-8 x(y^2+z^2)f^2/sigma^6`. The balance is odd in x and therefore integrates to zero over all space for the symmetric localized Gaussian. Separately, rigid translation makes `Integral partial_t E d^3x=0`; the shift-work integral also vanishes by parity. Thus a constant-speed bubble has nonzero local Eulerian energy redistribution but no changing total integrated Eulerian source energy in this model.

This is not a source construction. Covariant conservation of the effective Einstein stress-energy is necessary and ultimately follows from the contracted Bianchi identity. The test is useful because it checks signs/projections and blocks a false power or propulsion inference from incomplete local terms.

Primary context: Alcubierre (1994), DOI `10.1088/0264-9381/11/5/001`; Gourgoulhon, *3+1 Formalism and Bases of Numerical Relativity*, arXiv:`gr-qc/0703035` (matter 3+1 decomposition and conservation framework).
