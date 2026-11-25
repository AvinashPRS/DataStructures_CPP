"""LRU cache using a doubly linked list + hash table, with a randomised test."""
import random
import sys

MAX_NUM_ITERATIONS = 50


def handle_error():
    print("Error occured")
    sys.exit(1)


class Node:
    def __init__(self, key, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size  # maximum number of nodes the cache can hold
        self.count = 0            # current number of nodes
        self.head = None          # head of the doubly linked list (most recent)
        self.tail = None          # tail (least recent)
        self.ht = {}              # key -> node

    def add(self, new_item):
        if self.count == self.max_size:
            # Cache is full: remove the last node from the list
            temp = self.tail
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
            self.count -= 1
            del self.ht[temp.key]

        # Add the new node to the front of the list
        new_item.prev = None
        new_item.next = self.head
        if self.head:
            self.head.prev = new_item
        self.head = new_item
        if not self.tail:
            self.tail = new_item
        self.count += 1
        self.ht[new_item.key] = new_item
        return 0

    def get(self, key):
        cur_node = self.ht.get(key)
        if cur_node is None:
            return None
        if self.head is cur_node:
            return cur_node
        # Detach the node and move it to the front; update tail if needed
        if self.tail is cur_node:
            self.tail = cur_node.prev
        cur_node.prev.next = cur_node.next
        if cur_node.next:
            cur_node.next.prev = cur_node.prev
        cur_node.prev = None
        cur_node.next = self.head
        self.head.prev = cur_node
        self.head = cur_node
        return cur_node


def lru_verify(cache):
    """Check the invariants of the linked list."""
    if cache.count == 0:
        if cache.head is not None or cache.tail is not None:
            handle_error()
        return
    if cache.head.prev is not None or cache.tail.next is not None:
        handle_error()
    if cache.count == 1:
        if cache.head is not cache.tail:
            handle_error()
        return

    count, cur = 0, cache.head
    while cur is not None:
        count += 1
        cur = cur.next
    if count != cache.count:
        handle_error()

    count, cur = 0, cache.tail
    while cur is not None:
        count += 1
        cur = cur.prev
    if count != cache.count:
        handle_error()


def test_01(max_size):
    cache = LRUCache(max_size)
    key = 0
    for _ in range(MAX_NUM_ITERATIONS):
        if random.randrange(2) == 0:
            # add operation
            cache.add(Node(key))
            key += 1
        else:
            # get operation
            search_key = random.randrange(key + 1)
            cur_node = cache.get(search_key)
            if cur_node:
                # just accessed, so it must be at the head
                if cache.head is not cur_node:
                    handle_error()
            else:
                # not found: verify the key really isn't in the cache
                cur = cache.head
                while cur is not None:
                    if cur.key == search_key:
                        handle_error()
                    cur = cur.next
        lru_verify(cache)


def main():
    # Test for different max sizes of LRU cache
    for max_size in range(1, 21):
        test_01(max_size)
    print("Test passed ")


if __name__ == "__main__":
    main()
