
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert node right after head
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    # Get a value
    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value

    # Insert or update a value
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]

    def __len__(self):
        return len(self.cache)

    def keys_by_recency(self):
        result = []
        current = self.head.next

        while current != self.tail:
            result.append(current.key)
            current = current.next

        return result
