import numpy as np


def softmax(Z: np.ndarray) -> np.ndarray:
    """
    Convert class scores into probabilities row-wise.
    """
    Z = np.asarray(Z, dtype=float)

    # Subtract maximum of each row for numerical stability
    Z_shifted = Z - np.max(Z, axis=1, keepdims=True)
    exp_Z = np.exp(Z_shifted)
    return exp_Z / np.sum(exp_Z, axis=1, keepdims=True)


def cce_loss(P: np.ndarray, y_indices: np.ndarray) -> float:
    """
    Calculate categorical cross-entropy loss.
    """
    P = np.asarray(P, dtype=float)
    y_indices = np.asarray(y_indices, dtype=int)

    n = P.shape[0]
    correct_probs = P[np.arange(n), y_indices]
    correct_probs = np.clip(correct_probs, 1e-12, 1.0)

    # Calculate average categorical cross-entropy
    return float(-np.mean(np.log(correct_probs)))
