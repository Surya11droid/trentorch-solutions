
def solve():

    class HashMap:

        def __init__(self, size=10):
            self.size = size
            self.table = [[] for _ in range(size)]

        def hash_function(self, key):
            return hash(key) % self.size

        def put(self, key, value):
            index = self.hash_function(key)
            bucket = self.table[index]

            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    return

            bucket.append((key, value))

        def get(self, key):
            index = self.hash_function(key)

            for k, v in self.table[index]:
                if k == key:
                    return v

            return None

        def remove(self, key):
            index = self.hash_function(key)
            bucket = self.table[index]

            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket.pop(i)
                    return

    # Test the implementation
    hm = HashMap()

    hm.put(101, "Rahul")
    hm.put(102, "Aman")

    assert hm.get(101) == "Rahul"

    hm.put(101, "Updated Rahul")
    assert hm.get(101) == "Updated Rahul"

    hm.remove(102)
    assert hm.get(102) is None

    return True
