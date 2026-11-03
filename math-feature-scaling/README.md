# Feature Scaling

Intermediate | data-processing

### The problem, from first principles

A dataset with "age in years" (roughly 0-100) and "income in dollars" (roughly 0-500,000) hands a model two features on wildly different scales. Gradient descent (`04-gd-step`) takes one learning rate for ALL parameters, but a small step for the income-weight moves the prediction a huge amount (income values are huge), while the same-sized step for the age-weight barely does anything, the loss surface is a long, thin, badly-conditioned valley instead of a nice round bowl and training crawls or oscillates. Distance-based methods (`01-knn`, later in Classical ML) have an even more direct problem: "distance" between two points is dominated entirely by whichever feature happens to have the largest raw numeric range, regardless of which feature actually matters more.

Feature scaling fixes both problems by putting every feature on a comparable numeric footing before training ever starts. This question implements the two standard approaches and sets up the exact "fit on training data only" discipline `04-data-leakage`, later in this track, treats as a hard requirement, not a suggestion.

### From theory to code

Theory gives two rescaling formulas, standardization (mean 0, std 1) and min-max normalization (squashed into `[0, 1]`) and both need to work in two modes: computing scaling parameters fresh from a dataset, or REUSING previously-computed parameters on new data.

Implement `standardize(x, mean=None, std=None)` and `min_max_normalize(x, min_val=None, max_val=None)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

- Both functions compute per-column (per-feature) statistics, `axis=0`, not a single global statistic across the whole array.
- If the relevant parameters (`mean`/`std`, or `min_val`/`max_val`) are supplied, use them as-is, don't recompute from `x`.
- Both return a 3-tuple: `(scaled_x, param1, param2)`, so a caller can reuse the returned parameters later.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.mean(x, axis=0)` and `np.std(x, axis=0)` give one number per column, exactly the per-feature statistics both formulas need.

</details>

<details>
<summary>Hint 2</summary>

Check `if mean is None` (and similarly for the other parameters) before computing, if a caller already supplied a value, don't overwrite it.

</details>
