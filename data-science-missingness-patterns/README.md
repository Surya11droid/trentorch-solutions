# Missingness Patterns

Intermediate | data-science | data-cleaning

### The problem, from first principles

`01-missing-values` finds the gaps in a dataset and fills them with a column average. That treats every gap the same, and the right treatment depends on why the value is missing. If a sensor drops readings at random, filling with the mean is harmless. If it drops readings mostly on hot days, the missing rows are systematically different from the rest, and filling them with the overall mean quietly biases every model trained on the result. This question builds the checks that tell those cases apart, and the indicator column that lets a model use the fact that a value was missing.

### From theory to code

Implement `missingness_rate_by_group(x, groups)`, the fraction of missing values within each group, then `mean_by_missingness(target, other)`, the average of another column split by whether the target is missing, then `likely_mechanism(target, other, threshold)`, a rough verdict on whether the gaps look random, then `add_missing_indicators(x)`, which appends a 0/1 flag column for every column that has gaps. The signatures and docstrings are already in the editor.

### Constraints

- Missing values are `np.nan`. `x`, `target` and `other` are float arrays; `groups` is a 1D array of any hashable labels with the same length as `x`.
- `missingness_rate_by_group` returns a dict mapping every label that appears in `groups` to the fraction of that group's entries that are missing. A group whose entries are all present has rate `0.0`.
- `mean_by_missingness` returns `(mean_when_observed, mean_when_missing)` as floats, where each is the mean of `other` over the rows where `target` is present or missing. `other` has no missing values. If either set of rows is empty, that mean is `nan`.
- `likely_mechanism` returns `"MCAR-like"` when the absolute gap between the two means, divided by the standard deviation of `other` over all rows, is below `threshold` and `"MAR-like"` otherwise. It returns `"MCAR-like"` when there are no missing values at all, and when `other` has zero standard deviation.
- `add_missing_indicators` returns a new 2D array: the original columns unchanged (with their `nan`), followed by one column of `1.0`/`0.0` flags for each original column that contains at least one missing value, in the original column order. Columns with no gaps get no flag. `x` must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

A boolean mask from `np.isnan` splits the rows of `other` into two groups. The two means being close is what "the gaps do not depend on `other`" looks like in the data.

</details>

<details>
<summary>Hint 2</summary>

Dividing the gap between the two means by the spread of `other` makes the comparison unit-free, so the same threshold works for a column measured in dollars or in degrees.

</details>

<details>
<summary>Hint 3</summary>

To build the indicators, find which columns have any missing value first, then stack their masks (converted to floats) to the right of the original array.

</details>
