import numpy as np


def weighted_majority_vote(predictions, weights):
    predictions = np.asarray(predictions)
    weights = np.asarray(weights)


    if np.any(weights < 0):
        raise ValueError("Weights cannot be negative")

    if np.sum(weights) == 0:
        raise ValueError("Weights cannot all be zero")

    if len(weights) != predictions.shape[0]:
        raise ValueError("Number of weights must match classifiers")

    n = predictions.shape[1]
    result = np.zeros(n, dtype=int)

    for j in range(n):
        
        scores = {}

        for i in range(predictions.shape[0]):
            label = predictions[i, j]
            scores[label] = scores.get(label, 0) + weights[i]

        
        result[j] = min(
            scores,
            key=lambda label: (-scores[label], label)
        )

    return result
