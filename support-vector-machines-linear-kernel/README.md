# Linear kernel

Beginner | classic-ml

### The problem, from first principles

`Hinge loss` and `Linear SVM via gradient descent on hinge loss` both use a straight line (a hyperplane) to separate two classes. Real data often is not separable that way. A kernel is a function that measures similarity between two points, and kernel methods replace every dot product in the algorithm with that similarity. The simplest kernel is the plain dot product itself, which is the linear kernel: it gives the same answer as the linear SVM, but it is written in a form every other kernel can slot into.

Given a matrix of points `X` with shape `(n, d)` and a matrix `Y` with shape `(m, d)`, build the `(n, m)` matrix of pairwise dot products.

### Constraints

- Return a NumPy array of shape `(n, m)` where entry `[i, j]` equals `X[i] @ Y[j]`.
- Do not modify `X` or `Y`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

One matrix product is enough. Think about which operand needs its rows and columns swapped.

</details>

<details>
<summary>Hint 2</summary>

`X @ Y.T` has shape `(n, d) @ (d, m)`, which gives `(n, m)`.

</details>
