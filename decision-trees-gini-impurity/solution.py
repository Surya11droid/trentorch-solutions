
import numpy as np

def gini_impurity(labels):
    labels = np.asarray(labels)
    if labels.size == 0:
        return 0.0
    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / labels.size
    gini = 1.0 - np.sum(probabilities ** 2)

    return float(gini)
