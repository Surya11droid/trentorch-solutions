def solve():
    intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

    intervals.sort(key=lambda x: x[0])

    merged = []

    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged
