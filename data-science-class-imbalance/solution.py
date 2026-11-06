
import numpy as np


def class_weights(y):
    classes, counts = np.unique(y, return_counts=True)
    return {c: len(y) / (len(classes) * n)
            for c, n in zip(classes, counts)}


def random_oversample(X, y, rng):
    classes, counts = np.unique(y, return_counts=True)
    X_new, y_new = [X], [y]

    for c, n in zip(classes, counts):
        idx = np.where(y == c)[0]
        extra = rng.choice(idx, size=counts.max() - n, replace=True)
        if len(extra):
            X_new.append(X[extra])
            y_new.append(y[extra])

    return np.concatenate(X_new), np.concatenate(y_new)


def random_undersample(X, y, rng):
    classes, counts = np.unique(y, return_counts=True)
    idx = []

    for c in classes:
        rows = np.where(y == c)[0]
        idx.extend(np.sort(rng.choice(rows, counts.min(), replace=False)))

    idx = np.array(idx)
    return X[idx], y[idx]


def interpolate_minority(minority, n_new, rng):
    if len(minority) < 2:
        raise ValueError("At least 2 minority points required")

    result = []
    for _ in range(n_new):
        a, b = minority[rng.choice(len(minority), 2, replace=False)]
        u = rng.random()
        result.append(a + u * (b - a))

    return np.array(result).reshape(n_new, minority.shape[1])
