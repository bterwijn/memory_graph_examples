class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}  # key -> its node in the recency list

        self.head = Node()  # Dummy: immediately after it is MRU
        self.tail = Node()  # Dummy: immediately before it is LRU
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        # Unlink a known node without searching the list.
        before, after = node.prev, node.next
        before.next = after
        after.prev = before

    def _add_front(self, node: Node) -> None:
        # Insert immediately after head: node becomes MRU.
        first = self.head.next
        node.prev, node.next = self.head, first
        self.head.next = node
        first.prev = node

    def _touch(self, node: Node) -> None:
        self._remove(node)
        self._add_front(node)

    def get(self, key: object) -> object|None:
        node = self.nodes.get(key)
        if node is None:
            return None

        self._touch(node)  # A successful read changes recency.
        return node.value

    def put(self, key: object, value: object) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._touch(node)
            return

        node = Node(key, value)
        self.nodes[key] = node
        self._add_front(node)

        if len(self.nodes) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.nodes[lru.key]
