
import numpy as np


def ridge_grad(
    input: np.ndarray,
    weight: np.ndarray,
    bias: np.ndarray | None,
    target: np.ndarray,
    lam: float,
) -> tuple[np.ndarray, np.ndarray | None]:

    grad_weight, grad_bias = mse_gradient(input, weight, bias, target)

    grad_weight = grad_weight + 2 * lam * weight

    return grad_weight, grad_bias
