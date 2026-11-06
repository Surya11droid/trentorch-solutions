# Binary Search & Sorted Indexes

Beginner | data-structures | searching

### The problem, from first principles

`01-hash-tables` finds one exact key fast. It cannot answer "every price between 10 and 20" or "the first order after noon", because hashing scatters neighbours. For range questions the data is kept **sorted**, and a sorted array can be searched by halving: look at the middle, discard the half that cannot contain the answer, repeat. Finding a position among a million sorted values takes about twenty comparisons. A sorted list of keys with positions attached is the simplest database index, and the two boundary searches built here, lower bound and upper bound, are what every range query reduces to.

### From theory to code

Implement `lower_bound(a, x)`, the first position where `x` could be inserted without breaking the order, then `upper_bound(a, x)`, the position just after the last equal value, then `range_query(a, low, high)`, every value between two limits, then `insert_sorted(a, x)`, which keeps a list sorted as new values arrive. The signatures and docstrings are already in the editor.

### Constraints

- `a` is a list of numbers sorted in non-decreasing order. Duplicates are allowed. Do not use the `bisect` module or `list.index`, and do not sort or scan the whole list for a search.
- `lower_bound(a, x)` returns the smallest index `i` such that every value before `i` is `< x`. It equals `len(a)` when all values are smaller than `x`.
- `upper_bound(a, x)` returns the smallest index `i` such that every value before `i` is `<= x`. It equals `len(a)` when all values are `<= x`.
- `range_query(a, low, high)` returns the list of values `v` with `low <= v <= high`, in order, using the two bounds above and one slice.
- `insert_sorted(a, x)` returns a **new** list with `x` inserted so the result is sorted. If equal values exist, `x` goes after them. `a` must not be modified.
- Each search must take `O(log n)` comparisons. Tests count the comparisons.

### Hints

<details>
<summary>Hint 1</summary>

Keep two indices, `low` and `high`, around the answer and look at the middle one. If it is too small the answer is to its right, otherwise it is at the middle or to its left.

</details>

<details>
<summary>Hint 2</summary>

Lower bound and upper bound differ only in whether the middle value counts as "too small" when it equals `x`. Write one and change a single comparison for the other.

</details>

<details>
<summary>Hint 3</summary>

A range of values `[low, high]` starts at `lower_bound(low)` and ends just before `upper_bound(high)`.

</details>
