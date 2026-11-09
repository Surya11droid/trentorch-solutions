# NTH Highest Value

Intermediate | db

Analytics needs the **second-highest age** among users. Two users are tied for the highest age (40), and the tie must count as one level: the answer is the next _different_ age. One user has no age recorded.

Write a query that returns a single value: the second-highest distinct `age`.

### Constraints

- Return a single row with a single column
- Ties count once (use distinct ages)
- Ignore users whose age is NULL

### Hints

<details>
<summary>Hint 1</summary>

Sort distinct ages descending and skip the first one.

</details>

<details>
<summary>Hint 2</summary>

`LIMIT 1 OFFSET 1` returns the second row.

</details>
