# Note: histogram-based boosting (LightGBM-style binning), why it is faster at scale

Beginner | classical-ml | ensembles | gradient-boosting | scalability

### The problem, from first principles

Exact tree search checks boundaries between every distinct feature value. On large continuous datasets that means far too many candidates per node. Histogram search limits each feature to a fixed set of evenly spaced bin boundaries, trading a little precision for predictable work.

### From theory to code

Implement `build_histogram` and `find_best_split_histogram`, using the same information-gain score as exact trees but only interior bin edges as thresholds.

### Constraints

- `build_histogram` returns exactly `n_bins + 1` edges from `values.min()` to `values.max()`.
- Each feature contributes only `n_bins - 1` interior candidate thresholds.
- Skip candidates that leave either child empty.
- Choose only a strictly positive best information gain; otherwise return `None`.
- Reuse `information_gain` and preserve its label partitioning.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

An interval count needs one more edge than the number of intervals.

</details>

<details><summary>Hint 2</summary>

`edges[1:-1]` removes the endpoints that would put all samples on one side.

</details>
