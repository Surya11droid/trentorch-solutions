# CROSS JOIN

Intermediate | db

A T-shirt shop wants a list of every variant it could stock: each color in each size.

Write a query returning every combination of a row from `colors` and a row from `sizes`, with the columns `color` and `size`.

### Constraints

- Columns, in order: `color`, `size`
- Every color paired with every size (2 × 3 = 6 rows here)

### Hints

<details>
<summary>Hint 1</summary>

A cross join needs no `ON` condition.

</details>

<details>
<summary>Hint 2</summary>

Alias both `name` columns, since both tables have one.

</details>
