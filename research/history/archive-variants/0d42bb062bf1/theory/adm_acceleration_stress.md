# Acceleration-dependent ADM trace-stress gate

**Status: DERIVED-CONDITIONAL.** Prescribed Alcubierre geometry, geometric units `c=G=1`; this is a source requirement, not an engine.

Use unit lapse, flat spatial metric and `beta_x=-v(t) f(x-x_s(t),y,z)`. With the repository's standard ADM convention, `K_ij=(D_i beta_j+D_j beta_i)/2`, so `K=-v f_x`.

The ADM trace evolution equation is

`(partial_t - L_beta) K = K_ij K^ij + 4 pi (E+S)`

for `alpha=1` and spatial scalar curvature `R=0`, where `E` is Eulerian energy density and `S=gamma^ij S_ij` is the spatial-stress trace. Isolating only terms proportional to the coordinate acceleration `a=dv/dt` gives

`(E+S)_acc = -a f_x/(4 pi)`.

Thus acceleration requires a **local, sign-changing stress/energy-trace contribution** concentrated where the shape has longitudinal gradient. It is odd front-to-back for a symmetric localized bubble. Its volume integral is

`Integral (E+S)_acc d^3x = -a/(4 pi) Integral partial_x f d^3x`,

which is a boundary term and vanishes when `f` decays sufficiently at spatial infinity. This does not prove that all acceleration-dependent energy or momentum costs vanish: the trace is only one combination of the required spatial stresses. It does falsify the narrower idea that the trace evolution equation itself supplies a nonzero integrated reaction term for a localized bubble.

**Dimensions:** in geometric units `a` and `f_x` each scale as inverse length, so `(E+S)_acc` scales as inverse length squared, as required by Einstein's equations.

Primary context: Alcubierre (1994), DOI 10.1088/0264-9381/11/5/001. McMonigal, Lewis & O'Byrne (2012), DOI 10.1103/PhysRevD.85.064024, independently show acceleration-dependent effects on non-Eulerian test particles, but do not construct the source. Béatrix-Drouhet (2020), arXiv:2012.09941, studies stress-energy matching for different acceleration/velocity configurations; used as context, not experimental evidence.
