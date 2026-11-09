# SUM with GROUP BY

Intermediate | db

The sales dashboard shows revenue per region.

Write a query returning each `region` of `sales` and the sum of its `amount` values, named `total_revenue`.

### Constraints

- Columns, in order: `region`, `total_revenue`
- One row per region

### Hints

<details>
<summary>Hint 1</summary>

`SUM(amount)` adds up numbers; combine it with `GROUP BY region`.

</details>

<details>
<summary>Hint 2</summary>

Give the sum an alias with `AS total_revenue`.

</details>
