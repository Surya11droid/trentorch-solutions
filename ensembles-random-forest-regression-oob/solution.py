
import numpy as np


def bootstrap_sample_with_oob(
    input: np.ndarray, targets: np.ndarray, seed: int | None = None
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

    n_samples = len(input)

    rng = np.random.default_rng(seed)

    # Draw indices with replacement
    indices = rng.integers(0, n_samples, size=n_samples)

    # Bootstrap samples
    boot_input = input[indices]
    boot_targets = targets[indices]

    # Identify indices that were never selected
    was_drawn = np.zeros(n_samples, dtype=bool)
    was_drawn[indices] = True

    oob_indices = np.where(~was_drawn)[0]

    return boot_input, boot_targets, oob_indices


def train_random_forest_regressor(
    input: np.ndarray,
    targets: np.ndarray,
    n_trees: int,
    max_depth: int,
    seed: int | None = None,
) -> list[tuple[dict, np.ndarray]]:

    # Create one RNG for the entire forest
    rng = np.random.default_rng(seed)

    forest = []

    for _ in range(n_trees):

        # Bootstrap sampling
        n_samples = len(input)
        indices = rng.integers(0, n_samples, size=n_samples)

        boot_input = input[indices]
        boot_targets = targets[indices]

        was_drawn = np.zeros(n_samples, dtype=bool)
        was_drawn[indices] = True

        oob_indices = np.where(~was_drawn)[0]

        # Train regression tree
        tree = build_regression_tree(
            boot_input, boot_targets, max_depth
        )

        forest.append((tree, oob_indices))

    return forest


def predict_random_forest_regressor(
    forest: list[tuple[dict, np.ndarray]], input: np.ndarray
) -> np.ndarray:

    # Get predictions from every tree
    predictions = np.array([
        predict_regression_tree(tree, input)
        for tree, _ in forest
    ])

    # Average across trees
    return np.mean(predictions, axis=0)


def oob_error(
    forest: list[tuple[dict, np.ndarray]],
    input: np.ndarray,
    targets: np.ndarray
) -> float:

    n_samples = len(targets)

    # Store prediction sums and counts
    oob_predictions = np.zeros(n_samples)
    oob_counts = np.zeros(n_samples)

    for tree, oob_indices in forest:

        if len(oob_indices) == 0:
            continue

        # Predict only samples that were OOB for this tree
        predictions = predict_regression_tree(
            tree, input[oob_indices]
        )

        # Accumulate predictions
        oob_predictions[oob_indices] += predictions

        # Count number of OOB predictions per sample
        oob_counts[oob_indices] += 1

    # Select samples having at least one OOB prediction
    valid = oob_counts > 0

    # Average OOB predictions
    oob_predictions[valid] /= oob_counts[valid]

    # Calculate mean squared error
    mse = np.mean(
        (targets[valid] - oob_predictions[valid]) ** 2
    )

    return float(mse)
