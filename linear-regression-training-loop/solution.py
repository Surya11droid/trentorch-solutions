import numpy as np


def train_linear_regression(
    input: np.ndarray,
    target: np.ndarray,
    lr: float,
    epochs: int,
) -> tuple[np.ndarray, np.ndarray]:

    # Initialize weight and bias
    weight = np.zeros((1, input.shape[1]))
    bias = np.zeros((1,))

    # Reshape target into a column
    target = target.reshape(-1, 1)

    # Full-batch gradient descent
    for _ in range(epochs):

        # Calculate gradients
        grad_w, grad_b = mse_gradient(
            input, weight, bias, target
        )

        # Update parameters
        weight, bias = gd_step(
            weight,
            bias,
            grad_w,
            grad_b,
            lr
        )

    return weight, bias
