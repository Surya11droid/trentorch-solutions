import numpy as np


def ridge_regression_closed_form(
    input: np.ndarray, target: np.ndarray, alpha: float = 1.0
) -> tuple[np.ndarray, np.ndarray]:

    X = np.column_stack((input, np.ones(input.shape[0])))

    I = np.eye(X.shape[1])
    I[-1, -1] = 0

    theta = np.linalg.solve(
        X.T @ X + alpha * I,
        X.T @ target
    )

    return theta[:-1], theta[-1:]
