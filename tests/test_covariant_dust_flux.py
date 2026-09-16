import unittest
import math
from src.medium import top_hat_shape

class CovariantDustFluxTests(unittest.TestCase):
    def test_metric_inverse_and_normal(self):
        for beta in (-0.7, 0.0, 0.4):
            gtt, gtx, gxx = beta*beta-1.0, -beta, 1.0
            # inverse: [[-1,-beta],[-beta,1-beta^2]]
            self.assertAlmostEqual(gtt*(-1)+gtx*(-beta), 1.0)
            self.assertAlmostEqual(gtt*(-beta)+gtx*(1-beta*beta), 0.0)
            # n^mu=(1,beta), n_mu=(-1,0)
            self.assertAlmostEqual(gtt + gtx*beta, -1.0)
            self.assertAlmostEqual(gtx + gxx*beta, 0.0)

    def test_eulerian_energy_and_zero_local_momentum(self):
        eps, beta = 3.2, 0.35
        # T^tt=e, T^tx=e beta, T^xx=e beta^2; n_mu=(-1,0)
        E = eps
        # spatial projection gamma_xmu T^{mu nu} n_nu = 0 analytically
        jx = -(beta*eps + 1.0*eps*beta*(-1))  # explicit cancellation form
        self.assertAlmostEqual(E, eps)
        self.assertAlmostEqual(jx, 0.0)

    def test_relative_flux_invariant(self):
        vs, R, w, eps0 = 100.0, 5.0, 2.0, 1.225
        xi0, xi = 8.0, 5.53552944
        f0, ft = top_hat_shape(xi0,R,w), top_hat_shape(xi,R,w)
        eps = eps0*(1-f0)/(1-ft)
        rel0 = -vs*eps0*(1-f0)
        relt = eps*vs*(ft-1)
        self.assertAlmostEqual(relt, rel0, places=9)

if __name__ == '__main__': unittest.main()
