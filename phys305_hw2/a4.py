#!/usr/bin/env python3

# Please look for "TODO" in the comments, which indicate where you
# need to write your code.

# Assignment 4: Gradient Descent to Optimize the Launch Angle (2 points)
#
# Objective: Use a gradient descent algorithm and your
# finite-difference derivative from Assignment 3 to numerically find
# the angle $\theta$ that maximizes $R(\theta)$.
#
# Details:
# * Create a function `gd_hist(df, x0, alpha, imax=1000)` to perform
#   gradient descent.
#   * Starts with an initial guess `theta0` -> `x0`.
#   * Computes the gradient (derivative) $R'(\theta)$ -> `df` using
#     your finite difference scheme from Assignment 3.
# * Experiment with different step sizes `alpha` (the "learning rate")
#   to see how it affects convergence.
# * Create a function `Theta(v0, g, gamma)` that uses `gd_hist()` to
#   maximize the range function by adjust the launch angle `theta`.
# * Compare the angle you find with the analytical $45^\circ$ result
#   in the no-drag case, and observe how it changes for increasing
#   $\gamma$.
# * A code template for this assignment can be found in
#   `src/phys305_hw2/a4.py`.

import numpy as np

from phys305_hw2 import Rp_proj

def gd_hist(df, x0, alpha, tol=1e-6, imax=100):
    # TODO: document and implement a gradient descent.
    theta0 = x0
    theta_hist = [theta0]
    for _ in range(imax):
        theta_hist.append(theta_hist[-1] - alpha * df(theta_hist[-1]))
    return theta_hist

def Theta(v0, g, gamma):
    # TODO: document and implement the solver that maximize the range
    # function by adjust the launch angle `theta`.
    theta0 = np.pi/4
    alpha = 0.01
    theta_hist = gd_hist(lambda theta: Rp_proj(theta, v0, g, gamma), theta0, alpha)
    theta_opt = theta_hist[-1]
    result = abs(theta_opt)
    if result > np.pi/2:
        result = np.pi-result
    return (result)
