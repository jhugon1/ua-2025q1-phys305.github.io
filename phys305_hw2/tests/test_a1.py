import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


import pytest
import numpy as np

from phys305_hw2 import root, y, T_flight

def test_root():
    def f1(x):
        return (x - 1)
    def f2(x):
        return (x - 2) * (x - 2)
    def f3(x):
        return (x - 3) * (x - 3) * (x - 3)

    x = root(f1, 0.0)
    assert x == pytest.approx(1)

    x = root(f2, 0.0)
    assert x == pytest.approx(2)

    x = root(f3, 0.0)
    assert x == pytest.approx(3)

def test_y():

    theta = np.pi / 4
    v0    = 10.0
    g     =  9.81
    t     =  1.0

    y0 = y(theta, v0, g, 0.0, t)
    assert y0 == pytest.approx(2.1660678118654744, abs=1e-12)

    y0 = y(theta, v0, g, 0.1, t)
    assert y0 == pytest.approx(1.9835036089230726, abs=1e-12)

    y0 = y(theta, v0, g, 0.2, t)
    assert y0 == pytest.approx(1.8151184935818420, abs=1e-12)

def test_T_flight():

    theta = np.pi / 4
    v0    = 10.0
    g     =  9.8

    T0 = T_flight(theta, v0, g, 0.0)
    assert T0 == pytest.approx(1.4430750636460150, abs=1e-12)

    T0 = T_flight(theta, v0, g, 0.1)
    assert T0 == pytest.approx(1.4099532342329029, abs=1e-12)

    T0 = T_flight(theta, v0, g, 0.2)
    assert T0 == pytest.approx(1.3797027836918636, abs=1e-12)
