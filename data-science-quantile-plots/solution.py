
import numpy as np
import math


def normal_ppf(p):
    if not 0 < p < 1:
        raise ValueError("p must be between 0 and 1")

    def cdf(z):
        return 0.5 * (1 + math.erf(z / math.sqrt(2)))

    low, high = -10.0, 10.0

    for _ in range(100):
        mid = (low + high) / 2

        if cdf(mid) < p:
            low = mid
        else:
            high = mid

    return (low + high) / 2


def plotting_positions(n):
    if n <= 0:
        raise ValueError("n must be positive")

    return (np.arange(1, n + 1) - 0.5) / n


def qq_points(x):
    x = np.asarray(x, dtype=float)

    sample = np.sort(x)
    probabilities = plotting_positions(len(sample))

    theoretical = np.array([
        normal_ppf(p) for p in probabilities
    ])

    return theoretical, sample


def qq_line(theoretical, sample):
    t25, t75 = np.percentile(theoretical, [25, 75])
    s25, s75 = np.percentile(sample, [25, 75])

    slope = (s75 - s25) / (t75 - t25)
    intercept = s25 - slope * t25

    return float(slope), float(intercept)


def qq_correlation(x):
    theoretical, sample = qq_points(x)

    return float(np.corrcoef(theoretical, sample)[0, 1])
