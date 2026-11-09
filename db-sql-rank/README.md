# RANK: Window Function with Gaps

Advanced | db

Rank users by age **within their region**, oldest first (rank 1 is the oldest). When two users have the same age they share a rank, and the next rank is skipped (1, 2, 2, 4), as in sports standings.

Write a query returning `name`, `region`, `age` and the rank as `age_rank`, using the `RANK()` window function.

### Constraints

- Columns, in order: `name`, `region`, `age`, `age_rank`
- Ranks restart in every region
- Ties share a rank and leave a gap afterwards

### Hints

<details>
<summary>Hint 1</summary>

`RANK() OVER (PARTITION BY ... ORDER BY ...)`

</details>

<details>
<summary>Hint 2</summary>

`PARTITION BY region` restarts the ranking per region; `ORDER BY age DESC` puts the oldest first.

</details>
