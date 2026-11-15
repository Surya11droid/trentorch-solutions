
import numpy as np

def bce_with_logits_loss(z, y):
    loss = (
        np.maximum(z, 0)
        - z * y
        + np.log1p(np.exp(-np.abs(z)))
    )

    return float(np.mean(loss))
