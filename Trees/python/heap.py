"""
  Heap using an array
  Enables us to represent binary trees without pointers:
  - Left child sits at 2n
  - Right child sits at 2n + 1
  - Parent sits at floor(n/2)
  Index 0 holds a dud element so the root is at index 1.
"""


class Heap:
    """Min-heap."""

    def __init__(self):
        self.queue_ = [0]   # first item is a dud
        self.size_ = 0

    def is_empty(self):
        return self.size_ == 0

    def size(self):
        return self.size_

    def clear(self):
        self.queue_ = [0]
        self.size_ = 0

    def get_item(self, idx):
        return self.queue_[idx]

    def parent(self, idx):
        if self.size_ <= 1 or idx <= 1:  # empty, or root has no parent
            return -1
        return idx // 2

    def child(self, idx):
        if self.size_ <= 1 or 2 * idx > self.size_:  # no child
            return -1
        return 2 * idx

    def find(self, idx, val):
        """Index of val in the subtree rooted at idx, or -1."""
        if idx > self.size_:            # out of bounds
            return -1
        if val < self.queue_[idx]:      # val can't be below a bigger node
            return -1
        if self.queue_[idx] == val:
            return idx
        child_idx = self.child(idx)
        i = -1
        if child_idx != -1:
            i = max(self.find(child_idx, val), self.find(child_idx + 1, val))
        return i

    def _bubble_up(self, idx):
        """While the parent's value is greater, move the item up. O(log n)"""
        parent_idx = self.parent(idx)
        if parent_idx == -1:
            return
        q = self.queue_
        if q[parent_idx] > q[idx]:
            q[parent_idx], q[idx] = q[idx], q[parent_idx]
            self._bubble_up(parent_idx)

    def insert(self, val):
        self.queue_.append(val)
        self.size_ += 1
        self._bubble_up(self.size_)

    def _get_min_idx(self, a_idx, b_idx, c_idx):
        """Index of the min value among 3 indices (c_idx may not exist)."""
        q = self.queue_
        is_left_smaller = q[a_idx] < q[b_idx]
        if c_idx > self.size_:
            return a_idx if is_left_smaller else b_idx
        elif is_left_smaller:
            return a_idx if q[a_idx] < q[c_idx] else c_idx
        else:
            return b_idx if q[b_idx] < q[c_idx] else c_idx

    def _bubble_down(self, idx):
        """While a child is smaller, move the item down. O(log n)"""
        child_idx = self.child(idx)
        if child_idx == -1:
            return
        min_idx = self._get_min_idx(idx, child_idx, child_idx + 1)
        if min_idx != idx:
            q = self.queue_
            q[min_idx], q[idx] = q[idx], q[min_idx]
            self._bubble_down(min_idx)

    def remove(self, val):
        """O(2 * log n)"""
        idx = self.find(1, val)
        if idx == -1:
            return
        # replace with the last item
        self.queue_[idx] = self.queue_[self.size_]
        self.size_ -= 1
        del self.queue_[self.size_ + 1:]
        if idx <= self.size_:
            self._bubble_down(idx)
            self._bubble_up(idx)

    def extract_min(self):
        """Removes and returns the min value."""
        if self.is_empty():
            raise IndexError("Empty Heap!")
        mn = self.queue_[1]
        self.remove(mn)
        return mn

    def heap_sort(self):
        """O(n log n)"""
        sorted_items = []
        while not self.is_empty():
            sorted_items.append(self.extract_min())
        return sorted_items

    def make_heap(self, array, n=None):
        """Create the heap from an unsorted array/list."""
        if n is None:
            n = len(array)
        self.size_ = n
        self.queue_.extend(array[:n])
        for i in range(n, 0, -1):
            self._bubble_down(i)

    def __str__(self):
        return " ".join(map(str, self.queue_[1:]))

    to_string = __str__


def main():
    h = Heap()
    array = [3, 70, 4, 80, 90, 5, 6, 82, 84, 91, 92, 7, 8]
    h.make_heap(array, 13)
    print(h.to_string())
    h.remove(80)
    print(h.to_string())


if __name__ == "__main__":
    main()
