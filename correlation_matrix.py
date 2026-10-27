import numpy as np

from _load import load_solution

correlation = load_solution(
    "math-expectation-variance-covariance"
).correlation


def correlation_matrix(x: np.ndarray) -> np.ndarray:
    num_features = x.shape[1]
    corr_matrix = np.eye(num_features)

    for i in range(num_features):
        for j in range(i + 1, num_features):
            corr = correlation(x[:, i], x[:, j])

            corr_matrix[i, j] = corr
            corr_matrix[j, i] = corr

    return corr_matrix


def most_correlated_pair(corr_matrix: np.ndarray) -> tuple[int, int]:
    n = corr_matrix.shape[0]

    if n < 2:
        raise ValueError("At least two features are required")

    
    scores = np.abs(corr_matrix.copy())
    np.fill_diagonal(scores, -np.inf)

    
    return tuple(map(int, np.unravel_index(np.argmax(scores), scores.shape)))
