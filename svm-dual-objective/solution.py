
import numpy as np

def dual_objective(alpha, y, K):
    alpha = np.asarray(alpha)
    y = np.asarray(y)
    K = np.asarray(K)

    n = len(alpha)

    if len(y) != n or K.shape != (n, n):
        raise ValueError("Invalid input dimensions")

    # Q[i,j] = alpha[i] * alpha[j] * y[i] * y[j] * K[i,j]
    Q = np.outer(alpha * y, alpha * y) * K

    return float(np.sum(alpha) - 0.5 * np.sum(Q))


def is_dual_feasible(alpha, y, C, tol=1e-9):
    alpha = np.asarray(alpha)
    y = np.asarray(y)

    if len(alpha) != len(y):
        raise ValueError("alpha and y must have the same length")

    if C < 0:
        raise ValueError("C cannot be negative")

    # Check box constraints: 0 <= alpha[i] <= C
    bounds_valid = np.all(alpha >= -tol) and np.all(alpha <= C + tol)

    # Check equality constraint: sum(alpha[i] * y[i]) = 0
    equality_valid = abs(np.sum(alpha * y)) <= tol

    return bool(bounds_valid and equality_valid)
