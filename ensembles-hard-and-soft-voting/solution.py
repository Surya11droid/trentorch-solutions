
import numpy as np


def hard_vote(predictions):
    n_models, n_samples = predictions.shape

    result = []

    for i in range(n_samples):
        labels, counts = np.unique(
            predictions[:, i],
            return_counts=True
        )

        result.append(labels[np.argmax(counts)])

    return np.array(result, dtype=int)


def soft_vote(probabilities, weights=None):
    n_models, n_samples, n_classes = probabilities.shape

    if weights is None:
        weights = np.ones(n_models)

    weights = np.asarray(weights, dtype=float)
    weights = weights / weights.sum()

    avg_probabilities = np.average(
        probabilities,
        axis=0,
        weights=weights
    )

    return np.argmax(avg_probabilities, axis=1).astype(int)
