# Heaps & Top-K

Intermediate | data-structures | heaps

### The problem, from first principles

`02-binary-search` keeps a whole array sorted so any range can be found fast. Often only the extreme is needed: the smallest pending task, the ten highest-scoring results out of ten million, the next event in a simulation. Sorting everything to read off the top wastes almost all of the work. A **heap** keeps just enough order to hand back the minimum instantly and to absorb new values cheaply. It is an ordinary array with a rule about parents and children, and it is behind priority queues, top-k selection and merging many sorted lists. This question builds the heap, and two classic uses of it.

### From theory to code

Implement the class `MinHeap` with `push(x)`, `pop()`, `peek()` and `__len__()`, then `heapify(values)`, which builds a heap from a list in linear time, then `top_k(stream, k)`, the `k` largest values of a stream using memory for only `k`, then `merge_sorted(lists)`, which merges several sorted lists into one. The skeleton and docstrings are already in the editor.

### Constraints

- `MinHeap` stores its items in a plain list `self.items` laid out as a **binary heap**: the children of index `i` are `2*i + 1` and `2*i + 2`, and every parent is `<=` both of its children. Do not use the `heapq` module.
- `push(x)` appends `x` and moves it up while it is smaller than its parent. `pop()` removes and returns the smallest item by moving the last item to the root and moving it down toward the smaller child. `peek()` returns the smallest without removing it. `pop` and `peek` on an empty heap raise `IndexError`.
- `heapify(values)` returns a new `MinHeap` containing all `values` built by sifting down from the last parent to the root, not by `n` separate pushes. `values` must not be modified.
- `top_k(stream, k)` consumes an iterable once and returns the `k` largest values as a list in **descending** order, keeping a `MinHeap` of at most `k` items. It returns fewer than `k` values if the stream is shorter, and `[]` for `k <= 0`.
- `merge_sorted(lists)` takes a list of sorted lists and returns one sorted list of all their values, using a heap that holds at most one entry per input list. Ties keep the order of the lists. It must not sort the combined list.

### Hints

<details>
<summary>Hint 1</summary>

A heap is not sorted. Only parents are no larger than their children, which is enough to find the minimum at the root and cheap enough to restore after a change, in at most the height of the tree, about `log2 n` swaps.

</details>

<details>
<summary>Hint 2</summary>

To keep the `k` largest, keep a min-heap of the best `k` seen so far. A new value only matters if it beats the smallest of those, and the smallest is exactly what the root gives you.

</details>

<details>
<summary>Hint 3</summary>

To merge, put the first value of every list into the heap, tagged with which list it came from. Pop the smallest, output it, and push the next value from the same list.

</details>
