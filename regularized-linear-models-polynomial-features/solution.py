
import numpy as np
from itertools import combinations_with_replacement


def polynomial_features_multivariate(X, degree):
    X = np.asarray(X)

    n_samples, n_features = X.shape

    features = []
    features.append(np.ones(n_samples))
    for d in range(1, degree + 1):
        for combo in combinations_with_replacement(
            range(n_features), d
        ):
            column = np.prod(X[:, combo], axis=1)

            features.append(column)

    return np.column_stack(features)
