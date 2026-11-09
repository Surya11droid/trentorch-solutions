# Subqueries: Nested Queries

Advanced | db

You want to highlight users who are older than average. You cannot compare against `AVG(age)` directly in a `WHERE` clause, because the average has to be computed first.

Write a query returning `id`, `name` and `age` of every user whose age is strictly greater than the average age of all users. Use a subquery for the average.

### Constraints

- Columns, in order: `id`, `name`, `age`
- Strictly greater than the average (not equal)
- Compute the average inside the query; do not type it in

### Hints

<details>
<summary>Hint 1</summary>

A subquery is a `SELECT` in parentheses used as a value.

</details>

<details>
<summary>Hint 2</summary>

`WHERE age > (SELECT AVG(age) FROM users)`

</details>
