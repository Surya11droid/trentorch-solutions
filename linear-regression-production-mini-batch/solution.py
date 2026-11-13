
import numpy as np


def train_linear_regression_production(
    input: np.ndarray,
    target: np.ndarray,
    lr: float,
    epochs: int,
    batch_size: int,
    seed: int | None = None,
) -> tuple[np.ndarray, np.ndarray]:

    n_samples, n_features = input.shape

    # 1. Initialize weights and bias
    weight = np.zeros((1, n_features))
    bias = np.zeros((1,))

    # 2. Reshape target once
    target = target.reshape(-1, 1)

    # 3. Create RNG only once
    rng = np.random.default_rng(seed)

    # 4. Training loop
    for epoch in range(epochs):

        # Shuffle sample indices
        indices = rng.permutation(n_samples)

        # 5. Divide into mini-batches
        for start in range(0, n_samples, batch_size):

            end = start + batch_size

            batch_indices = indices[start:end]

            # Extract current batch only
            batch_input = input[batch_indices]
            batch_target = target[batch_indices]

            # 6. Calculate gradients
            grad_weight, grad_bias = mse_gradient(
                batch_input,
                weight,
                bias,
                batch_target
            )

            # 7. Update parameters
            weight, bias = gd_step(
                weight,
                bias,
                grad_weight,
                grad_bias,
                lr
            )

    return weight, bias
