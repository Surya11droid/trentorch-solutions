
import numpy as np

def closed_form_linear_regression(input, target):
    # Augment input with a column of ones
    X = np.c_[input, np.ones(input.shape[0])]

    # Calculate optimal parameters
    params = np.linalg.pinv(X) @ target.reshape(-1, 1)

    # Extract weights and bias
    weight = params[:-1].T
    bias = params[-1].reshape(1,)

    return weight, bias
