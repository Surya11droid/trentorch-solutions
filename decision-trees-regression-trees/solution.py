
import numpy as np


# 1. Calculate variance
def variance(targets):

    targets = np.asarray(targets, dtype=float)

    if len(targets) == 0:
        return 0.0

    mean = np.mean(targets)

    return float(np.mean((targets - mean) ** 2))


# 2. Calculate variance reduction
def variance_reduction(parent, left, right):

    parent = np.asarray(parent, dtype=float)
    left = np.asarray(left, dtype=float)
    right = np.asarray(right, dtype=float)

    n = len(parent)

    if n == 0:
        return 0.0

    weighted_child_variance = (
        (len(left) / n) * variance(left)
        +
        (len(right) / n) * variance(right)
    )

    return variance(parent) - weighted_child_variance


# 3. Find the best regression split

def find_best_regression_split(X, targets):

    X = np.asarray(X, dtype=float)
    targets = np.asarray(targets, dtype=float)

    # No possible improvement with constant targets
    if len(targets) == 0 or variance(targets) == 0.0:
        return None

    best_reduction = 0.0
    best_feature = None
    best_threshold = None

    for feature in range(X.shape[1]):

        values = np.unique(X[:, feature])

        for i in range(len(values) - 1):

            threshold = (values[i] + values[i + 1]) / 2

            left_mask = X[:, feature] <= threshold
            right_mask = X[:, feature] > threshold

            left = targets[left_mask]
            right = targets[right_mask]

            if len(left) == 0 or len(right) == 0:
                continue

            reduction = variance_reduction(
                targets, left, right
            )

            if reduction > best_reduction:
                best_reduction = reduction
                best_feature = feature
                best_threshold = float(threshold)

    if best_feature is None:
        return None

    return best_feature, best_threshold, best_reduction


# 4. Build regression tree recursively
def build_regression_tree(X, targets, max_depth):

    X = np.asarray(X, dtype=float)
    targets = np.asarray(targets, dtype=float)

    # Stopping conditions
    if (
        max_depth == 0
        or len(targets) < 2
        or variance(targets) == 0.0
    ):
        return {
            "leaf": True,
            "prediction": float(np.mean(targets))
        }

    # Find best split
    feature, threshold, reduction = find_best_regression_split(
        X, targets
    )

    # No valid split
    if feature is None:
        return {
            "leaf": True,
            "prediction": float(np.mean(targets))
        }

    # Divide dataset
    left_mask = X[:, feature] <= threshold
    right_mask = X[:, feature] > threshold

    # Build child trees
    left_tree = build_regression_tree(
        X[left_mask],
        targets[left_mask],
        max_depth - 1
    )

    right_tree = build_regression_tree(
        X[right_mask],
        targets[right_mask],
        max_depth - 1
    )

    return {
        "leaf": False,
        "feature": feature,
        "threshold": threshold,
        "left": left_tree,
        "right": right_tree
    }


# 5. Predict using regression tree
def predict_regression_tree(tree, X):

    X = np.asarray(X, dtype=float)

    predictions = []

    for row in X:

        node = tree

        # Traverse until leaf
        while not node["leaf"]:

            feature = node["feature"]
            threshold = node["threshold"]

            if row[feature] <= threshold:
                node = node["left"]
            else:
                node = node["right"]

        predictions.append(float(node["prediction"]))

    return np.array(predictions, dtype=float)
