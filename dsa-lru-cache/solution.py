
def solve():

    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    class LRUCache:

        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = {}

            self.head = Node()
            self.tail = Node()

            self.head.next = self.tail
            self.tail.prev = self.head

        def remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev

        def add(self, node):
            node.next = self.head.next
            node.prev = self.head

            self.head.next.prev = node
            self.head.next = node

        def move_to_front(self, node):
            self.remove(node)
            self.add(node)

        def pop_tail(self):
            node = self.tail.prev
            self.remove(node)
            return node

        def get(self, key):
            if key not in self.cache:
                return -1

            node = self.cache[key]

            self.move_to_front(node)

            return node.value

        def put(self, key, value):

            if key in self.cache:
                node = self.cache[key]
                node.value = value
                self.move_to_front(node)
                return

            node = Node(key, value)

            self.cache[key] = node
            self.add(node)

            if len(self.cache) > self.capacity:
                lru = self.pop_tail()
                del self.cache[lru.key]

    return True


if __name__ == "__main__":
    solve()
