
import numpy as np


def ambiguity_decomposition(predictions, target):
    predictions = np.asarray(predictions, dtype=float)
    target = np.asarray(target, dtype=float)
    ensemble_predictions = np.mean(predictions, axis=0)
    ensemble_error = np.mean(
        (ensemble_predictions - target) ** 2
    )
    individual_errors = np.mean(
        (predictions - target) ** 2,
        axis=1
    )
    mean_individual_error = np.mean(individual_errors)
    ambiguity = np.mean(
        (predictions - ensemble_predictions) ** 2
    )

    return (
        float(ensemble_error),
        float(mean_individual_error),
        float(ambiguity)
    )
