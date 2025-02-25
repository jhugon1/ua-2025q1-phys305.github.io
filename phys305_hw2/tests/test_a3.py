import pytest
import numpy as np

from phys305_hw2 import fd, Rp_proj

def test_fd():

    f1 = lambda x: x
    f2 = lambda x: x * x
    f3 = lambda x: x * x * x

    assert fd(f1, 1) == pytest.approx(1.0, abs=1e-5)
    assert fd(f2, 1) == pytest.approx(2.0, abs=1e-5)
    assert fd(f3, 1) == pytest.approx(3.0, abs=1e-5)

def test_Rp_proj():

    theta = np.pi / 4
    v0    = 10.0
    g     =  9.81

    Rp0 = Rp_proj(theta, v0, g, 0.0)
    assert Rp0 == pytest.approx( 0.0000000000000000, abs=1e-5)

    Rp0 = Rp_proj(theta, v0, g, 0.1)
    assert Rp0 == pytest.approx(-0.8327424083631740, abs=1e-5)

    Rp0 = Rp_proj(theta, v0, g, 0.2)
    assert Rp0 == pytest.approx(-1.4304545103982491, abs=1e-5)
