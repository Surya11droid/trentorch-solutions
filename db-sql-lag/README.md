# LAG: Access Previous Row

Advanced | db

A finance report compares each month's revenue with the month before. The first month has no previous value, so it shows NULL.

Write a query returning `month`, `revenue` and the previous month's revenue as `prev_revenue`, using `LAG()`, with the rows ordered by `month`.

### Constraints

- Columns, in order: `month`, `revenue`, `prev_revenue`
- The first month's `prev_revenue` is NULL
- Rows ordered by `month` ascending

### Hints

<details>
<summary>Hint 1</summary>

`LAG(column) OVER (ORDER BY ...)` reads the value from the previous row.

</details>

<details>
<summary>Hint 2</summary>

Add a normal `ORDER BY month` at the end to order the output.

</details>
