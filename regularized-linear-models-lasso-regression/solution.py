
import numpy as np


def soft_threshold(x, threshold):
    return np.sign(x) * np.maximum(np.abs(x) - threshold, 0)


def lasso_regression_coordinate_descent(
    input, target, alpha=1.0, epochs=200
):
    X = np.asarray(input, dtype=float)
    y = np.asarray(target, dtype=float).reshape(-1)

    x_mean = X.mean(axis=0)
    y_mean = y.mean()

    X = X - x_mean
    y = y - y_mean

    n, features = X.shape
    weight = np.zeros(features)

    for _ in range(epochs):
        for j in range(features):
            residual = y - X @ weight + X[:, j] * weight[j]

            rho = np.dot(X[:, j], residual) / n
            z = np.dot(X[:, j], X[:, j]) / n

            if z > 0:
                weight[j] = soft_threshold(rho, alpha) / z

    bias = y_mean - np.dot(x_mean, weight)

    return weight.reshape(1, -1), np.array([bias])
