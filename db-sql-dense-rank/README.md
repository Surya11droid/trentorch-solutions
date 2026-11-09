# DENSE_RANK: Window Function without Gaps

Advanced | db

A quiz leaderboard awards medal levels: highest score is level 1, and people with the same score share a level. Unlike sports standings there should be **no gaps**: after two people tie for level 2 the next score is level 3, not 4.

Write a query returning `name`, `score` and the level as `score_rank`, using `DENSE_RANK()`.

### Constraints

- Columns, in order: `name`, `score`, `score_rank`
- Highest score has `score_rank` 1
- Ties share a rank and the next rank follows immediately (1, 2, 2, 3)

### Hints

<details>
<summary>Hint 1</summary>

`DENSE_RANK() OVER (ORDER BY score DESC)`

</details>

<details>
<summary>Hint 2</summary>

`RANK()` would leave a gap after a tie; `DENSE_RANK()` does not.

</details>
