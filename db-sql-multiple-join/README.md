# MULTIPLE JOIN

Intermediate | db

An order only stores ids: the buyer's `user_id` and the `product_id`. To produce a readable order list you must join **three** tables: `orders`, `users` and `products`.

Write a query returning the buyer's name as `user_name`, the product's name as `product_name`, and the order's `quantity`.

### Constraints

- Columns, in order: `user_name`, `product_name`, `quantity`
- Join all three tables (one row per order)
- Both `users.name` and `products.name` need aliases because the names collide

### Hints

<details>
<summary>Hint 1</summary>

Start from `orders` and add one `JOIN ... ON` per table.

</details>

<details>
<summary>Hint 2</summary>

Both `users` and `products` have a `name` column; give each output column a distinct alias.

</details>
