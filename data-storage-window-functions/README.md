# Window Functions

Intermediate | databases | window-functions

### The problem, from first principles

`02-group-by` collapses each group to a single row. Many questions need the opposite: keep every row and attach a number computed from its neighbours. The running total of an account balance, the rank of each salary within a department, the change from the previous day, a seven-day moving average. These are **window functions**. Each row looks at a window of related rows (its own partition, up to the current position) and computes a value without removing any row. They are among the most useful and most misread tools in SQL, and the same logic builds time-series features for models. This question builds the four most common ones over rows that are already in order.

### From theory to code

Implement `running_sum(values, partitions)`, a cumulative total that restarts in each partition, then `rank(values, partitions)`, the standard competition ranking within each partition, then `lag(values, partitions, offset, default)`, the value from an earlier row in the same partition, then `moving_average(values, window)`, the average of the last few values. The signatures and docstrings are already in the editor.

### Constraints

- `values` and `partitions` are lists of the same length, in the **row order** of the table (the order the window follows). `partitions[i]` is the partition label of row `i`. Rows of one partition may be interleaved with others, and within a partition the order is the row order.
- `running_sum(values, partitions)` returns a list where entry `i` is the sum of `values[j]` over rows `j <= i` in the same partition as row `i`.
- `rank(values, partitions)` returns a list of ranks where entry `i` is `1 + (number of rows in the same partition with a strictly larger value)`: the highest value has rank 1, **ties share a rank and the next rank is skipped** (values 9, 9, 7 have ranks 1, 1, 3).
- `lag(values, partitions, offset, default)` returns a list where entry `i` is the value of the row `offset` rows earlier **within the same partition**, or `default` if there is no such row. `offset >= 1`.
- `moving_average(values, window)` ignores partitions and returns a list of floats where entry `i` is the mean of `values[max(0, i - window + 1) : i + 1]`, so early entries average over fewer values. `window >= 1`.
- Inputs must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

Keep one running state per partition in a dict, updated as you walk the rows in order. A row only ever needs the state of its own partition.

</details>

<details>
<summary>Hint 2</summary>

For `lag`, keep the list of values seen so far in each partition. The value `offset` rows back is at position `len(seen) - offset`, if that position exists.

</details>

<details>
<summary>Hint 3</summary>

Rank counts how many values in the partition beat this one, which is why equal values get the same rank and leave a gap after them.

</details>
