"""
Create lookup, insert and delete methods for 10-digit ISBNs.
Use an LRU scheme for caching.

Solution:
    Keep an 'n' sized cache. The C++ version uses a list as the LRU queue and a hash table
    mapping ISBN -> (iterator into the list, price). In Python an OrderedDict gives both:
    move_to_end() is O(1) and popitem(last=False) removes the least recently used entry.
    Here the "front" of the queue (most recent) is the END of the OrderedDict.

    TC: lookup / insert / erase: O(1)
    SC: O(n), n: cache size
"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self._isbn_cache = OrderedDict()  # isbn -> price

    def _move_isbn_to_front(self, isbn):
        print("LRU Queue updated")
        self._isbn_cache.move_to_end(isbn)

    def insert_isbn(self, isbn, price):
        if isbn in self._isbn_cache:
            # already present: just refresh its position in the LRU queue
            self._move_isbn_to_front(isbn)
        else:
            # cache full: remove the least recently used isbn
            if len(self._isbn_cache) == self.capacity:
                self._isbn_cache.popitem(last=False)
                print("Old ISBN deleted")
            print("ISBN added to cache")
            self._isbn_cache[isbn] = price

    def erase_isbn(self, isbn):
        if isbn in self._isbn_cache:
            del self._isbn_cache[isbn]
            return True
        return False

    def lookup_isbn(self, isbn):
        """Returns (found, price)."""
        if isbn in self._isbn_cache:
            price = self._isbn_cache[isbn]
            self._move_isbn_to_front(isbn)
            return True, price
        return False, 0


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.insert_isbn(1111123123, 100)
    cache.insert_isbn(1111111111, 200)
    found, price = cache.lookup_isbn(1111111111)
    print(f"Lookup: {int(found)}")
    print(f"Price: {price}")
    print(f"Erased: {int(cache.erase_isbn(1111111111))}")
    cache.insert_isbn(1111111111, 200)
    cache.insert_isbn(1111111111, 200)
    cache.insert_isbn(1111111112, 200)
