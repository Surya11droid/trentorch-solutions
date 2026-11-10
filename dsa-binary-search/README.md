# Binary Search

Intermediate | dsa

### The problem

Given a list `arr` of integers sorted in ascending order and an integer `target`, return the index of `target` in `arr`, or `-1` if it is not there. Your solution must run in O(log n) time, so scanning the list one element at a time will not do.

Implement `solve(arr, target)`. The signature and docstring are already in the editor.

### Constraints

- `arr` is sorted ascending and has no duplicates; it may be empty.
- `target` may be smaller or larger than every element.

### Hints

<details>
<summary>Hint 1</summary>

Keep two indices, `lo` and `hi`, that bound the part of the list that could still hold `target`. Look at the middle element each round.

</details>

<details>
<summary>Hint 2</summary>

If the middle element is too small, `target` can only be to its right, so move `lo` past it. If it is too big, move `hi` before it. Stop when `lo > hi`.

</details>
