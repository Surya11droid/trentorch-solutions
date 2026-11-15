
import numpy as np

def weighted_bce_loss(p, y, class_weights):
    p = np.clip(p, 1e-12, 1 - 1e-12)

    weights = np.where(
        y == 1,
        class_weights[1],
        class_weights[0]
    )

    loss = -(
        y * np.log(p) +
        (1 - y) * np.log(1 - p)
    )

    return float(np.mean(weights * loss))
