# Weighted majority vote

Beginner | classical-ml | supervised | ensembles | voting

### Trust some voters more

In a plain majority vote every classifier counts equally. A weighted vote lets stronger classifiers count more, for example by giving each one a weight based on its validation accuracy.

Implement `weighted_majority_vote(predictions, weights)`.

- `predictions` has shape `(m, n)`: `m` classifiers voting on `n` samples, with integer labels `0, 1, 2, …`.
- `weights` has length `m` and must be nonnegative.
- For each sample, add each classifier's weight to the total for the label it predicts. The winning label is the one with the largest total.
- Ties go to the smaller label.

Return an integer array of length `n`.

### Constraints

- Negative weights raise `ValueError`.
- If the weights sum to zero, raise `ValueError`.
- `len(weights)` must equal the number of rows in `predictions`, otherwise raise `ValueError`.
- Do not modify the inputs.

### Hints

<details>
<summary>Hint 1</summary>

Build a `(n, classes)` score matrix and add each weight into the column of the label it votes for.

</details>
