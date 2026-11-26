
import numpy as np


def pairwise_distances(input, queries):
    diff = queries[:, None, :] - input[None, :, :]
    return np.sqrt(np.sum(diff ** 2, axis=2))


def knn_predict(input, labels, queries, k):
    distances = pairwise_distances(input, queries)

    predictions = []

    for row in distances:
        # Find indices of k nearest neighbors
        indices = np.argsort(row)[:k]

        # Get their corresponding labels
        neighbor_labels = labels[indices]

        # Count each class
        classes, counts = np.unique(
            neighbor_labels,
            return_counts=True
        )

        # Majority vote (ties go to lower class)
        prediction = classes[np.argmax(counts)]

        predictions.append(prediction)

    return np.array(predictions)
