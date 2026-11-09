# ROW_NUMBER: Unique Sequential Numbering

Advanced | db

To paginate a list ("page 1 is rows 1-10") you need a stable, unique position for every row. Users must be numbered by age, youngest first, and when two users have the same age the one with the smaller `id` comes first, so the numbering never changes between runs.

Write a query returning `name`, `age` and the position as `row_num` using `ROW_NUMBER()`.

### Constraints

- Columns, in order: `name`, `age`, `row_num`
- `row_num` goes 1, 2, 3, ... with no repeats
- Order by `age` ascending, ties by `id` ascending

### Hints

<details>
<summary>Hint 1</summary>

`ROW_NUMBER() OVER (ORDER BY ...)` numbers rows in the given order.

</details>

<details>
<summary>Hint 2</summary>

Add `id` as a second sort key to make ties deterministic.

</details>
