
import numpy as np

def functional_margin(weight, bias, X, y):
    predictions = X @ weight + bias
    return y * predictions


def geometric_margin(weight, bias, X, y):
    functional = functional_margin(weight, bias, X, y)
    norm = np.linalg.norm(weight)
    return functional / norm


def dataset_margin(weight, bias, X, y):
    margins = geometric_margin(weight, bias, X, y)
    return np.min(margins)
