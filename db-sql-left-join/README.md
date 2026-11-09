# LEFT JOIN Preserving Left Table

Intermediate | db

The analytics page lists every user with the number of orders they have placed. Users who have never ordered must still appear, with a count of 0.

Write a query returning `users.id`, `users.name` and the number of their orders as `order_count`, using a `LEFT JOIN` and `GROUP BY`.

### Constraints

- Columns, in order: `id`, `name`, `order_count`
- Include users with no orders (count 0)
- One row per user

### Hints

<details>
<summary>Hint 1</summary>

`LEFT JOIN` keeps every row of the left table even without a match.

</details>

<details>
<summary>Hint 2</summary>

Count a column of the _orders_ table: `COUNT(*)` would count the NULL-filled row as 1.

</details>
