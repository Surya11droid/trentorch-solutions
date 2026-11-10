import heapq

def solve():
    nums = []
    small = []
    large = []
    result = []

    for num in nums:
        heapq.heappush(small, -num)

        if large and -small[0] > large[0]:
            heapq.heappush(large, -heapq.heappop(small))

        if len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        elif len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))

        if len(small) > len(large):
            result.append(-small[0])
        else:
            result.append((-small[0] + large[0]) / 2)

    return result
