
import numpy as np

def epsilon_insensitive_loss(
    predictions,
    targets,
    epsilon=0.1,
    reduction="mean"
):
    if reduction not in ("mean", "sum", "none"):
        raise ValueError("Invalid reduction")

    errors = np.abs(
        np.asarray(predictions) - np.asarray(targets)
    )

    losses = np.maximum(0, errors - epsilon)

    if reduction == "mean":
        return np.mean(losses)
    elif reduction == "sum":
        return np.sum(losses)
    else:
        return losses
