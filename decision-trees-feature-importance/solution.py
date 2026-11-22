import numpy as np

def feature_importances(tree, input, labels, n_features):

    importances = np.zeros(n_features)
    total_samples = len(labels)

    def traverse(node, X, y):
        if node["leaf"]:
            return
        feature = node["feature"]
        threshold = node["threshold"]
        left_mask = X[:, feature] <= threshold
        right_mask = ~left_mask
        left_X = X[left_mask]
        right_X = X[right_mask]

        left_y = y[left_mask]
        right_y = y[right_mask]

        
        gain = information_gain(y, left_y, right_y)

        contribution = (len(y) / total_samples) * gain

        importances[feature] += contribution

        traverse(node["left"], left_X, left_y)
        traverse(node["right"], right_X, right_y)

    traverse(tree, input, labels)

    total_importance = np.sum(importances)

    if total_importance > 0:
        importances = importances / total_importance

    return importances
