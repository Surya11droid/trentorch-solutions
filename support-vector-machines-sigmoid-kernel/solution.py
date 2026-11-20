
import numpy as np

def sigmoid_kernel(X, Y, gamma=1.0, coef0=0.0):
    linear = linear_kernel(X, Y)
    return np.tanh(gamma * linear + coef0)
