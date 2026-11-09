# RIGHT JOIN

Intermediate | db

A data-integrity report lists **every order**, together with the buyer's name when the buyer exists. Order 4 refers to user 99, who is not in `users`; it must still be listed, with a NULL name. Users who have placed no orders are not part of this report.

Write a query returning `orders.id` as `order_id` and `users.name`, keeping every order, using a `RIGHT JOIN` with `users` on the left and `orders` on the right.

### Constraints

- Columns, in order: `order_id`, `name`
- Every order appears once, even without a matching user
- Use `users` as the left table and `orders` as the right table

### Hints

<details>
<summary>Hint 1</summary>

A right join keeps all rows from the table written _after_ `JOIN`.

</details>

<details>
<summary>Hint 2</summary>

`FROM users u RIGHT JOIN orders o ON ...`

</details>
