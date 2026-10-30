# GroupBy & Aggregation

Intermediate | data-science | pandas | groupby | aggregation

### The problem, from first principles

Almost every real question about a table is a question about _groups_: average salary **per department**, orders **per customer**, the best-selling product **per month**. The idea behind all of them is the same three steps, usually called split-apply-combine. Split the rows into groups by a key. Apply something to each group. Combine the results back into one table.

What you _apply_ decides the shape of the answer, and that is the part that trips people. Aggregating (a mean) collapses each group to one row. Transforming (the group's mean written next to every member) keeps every row. Selecting (the top two per group) keeps some rows. This question builds one of each, and a fourth, a within-group z-score, that needs a transform with a spread.

### From theory to code

Implement `group_summary(df, key, value)`, `add_group_mean(df, key, value)`, `zscore_within_group(df, key, value)` and `top_n_per_group(df, key, value, n)`. The signatures and docstrings are already in the editor.

### Constraints

- Rows whose `key` is missing belong to no group: they are left out of every group statistic.
- `group_summary(df, key, value)` returns a frame **indexed by the distinct keys, sorted ascending**, with the columns `n` (count of non-missing `value`s, integer), `mean`, `median` and `max` of `value`, in that order. A group whose values are all missing still appears, with `n = 0` and `NaN` statistics.
- `add_group_mean(df, key, value)` returns a **copy** of `df` with one new column, `<value>_group_mean`, holding the mean of `value` over the row's group (missing values ignored). Rows with a missing key get `NaN`. The original frame is not changed.
- `zscore_within_group(df, key, value)` returns a float Series with `df`'s index: `(value - group mean) / group std`, with the **sample** standard deviation (divide by `n - 1`). It is `NaN` where the value is missing, the group has one value, the standard deviation is `0`, or the key is missing.
- `top_n_per_group(df, key, value, n)` returns, for each key, the `n` rows with the largest `value` (ties keep their original order; rows with a missing key or value are ignored). The result has all of `df`'s columns and original index labels, ordered by key ascending, then by `value` descending within a key.

### Hints

<details>
<summary>Hint 1</summary>

`groupby(key)[value].agg(...)` accepts named aggregations such as `n="count"`.

</details>

<details>
<summary>Hint 2</summary>

`transform` returns a result the same length as the input, aligned to the original rows. That is what lets a group statistic sit next to each member.

</details>

<details>
<summary>Hint 3</summary>

For the top rows of each group, sort by `value` descending first, then take the first `n` of every group with `groupby(...).head(n)`.

</details>
