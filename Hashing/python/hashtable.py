"""
Generic separate-chaining hash table, a Python port of
https://github.com/goldsborough/hashtable (C).

The C version stores raw bytes (key_size / value_size + memcpy/memcmp). In Python
we store any hashable key and any value directly, so those sizes are not needed.
Behavior kept from the original:
  - minimum capacity of 8 buckets, nodes pushed to the front of their chain
  - grow (x2 of size) when size reaches capacity
  - shrink when size drops to capacity / 4
  - djb2 hash by default (applied to the key's bytes/str), can be swapped
"""
import copy

HT_MINIMUM_CAPACITY = 8
HT_LOAD_FACTOR = 5
HT_MINIMUM_THRESHOLD = HT_MINIMUM_CAPACITY * HT_LOAD_FACTOR

HT_GROWTH_FACTOR = 2
HT_SHRINK_THRESHOLD = 1 / 4

HT_ERROR = -1
HT_SUCCESS = 0

HT_UPDATED = 1
HT_INSERTED = 0

HT_NOT_FOUND = 0
HT_FOUND = 1


class HTNode:
    __slots__ = ("next", "key", "value")

    def __init__(self, key, value, next_node=None):
        self.next = next_node
        self.key = key
        self.value = value


def _ht_default_hash(key):
    """djb2 string hashing algorithm (hash * 33 ^ byte)."""
    data = key if isinstance(key, (bytes, bytearray)) else repr(key).encode()
    h = 5381
    for byte in data:
        h = (((h << 5) + h) ^ byte) & 0xFFFFFFFFFFFFFFFF
    return h


def _ht_default_compare(first_key, second_key):
    return first_key == second_key


class HashTable:
    def __init__(self, capacity=HT_MINIMUM_CAPACITY):
        if capacity < HT_MINIMUM_CAPACITY:
            capacity = HT_MINIMUM_CAPACITY
        self.hash = _ht_default_hash
        self.compare = _ht_default_compare
        self.size = 0
        self._allocate(capacity)

    # ---------------- interface ----------------

    def copy(self):
        return copy.deepcopy(self)

    def swap(self, other):
        self.__dict__, other.__dict__ = other.__dict__, self.__dict__

    def insert(self, key, value):
        if key is None:
            return HT_ERROR

        if self._should_grow():
            self._adjust_capacity()

        index = self._hash(key)
        node = self.nodes[index]
        while node:
            if self.compare(key, node.key):
                node.value = value
                return HT_UPDATED
            node = node.next

        self.nodes[index] = HTNode(key, value, self.nodes[index])
        self.size += 1
        return HT_INSERTED

    def contains(self, key):
        return HT_FOUND if self._find_node(key) is not None else HT_NOT_FOUND

    def lookup(self, key):
        node = self._find_node(key)
        return node.value if node is not None else None

    def erase(self, key):
        if key is None:
            return HT_ERROR

        index = self._hash(key)
        previous, node = None, self.nodes[index]
        while node:
            if self.compare(key, node.key):
                if previous:
                    previous.next = node.next
                else:
                    self.nodes[index] = node.next
                self.size -= 1

                if self._should_shrink():
                    self._adjust_capacity()
                return HT_SUCCESS
            previous, node = node, node.next
        return HT_NOT_FOUND

    def clear(self):
        self._allocate(HT_MINIMUM_CAPACITY)
        self.size = 0
        return HT_SUCCESS

    def is_empty(self):
        return self.size == 0

    def reserve(self, minimum_capacity):
        """`minimum_capacity` is in elements, not in bucket indices."""
        if minimum_capacity > self.threshold:
            return self._resize(minimum_capacity // HT_LOAD_FACTOR)
        return HT_SUCCESS

    def __len__(self):
        return self.size

    # ---------------- private ----------------

    def _find_node(self, key):
        if key is None:
            return None
        node = self.nodes[self._hash(key)]
        while node:
            if self.compare(key, node.key):
                return node
            node = node.next
        return None

    def _hash(self, key):
        return self.hash(key) % self.capacity

    def _should_grow(self):
        return self.size == self.capacity

    def _should_shrink(self):
        return self.size == int(self.capacity * HT_SHRINK_THRESHOLD)

    def _adjust_capacity(self):
        return self._resize(self.size * HT_GROWTH_FACTOR)

    def _allocate(self, capacity):
        self.nodes = [None] * capacity
        self.capacity = capacity
        self.threshold = capacity * HT_LOAD_FACTOR
        return HT_SUCCESS

    def _resize(self, new_capacity):
        if new_capacity < HT_MINIMUM_CAPACITY:
            if self.capacity > HT_MINIMUM_CAPACITY:
                new_capacity = HT_MINIMUM_CAPACITY
            else:
                return HT_SUCCESS  # no-op

        old, old_capacity = self.nodes, self.capacity
        self._allocate(new_capacity)
        self._rehash(old, old_capacity)
        return HT_SUCCESS

    def _rehash(self, old, old_capacity):
        for chain in range(old_capacity):
            node = old[chain]
            while node:
                nxt = node.next
                new_index = self._hash(node.key)
                node.next = self.nodes[new_index]
                self.nodes[new_index] = node
                node = nxt


if __name__ == "__main__":
    # choose an initial capacity of 10
    table = HashTable(10)
    table.reserve(100)

    x = 6
    y = 9.0
    table.insert(x, y)

    if table.contains(x):
        y = table.lookup(x)
        print(f"{x}'s value is: {y:f}")

    table.erase(x)
    table.clear()
