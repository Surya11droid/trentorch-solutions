
import numpy as np


def radius_feature(x, y):
    """
    Calculate distance from origin.
    """
    return np.sqrt(np.asarray(x)**2 + np.asarray(y)**2)


def ratio_feature(numerator, denominator):
    """
    Calculate element-wise ratio.
    """
    return np.asarray(numerator) / np.asarray(denominator)
