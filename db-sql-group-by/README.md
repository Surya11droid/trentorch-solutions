# GROUP BY Aggregation

Intermediate | db

The dashboard shows order volume per customer instead of individual orders.

Write a query returning each `user_id` from `orders` together with the number of orders that user placed, named `order_count`.

### Constraints

- Columns, in order: `user_id`, `order_count`
- One row per distinct `user_id`
- Row order does not matter

### Hints

<details>
<summary>Hint 1</summary>

`GROUP BY` forms one group per distinct value of a column.

</details>

<details>
<summary>Hint 2</summary>

Aggregate functions like `COUNT(*)` are computed once per group.

</details>
