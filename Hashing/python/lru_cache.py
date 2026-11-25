"""
LRU cache (LeetCode 146 style) built from a hash map + doubly linked list,
mirroring the C implementation (sentinel start/end nodes, most recent at front).

    get(key): O(1)
    put(key, value): O(1)
"""


class Node:
    __slots__ = ("key", "value", "next", "prev")

    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.table = {}  # key -> Node

        # sentinels
        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start

    # ---------- doubly linked list ----------

    def _insert_front(self, key, value):
        p = self.start.next
        q = Node(key, value)
        q.next = p
        q.prev = self.start
        self.start.next = q
        p.prev = q
        return q

    @staticmethod
    def _delete_node(p):
        p.prev.next = p.next
        p.next.prev = p.prev

    # ---------- LRU API ----------

    def get(self, key):
        node = self.table.get(key)
        if node is None:
            return -1

        # move accessed node to front (most recently used)
        self._delete_node(node)
        self.table[key] = self._insert_front(key, node.value)
        return node.value

    def put(self, key, value):
        node = self.table.get(key)
        if node is not None:
            # key exists: update and move to front
            self._delete_node(node)
        elif len(self.table) >= self.cap:
            # remove least recently used (end.prev)
            lru = self.end.prev
            del self.table[lru.key]
            self._delete_node(lru)

        self.table[key] = self._insert_front(key, value)


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # returns 1

    cache.put(3, 3)      # evicts key 2
    print(cache.get(2))  # returns -1

    cache.put(4, 4)      # evicts key 1
    print(cache.get(1))  # returns -1
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4
