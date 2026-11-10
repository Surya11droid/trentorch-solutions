import heapq

def solve():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
