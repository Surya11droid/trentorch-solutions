
def lower_bound(a, x):
    left, right = 0, len(a)

    while left < right:
        mid = (left + right) // 2

        if a[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(a, x):
    left, right = 0, len(a)

    while left < right:
        mid = (left + right) // 2

        if a[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left


def range_query(a, low, high):
    start = lower_bound(a, low)
    end = upper_bound(a, high)

    return a[start:end]


def insert_sorted(a, x):
    pos = upper_bound(a, x)

    return a[:pos] + [x] + a[pos:]

    # TODO: Find the position with a bound, then build the new list.
    pass
