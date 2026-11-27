
import numpy as np


def gaussian_nb_fit(input, labels, var_smoothing=1e-9):

    input = np.asarray(input, dtype=float)
    labels = np.asarray(labels)

    classes = np.unique(labels)
    global_max_variance = np.var(input, axis=0).max()

    epsilon = var_smoothing * global_max_variance
    epsilon = max(epsilon, np.finfo(float).eps)

    log_priors = {}
    means = {}
    variances = {}

    for cls in classes:
        X_class = input[labels == cls]
        prior = len(X_class) / len(input)
        log_priors[cls] = np.log(prior)
        means[cls] = np.mean(X_class, axis=0)
        var = np.var(X_class, axis=0)


        variances[cls] = np.maximum(var, epsilon)

    return {
        "classes": classes,
        "log_priors": log_priors,
        "means": means,
        "variances": variances
    }


def gaussian_log_likelihood(x, mean, variance):

    x = np.asarray(x)
    mean = np.asarray(mean)
    variance = np.asarray(variance)

    log_density = -0.5 * (
        np.log(2 * np.pi * variance)
        + ((x - mean) ** 2) / variance
    )

    return float(np.sum(log_density))


def gaussian_nb_predict(model, queries):

    queries = np.asarray(queries, dtype=float)

    predictions = []

    for x in queries:

        scores = []

        for cls in model["classes"]:


            prior = model["log_priors"][cls]
            mean = model["means"][cls]
            variance = model["variances"][cls]


            likelihood = gaussian_log_likelihood(
                x, mean, variance
            )


            score = prior + likelihood

            scores.append(score)


        predicted_class = model["classes"][np.argmax(scores)]

        predictions.append(predicted_class)

    return np.array(predictions)
