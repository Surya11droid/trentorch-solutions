# INNER JOIN Combining Tables

Intermediate | db

Your shop has two tables: `users` (id, name) and `orders` (id, user_id, product). To display an order together with the customer's name you must match each order's `user_id` to a user's `id`. Orders that point to a user who does not exist (order 4 here) should not be listed.

Write a query returning `orders.user_id`, `orders.product` and `users.name` for every order that has a matching user (an inner join).

### Constraints

- Columns, in order: `user_id`, `product`, `name`
- Only orders that have a matching user (inner join)
- Row order does not matter

### Hints

<details>
<summary>Hint 1</summary>

`JOIN ... ON` connects rows from two tables where the condition is true.

</details>

<details>
<summary>Hint 2</summary>

Table aliases (`orders o`, `users u`) keep long conditions short.

</details>
