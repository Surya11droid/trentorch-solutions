# Transactions

Advanced | databases | transactions

### The problem, from first principles

Moving 100 from one bank account to another is two writes: subtract here, add there. If the machine fails between them, 100 has vanished. A **transaction** groups writes so that they take effect together or not at all, and that all-or-nothing promise, the A in ACID, is what lets people trust a database. It also lets a program try something and undo it. The classic way to understand transactions is to build a small in-memory key-value store with `begin`, `commit` and `rollback`, where transactions can be nested and a rollback throws away only the innermost one. This question builds that store and uses it for a safe transfer.

### From theory to code

Implement the class `TransactionalStore` with `set`, `get`, `delete`, `begin`, `commit`, `rollback` and `__len__`, then `transfer(store, source, target, amount)`, which moves money atomically. The skeleton and docstrings are already in the editor.

### Constraints

- `set(key, value)` stores a value and `get(key)` returns it, or `None` if the key is absent or deleted. `delete(key)` removes a key (a missing key is not an error). `__len__` is the number of keys currently visible.
- `begin()` opens a new transaction level. Transactions can be **nested** to any depth. Writes made inside a transaction are visible to reads in that transaction and in transactions opened inside it (**read your own writes**), but they are not permanent.
- `commit()` makes the innermost transaction's writes part of its parent: the next level out, or the permanent store if it was the outermost. `rollback()` discards the innermost transaction's writes and leaves everything else as it was. Both raise `RuntimeError` if no transaction is open.
- A `delete` inside a transaction hides the key from reads in that transaction, and is itself undone by `rollback`.
- `transfer(store, source, target, amount)` moves `amount` from the integer balance at `source` to the one at `target` inside its own transaction. If `source` has less than `amount` (a missing balance counts as `0`), it rolls back and returns `False` without changing anything. Otherwise it commits and returns `True`.
- Use plain dicts. Do not copy the entire store when a transaction begins: keep only the changes made at each level.

### Hints

<details>
<summary>Hint 1</summary>

Keep a stack of change-sets, one per open transaction. A change-set maps a key to its new value, or to a marker meaning "deleted".

</details>

<details>
<summary>Hint 2</summary>

To read a key, look in the innermost change-set first, then the next one out and finally in the permanent data. The first place that mentions the key decides the answer.

</details>

<details>
<summary>Hint 3</summary>

Committing a level merges its change-set into the one below it (or into the permanent data), and rolling it back just drops it.

</details>
