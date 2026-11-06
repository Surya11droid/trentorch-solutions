
import numpy as np

def feature_target_correlations(x, target):
    x = np.asarray(x)
    target = np.asarray(target)

    correlations = []

    for i in range(x.shape[1]):
        corr = np.corrcoef(x[:, i], target)[0, 1]
        correlations.append(corr)

    return np.array(correlations)


def find_suspicious_features(x, target, threshold=0.95):
    correlations = feature_target_correlations(x, target)

    return np.where(np.abs(correlations) >= threshold)[0]
