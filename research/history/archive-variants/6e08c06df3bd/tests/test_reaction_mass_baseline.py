import pytest
from src.reaction_mass_baseline import thrust,jet_power,propellant_rate_g_min,photon_power_equivalent

def test_reference_case():
    assert thrust(1e-5,100)==pytest.approx(1e-3)
    assert jet_power(1e-5,100)==pytest.approx(0.05)
    assert propellant_rate_g_min(1e-5)==pytest.approx(0.6)

def test_momentum_scaling():
    assert thrust(2e-5,100)==pytest.approx(2e-3)
    assert thrust(1e-5,200)==pytest.approx(2e-3)

def test_power_scaling():
    assert jet_power(1e-5,200)==pytest.approx(0.2)

def test_photon_comparison():
    assert photon_power_equivalent(1e-3)==pytest.approx(299792.458)
    assert photon_power_equivalent(1e-3,True)==pytest.approx(149896.229)

def test_reject_negative():
    with pytest.raises(ValueError): thrust(-1,1)
