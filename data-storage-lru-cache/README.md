# LRU Cache

Intermediate | data-structures | caching

### The problem, from first principles

Memory is fast and small, disks and networks are slow and large, so systems keep recently used results close by. A cache has to decide what to throw away when it fills up, and the most common bet is that whatever was used longest ago is least likely to be needed next. That policy is **least recently used**, and the version that matters in practice does both `get` and `put` in constant time. A dictionary alone gives constant-time lookup but no sense of recency. A linked list alone gives recency but slow lookup. Combining them gives both. This question builds that combination, with the list written by hand.

### From theory to code

Implement the class `LRUCache(capacity)` with `get(key)`, `put(key, value)`, `__len__()` and `keys_by_recency()`. The skeleton and docstrings are already in the editor.

### Constraints

- `LRUCache(capacity)` holds at most `capacity` entries, with `capacity >= 1`.
- `get(key)` returns the value and marks the key as the **most recently used**. If the key is absent it returns `None` and changes nothing.
- `put(key, value)` stores the pair and marks the key as most recently used. If the key already exists its value is replaced. If adding a **new** key would exceed the capacity, the **least recently used** entry is evicted first.
- `keys_by_recency()` returns a list of all keys from most recently used to least recently used.
- Both `get` and `put` must take constant time: use a `dict` from key to node plus a **doubly linked list** of nodes that you write yourself. Do not use `collections.OrderedDict`, `functools.lru_cache`, or list operations that shift elements.

### Hints

<details>
<summary>Hint 1</summary>

Keep the list ordered by recency, with the most recent at the head. The dict gives the node for a key in constant time, and unlinking a node from a doubly linked list is constant time because it knows both neighbours.

</details>

<details>
<summary>Hint 2</summary>

Two sentinel nodes, a dummy head and a dummy tail that hold no data, remove every special case for an empty list or for the first and last node.

</details>

<details>
<summary>Hint 3</summary>

Reading a key is a use. Moving a node to the front is the same operation for `get` and for `put` on an existing key, so write it once.

</details>
