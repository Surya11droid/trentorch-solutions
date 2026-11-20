
def polynomial_kernel(X, Y, degree=3, coef0=1.0, gamma=1.0):
    # Calculate the linear kernel first
    K = linear_kernel(X, Y)

    # Apply polynomial transformation
    return (gamma * K + coef0) ** degree
