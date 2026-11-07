
import math

class BloomFilter:
    def __init__(self, num_bits, num_hashes):
        self.num_bits = num_bits
        self.num_hashes = num_hashes
        self.bits = [0] * num_bits

    def _positions(self, item):
        h1 = (item * 2654435761) % (2**32)
        h2 = ((item * 40503) % (2**32)) | 1

        return [
            (h1 + i * h2) % self.num_bits
            for i in range(self.num_hashes)
        ]

    def add(self, item):
        for pos in self._positions(item):
            self.bits[pos] = 1

    def might_contain(self, item):
        return all(
            self.bits[pos]
            for pos in self._positions(item)
        )


def false_positive_rate(num_items, num_bits, num_hashes):
    return (
        1 - math.exp(
            -num_hashes * num_items / num_bits
        )
    ) ** num_hashes


def optimal_num_hashes(num_bits, num_items):
    return max(
        1,
        round((num_bits / num_items) * math.log(2))
    )
