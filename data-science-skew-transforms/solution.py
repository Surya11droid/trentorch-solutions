import numpy as np


def skewness(x):
    x = np.asarray(x, dtype=float)

    mean = np.mean(x)
    std = np.std(x)

    if std == 0:
        return 0.0

    standardized = (x - mean) / std

    return np.mean(standardized ** 3)


def log1p_transform(x):
    x = np.asarray(x, dtype=float)

    if np.any(x < 0):
        raise ValueError("Values must be non-negative")

    return np.log1p(x)


def inverse_log1p(z):
    z = np.asarray(z, dtype=float)

    return np.expm1(z)


def box_cox(x, lam):
    x = np.asarray(x, dtype=float)

    if np.any(x <= 0):
        raise ValueError("All values must be strictly positive")

    if lam == 0:
        return np.log(x)

    return (x ** lam - 1) / lam


def best_box_cox_lambda(x, candidates):
    x = np.asarray(x, dtype=float)

    best_lambda = None
    best_skewness = float("inf")

    for lam in candidates:
        transformed = box_cox(x, lam)
        current_skewness = abs(skewness(transformed))

        if current_skewness < best_skewness:
            best_skewness = current_skewness
            best_lambda = lam

    return best_lambda
