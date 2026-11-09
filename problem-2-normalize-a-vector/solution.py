
import numpy as np

def solve(x):
    x = np.array(x, dtype=float)

    norm = np.linalg.norm(x)

    if norm == 0:
        raise ValueError("Cannot normalize a zero vector")

    return x / norm
