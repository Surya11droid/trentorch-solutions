
import numpy as np

def log_softmax(Z):
    m = np.max(Z, axis=1, keepdims=True)

    shifted = Z - m

    log_sum_exp = np.log(
        np.sum(np.exp(shifted), axis=1, keepdims=True)
    )

    return shifted - log_sum_exp


def nll_loss(log_probs, y_indices):
    n = log_probs.shape[0]

    correct_log_probs = log_probs[
        np.arange(n), y_indices
    ]

    return -np.mean(correct_log_probs)
