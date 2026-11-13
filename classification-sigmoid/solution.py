import numpy as np

def sigmoid(z):
    z = np.asarray(z)

    # Prevent exponential overflow
    z = np.clip(z, -500, 500)

    return 1 / (1 + np.exp(-z))
