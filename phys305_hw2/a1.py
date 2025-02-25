#!/usr/bin/env python3

# Please look for "TODO" in the comments, which indicate where you
# need to write your code.

# Assignment 1: Implement the Vertical Motion $y(t)$ and Solve for
# Flight Time $T(\theta)$ (2 points)
#
# Objective: Implement the equation for the projectile's vertical
# position $y(t)$ under linear drag, then use a root-finding algorithm
# to determine the non-trivial flight time $T$ (i.e., when $y(t) = 0$
# after launch).

# Details:
# * Write a function `y(theta, v0, g, gamma, t)` that returns the
#   vertical position at time `t`.
# * Make sure to handle the special case $\gamma = 0$ (no drag).
# * Implement a root finder.
# * Implement a function `T(theta, v0, g, gamma)` that uses the root
#   finder to find the positive time root of `y(...) = 0`.
# * A good initial guess for the root is the no-drag flight time.
# * Test your function(s) for different parameters.
#   Print or plot the results to ensure they make physical sense.
# * The description of this assignment and a code skeleton can be
#   found in `src/phys305_hw2/a1.py`.

import jax
jax.config.update("jax_enable_x64", True)

from jax import numpy as np
from jax import grad

def root(f, x0, tol=1e-12, imax=1000):
    # Find root of function f using newtons method
    # 1000 iteration limit
    # Raises value error if derivative found to be zero
    
    df = grad(f)
    for _ in range(imax):
        df0 = df(x0)
        if df0 == 0:
            raise ValueError("Derivative is zero. No convergence.")
        x = x0 - f(x0)/df0
        if abs(x - x0) < tol:
            return x
        x0 = x
    return x

def y(theta, v0, g, gamma, t):
    # return the y position of the projectile at time t
    if gamma > 0:
        return ((v0*np.sin(theta)+(g/gamma))/gamma)*(1-np.exp(-gamma*t))-((g/gamma))*t
    else:
        return (v0*t*np.sin(theta))-(.5*g*t**2)

def T_flight(theta, v0, g, gamma):
    # reurn the derived time of flight given all input parameters

    t0 = (2*v0*np.sin(theta)/g) # make initial guess for gamma = 0 case
    return root(lambda t: y(theta, v0, g, gamma, t), t0) # find time when y = 0 and use as time of flight

