#!/usr/bin/env python3

# Please look for "TODO" in the comments, which indicate where you
# need to write your code.

# Assignment 3: Finite Difference Scheme for $R'(\theta)$ (2 points)
#
# Objective: Implement a finite difference approach to numerically
# approximate the derivative of the range $R(\theta)$ with respect to
# $\theta$.
#
# Details:
# * Given your `R(theta, v0, g, gamma)`, implement a function
#   `Rp(theta, v0, g, gamma)` that approximates
#   $$R'(\theta) \equiv \frac{d}{d\theta} R(\theta)$$
#   using a finite difference scheme.
# * Choose a small finite difference parameter $h$ and verify that
#   your approximation converges.
# * Demonstrate this derivative calculation for a few different angles
#   and drag coefficients, printing or plotting the approximate
#   $R'(\theta)$ values.
# * The description and relevant code can be found in
#   `src/phys305_hw2/a3.py`.

from phys305_hw2 import R_proj

def fd(f, x, h=1e-8):
    # TODO: document and implement a finite difference method
    return (f(x+h)-f(x-h))/(2*h)

def Rp_proj(theta, v0, g, gamma):
    # TODO: document and implement the derivative of the range function here
    return fd(lambda theta : R_proj(theta, v0, g, gamma), theta)
