
import numpy as np

# Import or reuse build_tree and predict_tree
# from your existing decision-tree implementation


def adaboost_train(
    input,
    labels,
    n_rounds,
    max_depth=1,
    seed=None
):
    input = np.asarray(input)
    labels = np.asarray(labels)

    n_samples = len(labels)

    # Initially every sample has equal weight
    weights = np.ones(n_samples) / n_samples

    # One RNG for all rounds
    rng = np.random.default_rng(seed)

    ensemble = []

    for _ in range(n_rounds):

        # Resample according to current sample weights
        indices = rng.choice(
            n_samples,
            size=n_samples,
            replace=True,
            p=weights
        )

        X_sample = input[indices]
        y_sample = labels[indices]

        # Train a weak learner
        tree = build_tree(
            X_sample,
            y_sample,
            max_depth=max_depth
        )

        # Predict on original training data
        predictions = np.asarray(
            predict_tree(tree, input)
        )

        # Calculate weighted error
        incorrect = predictions != labels
        error = np.sum(weights * incorrect)

        # Avoid log(0) and division by zero
        error = np.clip(error, 1e-10, 1 - 1e-10)

        # Calculate tree importance
        alpha = 0.5 * np.log((1 - error) / error)

        ensemble.append((tree, alpha))

        # Update sample weights
        weights *= np.exp(-alpha * labels * predictions)

        # Normalize weights
        weights /= np.sum(weights)

    return ensemble


def adaboost_predict(ensemble, input):

    input = np.asarray(input)

    # Accumulate weighted predictions
    scores = np.zeros(len(input))

    for tree, alpha in ensemble:

        predictions = predict_tree(tree, input)

        scores += alpha * np.asarray(predictions)

    # Convert scores into -1 or +1
    return np.where(scores >= 0, 1, -1)
