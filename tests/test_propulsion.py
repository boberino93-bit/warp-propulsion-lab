import unittest
from src.propulsion import SPEED_OF_LIGHT_M_S, ideal_rocket_thrust, ideal_jet_kinetic_power, photon_thrust

class PropulsionBenchmarks(unittest.TestCase):
    def test_rocket_momentum(self):
        self.assertAlmostEqual(ideal_rocket_thrust(0.1,3000),300.0)
        self.assertAlmostEqual(ideal_rocket_thrust(0,3000),0)
    def test_rocket_energy(self):
        self.assertAlmostEqual(ideal_jet_kinetic_power(0.1,3000),450000)
        self.assertAlmostEqual(ideal_jet_kinetic_power(0.1,3000),0.5*ideal_rocket_thrust(0.1,3000)*3000)
    def test_photon_thrust(self):
        self.assertAlmostEqual(photon_thrust(SPEED_OF_LIGHT_M_S),1.0)
        self.assertAlmostEqual(photon_thrust(0),0)
    def test_negative_rejected(self):
        for func,args in [(ideal_rocket_thrust,(-1,1)),(ideal_jet_kinetic_power,(1,-1)),(photon_thrust,(-1,))]:
            with self.assertRaises(ValueError): func(*args)

if __name__ == '__main__': unittest.main()
