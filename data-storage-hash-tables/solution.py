
class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def put(self, key, value):
        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

        if self.load_factor() > 0.75:
            self.resize()

    def get(self, key, default=None):
        index = hash(key) % self.capacity

        for k, v in self.buckets[index]:
            if k == key:
                return v

        return default

    def delete(self, key):
        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True

        return False

    def __len__(self):
        return self.size

    def load_factor(self):
        return self.size / self.capacity

    def keys(self):
        return [k for bucket in self.buckets for k, v in bucket]

    def resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            for key, value in bucket:
                index = hash(key) % self.capacity
                self.buckets[index].append((key, value))
