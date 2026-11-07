# Joins

Intermediate | databases | joins

### The problem, from first principles

Data lives in separate tables for good reason: customers once, orders many times. Answering a question about both means **joining** them: pair every order with its customer through a shared key. The result is the same however it is computed, but the cost is not. Comparing every row of one table with every row of the other is quadratic and hopeless at scale. Two classic algorithms avoid it, one by building a hash table of one side and one by sorting both sides and walking them together. Choosing between them is a large part of what a query planner does. This question builds all three and shows they agree.

### From theory to code

Implement `nested_loop_join(left, right, key)`, the direct comparison of every pair, then `hash_join(left, right, key)`, which builds a hash table on one side, then `sort_merge_join(left, right, key)`, which sorts both sides and merges them. The signatures and docstrings are already in the editor.

### Constraints

- `left` and `right` are lists of rows, each row a dict. `key` is a column name present in every row of both tables, and key values are comparable and hashable (numbers or strings).
- All three functions perform an **inner join on equality**: for every pair `(l, r)` with `l[key] == r[key]`, the output has one row `{**l, **r}`. If a column name appears in both rows, the value from `r` wins. Rows with no match on the other side do not appear.
- Duplicate keys produce every combination: two left rows and three right rows with the same key give six output rows.
- Output order: `nested_loop_join` and `hash_join` return rows in order of the left table, and for each left row its matches in the order of the right table. `sort_merge_join` returns rows ordered by key ascending, then by left order, then by right order.
- `hash_join` must not compare every pair: build a dict from key to the list of right rows (in right-table order) and probe it once per left row. `sort_merge_join` must sort each side once by key (a stable sort) and advance two positions through them, not compare every pair. The input tables must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

A nested loop is two loops and an `if`. It is the reference answer the other two must agree with.

</details>

<details>
<summary>Hint 2</summary>

For the hash join, group the right rows by key first. Then each left row finds all its partners in one dictionary lookup.

</details>

<details>
<summary>Hint 3</summary>

For the merge join, once both sides are sorted, advance whichever side has the smaller key. When the keys are equal, find the whole run of equal keys on both sides and emit every combination of the two runs.

</details>
