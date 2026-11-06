# Hash Tables

Intermediate | data-structures | hashing

### The problem, from first principles

A Python `dict` answers "what is the value for this key?" in roughly constant time, however many entries it holds, and that speed is behind counting words, caching results, joining tables and deduplicating rows. The trick is that it does not search. It turns the key into a number, uses the number as a position in an array and looks there. Two different keys can land on the same position, and how a table handles that collision, and how it grows when it gets crowded, decides whether the constant-time promise holds. This question builds a hash table with chaining from an empty array of buckets.

### From theory to code

Implement the class `HashTable` with `put(key, value)`, `get(key, default)`, `delete(key)`, `__len__()`, `load_factor()` and `keys()`, including automatic growth when the table becomes too full. The skeleton and docstrings are already in the editor.

### Constraints

- The constructor `HashTable(capacity=8)` creates `capacity` empty buckets, and `capacity` stays readable as an attribute. Each bucket is a list of `(key, value)` pairs (**separate chaining**).
- A key goes in bucket `hash(key) % capacity`. Tests use integer keys, whose hash is the integer itself, so bucket positions are predictable.
- `put` replaces the value if the key is already present, otherwise appends a pair to the bucket and increases the size. After inserting, if `load_factor() > 0.75` the table doubles its capacity and **rehashes** every pair into the new buckets.
- `get(key, default=None)` returns the stored value or `default` when the key is absent. `delete(key)` removes the key and returns `True`, or returns `False` if it was absent. `__len__` is the number of stored keys.
- `load_factor()` returns `len(self) / capacity` as a float. `keys()` returns a list of all keys in any order.
- Do not use a `dict` or `set` to store the data. Plain lists are the only containers allowed for the buckets.

### Hints

<details>
<summary>Hint 1</summary>

A bucket is just a list. Searching it is a short linear scan, which stays short as long as the table keeps the average bucket length low.

</details>

<details>
<summary>Hint 2</summary>

When capacity doubles, a key's bucket changes because `hash(key) % capacity` now uses a different modulus. Rebuild the table from scratch by re-inserting every pair.

</details>

<details>
<summary>Hint 3</summary>

Growing happens after an insertion pushes the load factor over the limit, so check it at the end of `put`, and only when a new key was added.

</details>
