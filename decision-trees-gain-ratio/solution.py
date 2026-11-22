
import numpy as np

def entropy(labels):
    if len(labels) == 0:
        return 0.0

    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)

    return float(-np.sum(
        probabilities * np.log2(probabilities)
    ))


def gain_ratio(feature, labels):
    feature = np.asarray(feature)
    labels = np.asarray(labels)

    if len(feature) == 0:
        return 0.0
    values, counts = np.unique(feature, return_counts=True)
    if len(values) == 1:
        return 0.0

    total = len(labels)

    parent_entropy = entropy(labels)
    child_entropy = 0.0
    split_info = 0.0

    for value, count in zip(values, counts):

        # Select labels belonging to this feature value
        group = labels[feature == value]

        probability = count / total

        # Weighted entropy of child group
        child_entropy += probability * entropy(group)

        # Intrinsic value
        split_info -= probability * np.log2(probability)

    # Information gain
    information_gain = parent_entropy - child_entropy

    # Gain ratio
    if split_info == 0:
        return 0.0

    return float(information_gain / split_info)
