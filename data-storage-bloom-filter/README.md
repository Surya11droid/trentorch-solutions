# Bloom Filters

Advanced | data-structures | probabilistic

### The problem, from first principles

A web crawler wants to know whether it has already visited a billion URLs. A database wants to know whether a key could be in a file before it pays for a disk read. Storing every item exactly is too much memory, and an exact set is not needed when a small, controlled mistake is acceptable in one direction only. A **Bloom filter** answers "definitely not present" or "possibly present" using a handful of bits per item. It never forgets an item that was added, so it never misses, but it sometimes claims an item is present when it was never added. Those false alarms are cheap to handle, and their rate can be computed and tuned in advance. This question builds the filter and the formulas that size it.

### From theory to code

Implement the class `BloomFilter(num_bits, num_hashes)` with `add(item)` and `might_contain(item)`, then `false_positive_rate(num_items, num_bits, num_hashes)`, the expected error rate, then `optimal_num_hashes(num_bits, num_items)`, the best number of hash functions for a given size. The skeleton and docstrings are already in the editor.

### Constraints

- Items are non-negative integers, so results are the same on every run. The two base hashes are `h1 = (item * 2654435761) % 2**32` and `h2 = ((item * 40503) % 2**32) | 1`. The `i`-th bit position of an item, for `i = 0 .. num_hashes - 1`, is `(h1 + i * h2) % num_bits`.
- `BloomFilter` stores `num_bits` bits in a plain list of 0 and 1. `add(item)` sets the item's `num_hashes` bit positions to 1. `might_contain(item)` returns `True` only if every one of those positions is 1.
- An item that was added must always be reported as possibly present (**no false negatives**). `might_contain` must never modify the filter.
- `false_positive_rate(num_items, num_bits, num_hashes)` returns `(1 - exp(-num_hashes * num_items / num_bits)) ** num_hashes` as a float.
- `optimal_num_hashes(num_bits, num_items)` returns `max(1, round((num_bits / num_items) * ln 2))` as an int.

### Hints

<details>
<summary>Hint 1</summary>

Each added item switches on a few bits. Looking an item up checks whether all of its bits are on. An item never added can still find all its bits on by accident, switched on by other items, and that accident is the false positive.

</details>

<details>
<summary>Hint 2</summary>

More bits per item makes accidents rarer. More hash functions help up to a point, then they just switch on too many bits and the filter fills up.

</details>

<details>
<summary>Hint 3</summary>

`1 - exp(-k * n / m)` is the chance that a given bit is on after `n` items with `k` hashes into `m` bits. A false positive needs all `k` of an item's bits on.

</details>
