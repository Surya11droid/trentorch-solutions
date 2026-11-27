# Stretch: Gaussian Naive Bayes

Intermediate | classical-ml | probabilistic | naive-bayes | stretch

### The problem, from first principles

`02-naive-bayes-bernoulli` modeled each feature as a coin flip, present or absent, a fine model for binary features but useless for real-valued ones. Naive Bayes's core assumption (features are conditionally independent given the class) doesn't care what distribution each feature follows, only that some per-feature probability model is chosen. For continuous features, the classic choice is a Gaussian: assume each feature, within each class, follows its own normal distribution.

### From theory to code

Implement `gaussian_nb_fit`, `gaussian_log_likelihood`, and `gaussian_nb_predict`. `input` is real-valued this time (`02-naive-bayes-bernoulli`'s features were binary), but the overall shape of fitting and prediction is unchanged; only the per-feature probability model itself changes from Bernoulli to Gaussian.

### Constraints

- `gaussian_nb_fit(input, labels, var_smoothing=1e-9)` returns a dict of per-class log-priors, per-feature means, and per-feature variances.
- `var_smoothing` floors every variance above `0`, scaled by the largest per-feature variance across the _entire_ dataset (not per class).
- `gaussian_log_likelihood(x, mean, variance)` returns a single float: the summed log-density across all features.
- `gaussian_nb_predict(model, queries)` returns one predicted class per row of `queries`, by argmax of `log_prior + log_likelihood` over classes.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

The independence assumption is identical to `02-naive-bayes-bernoulli`'s; only the per-feature term inside the sum changes, from a Bernoulli log-probability to a Gaussian log-density.

</details>

<details>
<summary>Hint 2</summary>

`epsilon = var_smoothing * np.var(input, axis=0).max()` computed once over the whole dataset, then added to every class's own per-feature variance, prevents a constant-within-class feature from ever producing a literal `variance = 0`.

</details>
