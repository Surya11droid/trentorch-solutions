# Join Order Optimization

Advanced | db

`regions` has 5 rows and `customers` has 1,000 rows with an index `idx_customers_region` on `region_id`. To list the customers of the region named `'EU'`, the efficient plan is:

1. look at the (tiny) `regions` table and find `EU`,
2. use `idx_customers_region` to fetch only that region's customers.

SQLite normally finds this plan by itself, but in a `CROSS JOIN` it will **never** reorder the tables, so you can dictate the loop order yourself.

Write the query with `CROSS JOIN` so that `regions` is the outer loop and `customers` the inner, index-driven loop. Return only the customer `name`. Do not use table aliases (so the plan text stays readable).

### Constraints

- Return one column: the customer `name`
- Use `regions CROSS JOIN customers ON ...` (outer loop `regions`)
- Do not alias the tables
- `customers` must be searched through `idx_customers_region`

### Hints

<details>
<summary>Hint 1</summary>

In SQLite the left table of a `CROSS JOIN` is always the outer loop.

</details>

<details>
<summary>Hint 2</summary>

Put the matching condition in `ON customers.region_id = regions.id` and the filter in `WHERE regions.name = 'EU'`.

</details>
