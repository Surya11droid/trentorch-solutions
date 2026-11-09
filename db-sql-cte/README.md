# Common Table Expressions (CTE): Named Queries

Advanced | db

The previous question solved "above their department's average" with a correlated subquery. A **common table expression** (CTE) makes the same logic easier to read by naming the intermediate step.

Write a query that first defines a CTE with each department's average salary, then returns `name`, `department` and `salary` of every employee earning more than the average of their department. The query must use a `WITH` clause.

### Constraints

- Columns, in order: `name`, `department`, `salary`
- Define the department averages in a `WITH` clause
- Join the CTE back to `employees`

### Hints

<details>
<summary>Hint 1</summary>

`WITH name AS (SELECT ...) SELECT ... FROM name` defines a temporary named result.

</details>

<details>
<summary>Hint 2</summary>

Join the CTE to `employees` on `department`, then filter with `WHERE`.

</details>
