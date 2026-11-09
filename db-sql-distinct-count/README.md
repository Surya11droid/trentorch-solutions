# DISTINCT COUNT

Intermediate | db

The sales report headline says "orders from N customers". There are six orders, but several customers ordered more than once, so counting rows overstates N.

Write a query returning a single value, the number of distinct `user_id`s in `orders`, named `customer_count`.

### Constraints

- Return a single row with the column `customer_count`
- Each customer counts once however many orders they placed

### Hints

<details>
<summary>Hint 1</summary>

`COUNT(DISTINCT column)` counts unique values.

</details>

<details>
<summary>Hint 2</summary>

`COUNT(*)` would return 6, the number of orders.

</details>
