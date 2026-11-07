# Group-By & Aggregation

Intermediate | databases | aggregation

### The problem, from first principles

A table of ten million orders is rarely the answer to a question. Revenue per country, the average basket size per week and the number of customers per plan are. Those are **group-by** questions: split the rows into groups by one or more columns, then collapse each group into a few summary numbers with an aggregate such as a count, a sum or a mean. It is the central operation of reporting and of feature engineering, and it is a hash table in disguise, with one bucket per group. This question builds the operation with several aggregates at once and the filter that applies after grouping.

### From theory to code

Implement `group_by(rows, keys, aggregations)`, which splits rows into groups and computes the requested aggregates for each, then `having(groups, predicate)`, which keeps only groups that satisfy a condition, then `count_distinct(rows, column)`, which counts different values in a column. The signatures and docstrings are already in the editor.

### Constraints

- `rows` is a list of dicts. `keys` is a non-empty list of column names defining the group. `aggregations` is a dict mapping an output column name to a pair `(column, function_name)` where `function_name` is one of `"count"`, `"sum"`, `"mean"`, `"min"`, `"max"`. For `"count"` the column is ignored and the number of rows in the group is returned.
- `group_by` returns a list of dicts, one per distinct combination of the key columns, sorted ascending by the tuple of key values. Each output dict has the key columns, then the aggregate columns in the order of `aggregations`.
- Aggregates ignore rows whose value in the aggregated column is `None`. `"mean"` is the sum divided by the number of non-`None` values. If a group has no non-`None` values for a `sum`, `mean`, `min` or `max`, the result is `None`. `"count"` counts every row, `None` or not.
- An unknown `function_name` raises `ValueError`. An empty table returns `[]`.
- `having(groups, predicate)` returns the list of group dicts for which `predicate(group)` is true, in the original order.
- `count_distinct(rows, column)` returns the number of different non-`None` values in the column, as an int. The input must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

Go through the rows once and keep a dict from the key tuple to the list of rows in that group. A tuple is hashable, so it can be a dict key even when the group is defined by several columns.

</details>

<details>
<summary>Hint 2</summary>

Compute every aggregate from the group's list of values after dropping the `None` values, and handle the empty case once instead of in each branch.

</details>

<details>
<summary>Hint 3</summary>

`having` is the filter that sees the aggregate results. A plain filter on rows before grouping cannot say "only groups with at least five rows".

</details>
