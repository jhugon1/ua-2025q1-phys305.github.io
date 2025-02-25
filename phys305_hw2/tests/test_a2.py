import pytest
import numpy as np

from phys305_hw2 import x, R_proj

def test_x():

    theta = np.pi / 4
    v0    = 10.0
    g     =  9.81
    t     =  1.0

    x0 = x(theta, v0, g, 0.0, t)
    assert x0 == pytest.approx(7.0710678118654755, abs=1e-12)

    x0 = x(theta, v0, g, 0.1, t)
    assert x0 == pytest.approx(6.7290107021993670, abs=1e-12)

    x0 = x(theta, v0, g, 0.2, t)
    assert x0 == pytest.approx(6.4088356859568885, abs=1e-12)

def test_R_proj():

    theta = np.pi / 4
    v0    = 10.0
    g     =  9.81

    R0 = R_proj(theta, v0, g, 0.0)
    assert R0 == pytest.approx(10.19367991845056, abs=1e-12)

    R0 = R_proj(theta, v0, g, 0.1)
    assert R0 == pytest.approx(9.290293395207929, abs=1e-12)

    R0 = R_proj(theta, v0, g, 0.2)
    assert R0 == pytest.approx(8.518424460268855, abs=1e-12)
