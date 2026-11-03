# Feature Selection

Intermediate | data-science | feature-selection

### The problem, from first principles

`05-feature-engineering` adds columns. Past some point more columns hurt: a feature that never changes carries no information, two features that move together carry the same information twice, and a pile of noisy features gives a model more ways to fit chance patterns in the training set. Feature selection removes columns before any model is trained, using cheap statistics of the data itself. This question builds three of the standard filters: drop columns that barely vary, drop one of each pair of near-duplicate columns, and keep only the columns most related to the label.

### From theory to code

Implement `variance_threshold(x, threshold)`, which finds the columns that vary enough, then `drop_correlated(x, threshold)`, which removes redundant columns, then `select_k_best(x, y, k)`, which ranks columns by how strongly they relate to the label. The signatures and docstrings are already in the editor.

### Constraints

- `x` is a 2D float array `(rows, columns)` with no missing values. `y` is a 1D float array with one entry per row.
- `variance_threshold` returns a boolean array of length `columns`, `True` where the column's population variance is strictly greater than `threshold`.
- `drop_correlated` returns the sorted list of column indices to keep. It scans columns left to right and keeps a column unless its absolute Pearson correlation with some already-kept column is strictly greater than `threshold`. A constant column has undefined correlation, which counts as `0`, so it is never dropped by this rule.
- `select_k_best` returns an integer array of the `k` column indices with the highest absolute Pearson correlation with `y`, ordered from strongest to weakest. Ties go to the lower column index. A constant column scores `0`. `k` is at most the number of columns.
- Inputs must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

Correlation of two columns is the covariance divided by the product of the standard deviations. Compute the standard deviations once and treat a zero standard deviation as a correlation of zero instead of dividing by it.

</details>

<details>
<summary>Hint 2</summary>

For `drop_correlated`, the order of the scan decides which of two correlated columns survives: the earlier one always does.

</details>

<details>
<summary>Hint 3</summary>

`np.argsort` on the negated scores is stable, so equal scores keep their original column order, which is exactly the tie rule.

</details>
