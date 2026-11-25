# Error-ambiguity decomposition

Intermediate | classical-ml | ensembles | diversity

### The problem, from first principles

Why does averaging many models help? The error-ambiguity decomposition gives an exact answer for regression: the averaged ensemble's error equals the models' average error minus how much the models disagree with each other. Disagreement is only useful when the models are still individually accurate.

### From theory to code

Implement `ambiguity_decomposition(predictions, target)` for a simple-average ensemble of regressors, returning the ensemble error, the mean individual error and the ambiguity. Errors are mean squared errors.

### Constraints

- `predictions` has shape `(n_models, n_samples)`; `target` has shape `(n_samples,)`.
- The ensemble prediction is the unweighted mean of the models.
- Return a tuple of three Python floats: `(ensemble_error, mean_individual_error, ambiguity)`.
- Compute all three directly from their definitions, not from the identity.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Ensemble error is the squared error of the averaged prediction. Mean individual error averages the squared error over models _and_ samples.

</details>

<details><summary>Hint 2</summary>

Ambiguity is the average squared distance between each model's prediction and the ensemble's prediction, again over models and samples.

</details>
