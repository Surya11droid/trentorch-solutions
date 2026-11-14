
import numpy as np


def bce_loss(p, y):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    loss = -(y * np.log(p) + (1 - y) * np.log(1 - p))
    return float(np.mean(loss))
