
import numpy as np


def huber_loss(
    input: np.ndarray, target: np.ndarray, delta: float = 1.0, reduction: str = "mean"
) -> float | np.ndarray:
    error = input - target
    abs_error = np.abs(error)
    quadratic = 0.5 * error**2
    linear = delta * (abs_error - 0.5 * delta)
    elementwise = np.where(abs_error <= delta, quadratic, linear)
    if reduction == "mean":
        return np.mean(elementwise)

    elif reduction == "sum":
        return np.sum(elementwise)

    elif reduction == "none":
        return elementwise

    else:
        raise ValueError("Invalid reduction mode")
