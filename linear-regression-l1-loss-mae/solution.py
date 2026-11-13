
import numpy as np

def l1_loss(input: np.ndarray,
            target: np.ndarray,
            reduction: str = "mean"):

    loss = np.abs(input - target)

    if reduction == "mean":
        return np.mean(loss)

    elif reduction == "sum":
        return np.sum(loss)

    elif reduction == "none":
        return loss

    else:
        raise ValueError("Invalid reduction mode")
