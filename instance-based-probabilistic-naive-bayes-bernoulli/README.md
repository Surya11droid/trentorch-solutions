# Naive Bayes: Bernoulli log-likelihood

Intermediate | classical-ml | probabilistic | naive-bayes

### The problem, from first principles

`01-knn` predicts by comparing distances directly; it never asks "how likely is this class, probabilistically." Naive Bayes takes a fully probabilistic approach instead: given a document represented as which words appear in it (`input` entries of `0`/`1`, "does this word appear"), model how likely each class is given those features, and pick whichever class is most likely. The catch is that estimating "how likely are these exact features together, given the class" directly is hopeless, with enough binary features there are more possible feature combinations than there are training examples to have ever seen most of them. Naive Bayes sidesteps this with one deliberately simplifying assumption: treat every feature as independent of every other feature, once you already know the class.

### From theory to code

Theory below derives, from Bayes' rule plus that independence assumption, a log-space formula for how well a class explains a set of features, and how Laplace smoothing keeps that formula from breaking on features that happen to be constant within a class. `bernoulli_nb_fit` estimates the per-class, per-feature probabilities and priors from training data; `bernoulli_log_likelihood` scores one sample's features against one class's probabilities; `bernoulli_nb_predict` combines both to pick the best class per query.

### Constraints

- `input` entries are `0` or `1` (feature present/absent); `labels` can be any set of class values, not necessarily `{0, 1}`.
- `bernoulli_nb_fit(input, labels, alpha=1.0)` returns a `dict` with `"classes"`, `"log_priors"` (a `{class: float}` mapping), and `"feature_probs"` (a `{class: array of shape (n_features,)}` mapping).
- `alpha` is Laplace smoothing strength, added to the numerator; `2 * alpha` (not `alpha`) is added to the denominator when estimating each `feature_probs[c]`.
- `bernoulli_log_likelihood(x, feature_probs)` takes one sample's features (shape `(n_features,)`) and one class's feature probabilities (same shape), returns a single `float`.
- `bernoulli_nb_predict(model, queries)` returns shape `(n_queries,)`, one predicted class per row of `queries`, chosen by highest `log_prior + log_likelihood` score, never by comparing raw (non-log) probabilities.
- Every computation stays in log space once priors and likelihoods are combined; never multiply raw probabilities together, that underflows for more than a handful of features.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`feature_probs[c]` is one array covering every feature at once for class `c`; you don't need a per-feature loop. `input[mask].sum(axis=0)` (where `mask` selects class `c`'s rows) counts, per feature, how many of class `c`'s examples had that feature present.

</details>

<details>
<summary>Hint 2</summary>

`bernoulli_log_likelihood`'s formula has two terms per feature, and exactly one of them is "active" per feature depending on whether `x_i` is `0` or `1`. Instead of branching, multiply each term by `x` or `(1 - x)`; the inactive term gets multiplied by `0` and vanishes on its own.

</details>

<details>
<summary>Hint 3</summary>

`bernoulli_nb_predict` needs to compare each query against _every_ class's `(log_prior, feature_probs)` pair and keep the best. Build a list or array of scores across `model["classes"]` for one query, then `np.argmax` picks the winning class index directly.

</details>
