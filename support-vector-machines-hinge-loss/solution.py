
import numpy as np

def hinge_loss(scores, target, reduction="mean"):
    scores = np.asarray(scores)
    target = np.asarray(target)
    losses = np.maximum(0, 1 - target * scores)

    if reduction == "mean":
        return np.mean(losses)

    elif reduction == "sum":
        return np.sum(losses)

    elif reduction == "none":
        return losses

    else:
        raise ValueError("Invalid reduction")
