# Full boosting loop: assemble a minimal booster

Advanced | classical-ml | ensembles | gradient-boosting

### The problem, from first principles

One residual tree makes one correction. A booster chains many such corrections, with each new tree seeing what every earlier tree still missed. The fitted model must also replay that same ordered, scaled sequence for unseen inputs.

### From theory to code

Implement `train_gradient_boosting` and `predict_gradient_boosting` using the existing residual-tree fitter and regression-tree predictor.

### Constraints

- Initialize with `float(np.mean(targets))` and one copy per training row.
- Fit exactly `n_trees` sequential residual trees; zero trees return an empty list.
- Scale every tree contribution by `learning_rate` during training and prediction.
- Return `(initial_prediction, trees)` and preserve tree order.
- Prediction starts from the same scalar for every new input row.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

The next tree must observe the updated predictions, not the original constant prediction.

</details>

<details><summary>Hint 2</summary>

Training and inference differ only in where the initial prediction and trees came from; both add the same scaled tree outputs in order.

</details>
