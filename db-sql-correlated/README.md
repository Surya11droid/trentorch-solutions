# Correlated Subqueries: Row-by-Row

Advanced | db

HR wants to see who is paid above their own team's norm. Engineering earns more than Sales on average, so comparing everyone to one company-wide average would give the wrong answer.

Write a query returning `name`, `department` and `salary` of every employee whose salary is greater than the average salary **of their own department**. Use a correlated subquery.

### Constraints

- Columns, in order: `name`, `department`, `salary`
- Compare each employee with their _own_ department's average
- A department with a single employee has no one above its average

### Hints

<details>
<summary>Hint 1</summary>

The subquery can refer to a column of the outer row, e.g. `e.department`.

</details>

<details>
<summary>Hint 2</summary>

Give the outer table an alias so the inner query can reach it.

</details>
