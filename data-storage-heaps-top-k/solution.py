
class MinHeap:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, x):
        self.items.append(x)
        i = len(self.items) - 1

        # Move upward
        while i > 0:
            parent = (i - 1) // 2

            if self.items[i] >= self.items[parent]:
                break

            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent

    def peek(self):
        if not self.items:
            raise IndexError("Heap is empty")

        return self.items[0]

    def pop(self):
        if not self.items:
            raise IndexError("Heap is empty")

        smallest = self.items[0]
        last = self.items.pop()

        if self.items:
            self.items[0] = last
            i = 0
            n = len(self.items)

            # Move downward
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest_child = i

                if left < n and self.items[left] < self.items[smallest_child]:
                    smallest_child = left

                if right < n and self.items[right] < self.items[smallest_child]:
                    smallest_child = right

                if smallest_child == i:
                    break

                self.items[i], self.items[smallest_child] = (
                    self.items[smallest_child], self.items[i]
                )

                i = smallest_child

        return smallest


def heapify(values):
    heap = MinHeap()
    heap.items = list(values)

    # Start from the last parent
    n = len(heap.items)

    for i in range(n // 2 - 1, -1, -1):
        current = i

        while True:
            left = 2 * current + 1
            right = 2 * current + 2
            smallest = current

            if left < n and heap.items[left] < heap.items[smallest]:
                smallest = left

            if right < n and heap.items[right] < heap.items[smallest]:
                smallest = right

            if smallest == current:
                break

            heap.items[current], heap.items[smallest] = (
                heap.items[smallest], heap.items[current]
            )

            current = smallest

    return heap


def top_k(stream, k):
    if k <= 0:
        return []

    heap = MinHeap()

    for x in stream:
        if len(heap) < k:
            heap.push(x)

        elif x > heap.peek():
            heap.pop()
            heap.push(x)

    result = []

    while len(heap):
        result.append(heap.pop())

    return result[::-1]


def merge_sorted(lists):
    heap = MinHeap()

    # Store (value, list_index, element_index)
    for i, lst in enumerate(lists):
        if lst:
            heap.push((lst[0], i, 0))

    result = []

    while len(heap):
        value, list_index, element_index = heap.pop()
        result.append(value)

        next_index = element_index + 1
        lst = lists[list_index]

        if next_index < len(lst):
            heap.push((lst[next_index], list_index, next_index))

    return result
