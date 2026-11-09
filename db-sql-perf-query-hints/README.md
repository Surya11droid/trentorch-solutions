# Query Hints: INDEXED BY

Advanced | db

`orders` has two indexes, `idx_orders_status` and `idx_orders_created`. For this query either could be used, and the planner picks one on its own:

```sql
SELECT COUNT(*) FROM orders WHERE status = 'paid' AND created_on >= '2024-06-01';
```

Sometimes you know better than the planner (or you want to be sure a particular plan is used). SQLite lets you _hint_ an index with `INDEXED BY`.

Write the count so that it must use `idx_orders_created`.

### Constraints

- Return a single count of paid orders with `created_on >= '2024-06-01'`
- Use `INDEXED BY idx_orders_created`
- The plan must use that index

### Hints

<details>
<summary>Hint 1</summary>

Syntax: `FROM orders INDEXED BY idx_orders_created`.

</details>

<details>
<summary>Hint 2</summary>

If the named index cannot be used for the query, SQLite raises an error instead of falling back.

</details>
