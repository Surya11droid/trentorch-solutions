# Reading EXPLAIN QUERY PLAN

Advanced | db

Before you can speed up a query you have to know how SQLite will run it. `EXPLAIN QUERY PLAN` shows the strategy chosen by the planner without running the query.

The `orders` table (5,000 rows) has no index on `total`. Prefix this query with `EXPLAIN QUERY PLAN` and run it:

```sql
SELECT * FROM orders WHERE total > 90;
```

The result should show a full table scan.

### Constraints

- Run `EXPLAIN QUERY PLAN` on exactly `SELECT * FROM orders WHERE total > 90`
- Do not create any index; the plan must show a `SCAN` of `orders`

### Hints

<details>
<summary>Hint 1</summary>

The statement is `EXPLAIN QUERY PLAN` followed by the query.

</details>

<details>
<summary>Hint 2</summary>

Read the `detail` column: `SCAN orders` means every row is read.

</details>
