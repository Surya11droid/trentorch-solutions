
import numpy as np


def standardize(x, mean=None, std=None):
    x = np.asarray(x, dtype=float)

    if mean is None:
        mean = np.mean(x, axis=0)

    if std is None:
        std = np.std(x, axis=0)

  
    std = np.where(std == 0, 1, std)

    scaled_x = (x - mean) / std

    return scaled_x, mean, std


def min_max_normalize(x, min_val=None, max_val=None):
    x = np.asarray(x, dtype=float)

    if min_val is None:
        min_val = np.min(x, axis=0)

    if max_val is None:
        max_val = np.max(x, axis=0)


    denominator = max_val - min_val
    denominator = np.where(denominator == 0, 1, denominator)

    scaled_x = (x - min_val) / denominator

    return scaled_x, min_val, max_val
