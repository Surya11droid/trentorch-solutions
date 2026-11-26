
import numpy as np


def logistic_grad_hess(y, raw):
    y = np.asarray(y)
    raw = np.asarray(raw)

    if not np.all((y == 0) | (y == 1)):
        raise ValueError("Labels must be 0 or 1")

    p = 1 / (1 + np.exp(-raw))

    g = p - y
    h = p * (1 - p)

    return g, h


def leaf_weight(G, H, lam):
    if lam <= 0:
        raise ValueError("lam must be positive")

    return -G / (H + lam)


def split_gain(G_L, H_L, G_R, H_R, lam, gamma):
    if lam <= 0:
        raise ValueError("lam must be positive")

    G = G_L + G_R
    H = H_L + H_R

    gain = 0.5 * (
        G_L**2 / (H_L + lam)
        + G_R**2 / (H_R + lam)
        - G**2 / (H + lam)
    ) - gamma

    return gain
