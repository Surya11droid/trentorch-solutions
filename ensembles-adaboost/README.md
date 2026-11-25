# AdaBoost: reweighting misclassified samples each round

Intermediate | classical-ml | ensembles | boosting

### The problem, from first principles

A single decision stump (a tree of `max_depth=1`) can only ask one question about one feature before it has to commit to an answer. That makes it a weak learner almost by definition, better than a coin flip, but not by much. `03-gradient-boosting-negative-gradient` and `04-full-boosting-loop` already showed one way to chain weak learners into a strong one: fit each new tree to the previous ensemble's residual. AdaBoost, historically the earlier idea, chains weak learners a different way. It never touches what a tree predicts; it changes which training samples the _next_ tree is trained to care about, by making the hard-to-classify samples louder in the training data each round.

### From theory to code

Theory below derives three things: how much to trust a round's tree (`alpha`), how to make the next round pay more attention to this round's mistakes (the weight update), and how to combine every round's tree into one final prediction. `adaboost_train` runs the round loop and produces the list of `(tree, alpha)` pairs; `adaboost_predict` implements the final weighted vote. Neither reimplements tree-building; both call `03-best-split-minimal-tree`'s `build_tree`/`predict_tree` directly.

### Constraints

- `labels` are `{-1, +1}`-valued, AdaBoost's standard convention, not `{0, 1}`.
- `adaboost_train(input, labels, n_rounds, max_depth=1, seed=None)` returns a `list` of exactly `n_rounds` `(tree, alpha)` pairs, one per round, in round order.
- `max_depth=1` by default: a shallow decision stump, AdaBoost's classic weak learner.
- Sample weights start uniform (`1/n_samples`) and must stay a valid probability distribution (renormalized to sum to `1`) after every round's update.
- Resampling for tree training is done via `rng` built once from `seed` before the loop starts, not re-seeded each round, so results are reproducible for a fixed `seed`.
- The weighted error rate must be clipped away from exactly `0` or `1` before it's used in `alpha`'s formula, to avoid `log(0)` or division by zero.
- `adaboost_predict(ensemble, input)` returns an array of `{-1, +1}` predictions, one per row of `input`, never anything else.
- Reuse `03-best-split-minimal-tree`'s `build_tree`/`predict_tree`, don't reimplement tree construction.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

The weak learner doesn't train on all the data equally every round; it trains on a _resample_ of the data, drawn according to the current sample weights, so heavily-weighted (hard) samples are more likely to appear multiple times. `np.random.Generator.choice` takes a `p=` argument for exactly this.

</details>

<details>
<summary>Hint 2</summary>

The weighted error rate is not computed on the resample; it's measured by running the freshly-trained tree back over the _full_ original `input`/`labels`, then summing the weights of the samples it got wrong. The resample was just a training-time trick; evaluation needs to reflect every sample's true current importance.

</details>

<details>
<summary>Hint 3</summary>

`labels * predictions` is `+1` wherever a prediction agrees with the true label and `-1` wherever it disagrees; that single elementwise product is the entire "did this sample get harder or easier" signal the weight-update formula needs. Feed it straight into `exp(-alpha * labels * predictions)`.

</details>
