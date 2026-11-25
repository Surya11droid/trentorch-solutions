# Stretch: regularized boosting (shrinkage + L2 leaf penalty, XGBoost-style)

Advanced | classical-ml | ensembles | gradient-boosting | regularization | stretch

### The problem, from first principles

`04-full-boosting-loop` fit every tree greedily: split on whichever feature/threshold reduces variance the most, set each leaf to the mean residual, and repeat. That works, but nothing in it stops a leaf from fitting itself to three noisy points with an extreme value, or a split from looking great only because it isolates a tiny, easily-overfit corner of the data. `06-ridge-regularization` already dealt with an analogous problem for linear weights, add a penalty so an extreme parameter has to earn its size, not just track noise. XGBoost applies the same idea to leaf values in a boosted tree, and derives both a leaf's value and a split's quality directly from the loss function instead of borrowing CART's variance-reduction criterion by convention.

### From theory to code

Theory below derives, from squared-error loss, the closed-form regularized leaf value and the closed-form regularized split gain; both in terms of each sample's gradient and hessian. `xgboost_leaf_value` and `xgboost_split_gain` implement those two formulas directly; `find_best_regularized_split` and `build_regularized_tree` reuse `05-regression-trees`'s tree-building shape with those formulas swapped in for variance reduction and the mean; `train_regularized_boosting`/`predict_regularized_boosting` reuse `04-full-boosting-loop`'s accumulation loop, computing gradients and hessians for squared-error loss each round.

### Constraints

- Squared-error loss throughout: `gradients = predictions - targets` (the derivative of `0.5*(prediction-target)^2` w.r.t. `prediction`), `hessians` are constant `1.0` per sample, every round.
- `xgboost_leaf_value(gradients, hessians, lam)` returns a single `float`: `-sum(gradients) / (sum(hessians) + lam)`.
- `xgboost_split_gain(gradients, hessians, left_mask, lam)` returns a single `float`, using the _parent's_ full gradient/hessian sums together with the left/right sums split by `left_mask`.
- `find_best_regularized_split` returns `None` if no feature has at least 2 distinct values (no valid threshold exists), otherwise `(feature, threshold, gain)` for the best split found, same candidate-threshold search as `05-regression-trees`.
- `build_regularized_tree` recursion stops (returns a leaf) at `max_depth == 0`, fewer than 2 samples, or when `find_best_regularized_split` returns `None`; never split further than that.
- `lam=0` must reduce to (numerically match, within floating-point tolerance) plain unregularized boosting; this is a real sanity check the tests enforce, not a coincidence.
- Reuse `05-regression-trees`'s `predict_regression_tree` for prediction; tree traversal doesn't change, only how leaves and splits are computed at training time.
- `train_regularized_boosting` returns `(initial_prediction, trees)` where `initial_prediction = mean(targets)`; `predict_regularized_boosting` replays `initial_prediction + learning_rate * sum of each tree's prediction`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Both formulas only ever need _sums_ of gradients and hessians; the total, the left-side sum, and the right-side sum. Compute those three pairs once (`G`/`H`, `G_left`/`H_left`, `G_right`/`H_right`) and everything else is arithmetic on scalars.

</details>

<details>
<summary>Hint 2</summary>

`lam` always sits in the denominator, added to a hessian sum, never touching a gradient sum directly. If your leaf value or gain formula adds `lam` anywhere else (to `G`, or outside the fraction), it will pass the `lam=0` case but fail as soon as `lam` actually matters.

</details>

<details>
<summary>Hint 3</summary>

`train_regularized_boosting`'s gradient is `predictions - targets`, not `targets - predictions`. Get the sign backwards and `xgboost_leaf_value`'s `-G/(H+lam)` will push every leaf the wrong direction; the model will get worse every round instead of better.

</details>
