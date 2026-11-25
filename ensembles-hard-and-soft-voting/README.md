# Hard vs. soft voting

Beginner | classical-ml | ensembles | combination-strategies

### The problem, from first principles

Once several classifiers are trained, you still have to turn their separate answers into one. Hard voting counts class votes. Soft voting averages predicted probabilities, so a confident model can outweigh two lukewarm ones.

### From theory to code

Implement `hard_vote(predictions)` and `soft_vote(probabilities, weights=None)`. Both return one predicted class per sample.

### Constraints

- `predictions` has shape `(n_models, n_samples)` and holds integer class labels.
- `probabilities` has shape `(n_models, n_samples, n_classes)`; `weights` is an optional length-`n_models` array.
- On a hard-vote tie, return the smallest label. On a soft-vote tie, return the smallest class index.
- Return integer NumPy arrays of length `n_samples`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

For hard voting, `np.unique(column, return_counts=True)` lists labels in sorted order, so `np.argmax` over the counts already breaks ties toward the smallest label.

</details>

<details><summary>Hint 2</summary>

For soft voting, average over the model axis first (weighted if weights are given, divided by their sum), then take `argmax` over the class axis.

</details>
