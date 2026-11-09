# MAX and MIN

Intermediate | db

The catalogue page shows, for every product category, the price range of its items.

Write a query returning each `category` of `products` with its highest price as `max_price` and its lowest price as `min_price`.

### Constraints

- Columns, in order: `category`, `max_price`, `min_price`
- One row per category

### Hints

<details>
<summary>Hint 1</summary>

`MAX` and `MIN` are aggregates, so they need `GROUP BY category`.

</details>

<details>
<summary>Hint 2</summary>

Both can appear in the same `SELECT`.

</details>
