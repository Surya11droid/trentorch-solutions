
import numpy as np

def lda_fit(X, y):

    # 1. Separate the two classes
    X0 = X[y == 0]
    X1 = X[y == 1]

    # 2. Calculate class means
    mu0 = X0.mean(axis=0)
    mu1 = X1.mean(axis=0)

    # 3. Center the data
    D0 = X0 - mu0
    D1 = X1 - mu1

    # 4. Calculate scatter matrices
    S0 = D0.T @ D0
    S1 = D1.T @ D1

    # 5. Calculate pooled covariance
    n = len(y)
    cov = (S0 + S1) / (n - 2)

    # 6. Calculate discriminant weights
    w = np.linalg.inv(cov) @ (mu1 - mu0)

    # 7. Calculate class counts
    N0 = len(X0)
    N1 = len(X1)

    # 8. Calculate intercept
    b = -0.5 * (mu1 + mu0) @ w + np.log(N1 / N0)

    return w, b
