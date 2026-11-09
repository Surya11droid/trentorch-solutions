# HAVING Filtering Groups

Intermediate | db

Marketing wants repeat customers only: users who placed **more than one** order.

Write a query returning `user_id` and `order_count` for the users that have more than 1 order, using `GROUP BY` and `HAVING`.

### Constraints

- Columns, in order: `user_id`, `order_count`
- Only groups whose count is greater than 1

### Hints

<details>
<summary>Hint 1</summary>

`WHERE` cannot see aggregate results; `HAVING` can.

</details>

<details>
<summary>Hint 2</summary>

`HAVING COUNT(*) > 1` goes right after `GROUP BY`.

</details>
