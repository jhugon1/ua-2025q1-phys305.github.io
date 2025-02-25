import pytest
import numpy as np

from phys305_hw2 import gd_hist, Theta

def test_gd():

    f1 = lambda x: (x - 1)**2
    f2 = lambda x: (x - 2)**2
    f3 = lambda x: (x - 3)**2

    df1 = lambda x: 2 * (x - 1)
    df2 = lambda x: 2 * (x - 2)
    df3 = lambda x: 2 * (x - 3)

    x1 = gd_hist(df1, 0, 0.1)[-1]
    assert x1 == pytest.approx(1.0, abs=1e-3)

    x2 = gd_hist(df2, 0, 0.1)[-1]
    assert x2 == pytest.approx(2.0, abs=1e-3)

    x3 = gd_hist(df3, 0, 0.1)[-1]
    assert x3 == pytest.approx(3.0, abs=1e-3)

def test_Theta():

    v0 = 10.0
    g  =  9.81

    theta0 = Theta(v0, g, 0.0)
    assert theta0 == pytest.approx(np.pi/4, 1e-3)

    theta0 = Theta(v0, g, 0.1)
    assert theta0 == pytest.approx(0.7624632436563017, abs=1e-3)

    theta0 = Theta(v0, g, 0.2)
    assert theta0 == pytest.approx(0.7414784031243782, abs=1e-3)
