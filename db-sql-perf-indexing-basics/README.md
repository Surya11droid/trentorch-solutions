# Indexes: Turning Scans into Searches

Advanced | db

The `orders` table holds 5,000 rows and customers constantly look up their own orders:

```sql
SELECT * FROM orders WHERE customer_id = 42;
```

With no index on `customer_id`, SQLite has to read **every** row to find the matching ones (a _table scan_). Add an index so it can jump straight to them (an _index search_).

Create an index named `idx_orders_customer` on `orders(customer_id)`, and then run the lookup for customer 42 so the result is returned.

### Constraints

- The index must be named `idx_orders_customer` and cover only `customer_id`
- End your script with the lookup `SELECT * FROM orders WHERE customer_id = 42;`
- The lookup must use the index (checked with `EXPLAIN QUERY PLAN`)

### Hints

<details>
<summary>Hint 1</summary>

`CREATE INDEX name ON table(column);`

</details>

<details>
<summary>Hint 2</summary>

Run `EXPLAIN QUERY PLAN SELECT ...` yourself: `SCAN orders` is slow, `SEARCH orders USING INDEX ...` is fast.

</details>
