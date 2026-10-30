# Merge & Join

Intermediate | data-science | pandas | merge | join

### The problem, from first principles

Real data lives in several tables: customers in one, their orders in another, the products in a third. Combining them is what a `merge` (SQL's `JOIN`) does, and most of the ways it goes wrong are silent. Rows vanish because a key had no partner. Rows multiply because a key had _two_ partners. A "left" join keeps a customer who never ordered, but fills their order columns with `NaN`, and an `int` count turns into a `float`.

This question builds the four join questions an analyst is asked constantly: the orders with their customer, every customer with their order totals (including those with none), the customers who never ordered (an anti-join), and a merge that refuses to run if it would multiply rows by accident.

### From theory to code

Implement `orders_with_customers(customers, orders)`, `customer_totals(customers, orders)`, `customers_without_orders(customers, orders)` and `safe_merge(left, right, key)`. The signatures and docstrings are already in the editor.

### Constraints

- `customers` has columns `id` (unique), `name`, `city`. `orders` has `order_id` (unique), `customer_id`, `amount`. Keys are never missing. An order may refer to a customer that does not exist.
- `orders_with_customers(customers, orders)` is the **inner** join of the two tables on `orders.customer_id == customers.id`. It returns only the columns `order_id`, `customer_id`, `name`, `amount` (in that order), sorted by `order_id`, with a fresh `0..n-1` index.
- `customer_totals(customers, orders)` returns one row per customer with the columns `id`, `name`, `n_orders` (integer count of the customer's orders) and `total` (sum of their `amount`). A customer with no orders appears with `n_orders = 0` and `total = 0.0`. Sorted by `id`, fresh `0..n-1` index.
- `customers_without_orders(customers, orders)` returns the rows of `customers` (all of their columns, in their original order) whose `id` appears in no order, with a fresh `0..n-1` index.
- `safe_merge(left, right, key)` returns the **left** join of `left` with `right` on the column `key`, keeping `left`'s row order, with a fresh index. If `right` has the same `key` value more than once it must raise `ValueError` instead of multiplying rows.

### Hints

<details>
<summary>Hint 1</summary>

`merge(..., left_on=..., right_on=...)` joins on columns with different names. `how` chooses inner, left, right or outer.

</details>

<details>
<summary>Hint 2</summary>

Aggregate the orders per customer first, then left-join the totals onto the customers and fill the gaps for the customers with no orders.

</details>

<details>
<summary>Hint 3</summary>

`merge` has an `indicator` argument that records which side each row came from, and a `validate` argument that checks the relationship (such as `"m:1"`, many left rows to one right row).

</details>
