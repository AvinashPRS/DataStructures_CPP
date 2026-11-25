"""
Generic Heap class Implementation.

    For heap of size 'n':
        TC: Push: O(logn)
            Pop: O(logn)
            Heapify: O(n)
            Max/Min: O(1)
        Explanation: http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf
        SC: O(n) for heap
"""
import operator
from enum import Enum


class HeapType(Enum):
    MIN_HEAP = 0
    MAX_HEAP = 1


class Heap:
    RESIZE_FACTOR = 2

    def __init__(self, arr_or_capacity, heap_type):
        """
        Heap(list, type): builds a heap from the list, capacity = 2 * len(list)
        Heap(int, type):  creates an empty heap with the given capacity
        """
        self.heap_type = heap_type
        # set the comparator acc. to heap type
        # max-heap: True if first is greater than second
        # min-heap: True if first is smaller than second
        self.comparator = operator.gt if heap_type == HeapType.MAX_HEAP else operator.lt

        if isinstance(arr_or_capacity, int):
            self.num_heap_elements = 0
            self.capacity = arr_or_capacity
            self.heap = [None] * self.capacity
        else:
            self.heap = list(arr_or_capacity)
            self.num_heap_elements = len(self.heap)
            self.capacity = 2 * self.num_heap_elements
            self.heap.extend([None] * (self.capacity - self.num_heap_elements))

            # now heapify the list, starting with the first non-leaf node
            # since leaf nodes always satisfy heap property, start percolating down
            for i in range((self.num_heap_elements - 1) // 2, -1, -1):
                self.heapify_down(i, self.comparator)

    def push(self, data):
        # when heap is full, resize
        if self.num_heap_elements == self.capacity:
            self.resize_heap()

        # add the element at last, then heapify from there all the way up
        self.num_heap_elements += 1
        self.heap[self.num_heap_elements - 1] = data

        # while the parent is not satisfying the heap property, swap
        # current element with parent
        i = self.num_heap_elements - 1
        while i > 0 and not self.comparator(self.heap[self.get_parent_index(i)], self.heap[i]):
            parent_idx = self.get_parent_index(i)
            self.heap[parent_idx], self.heap[i] = self.heap[i], self.heap[parent_idx]
            i = parent_idx

    def pop(self):
        """
        Heap deletion: only the root element is deleted.
        We swap the root element with last element, then reduce the
        heap size by 1. Then to fix the disruption caused by
        swapping we heapify from root.
        """
        if self.is_empty():
            raise IndexError("Heap is empty")

        last = self.num_heap_elements - 1
        self.heap[0], self.heap[last] = self.heap[last], self.heap[0]
        popped_data = self.heap[last]
        self.num_heap_elements -= 1

        self.heapify_down(0, self.comparator)
        return popped_data

    def top(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    def is_empty(self):
        return self.num_heap_elements == 0

    def get_parent_index(self, i):
        if self.is_empty() or i <= 0 or i >= self.num_heap_elements:
            return -1
        return (i - 1) // 2

    def get_left_child_index(self, i):
        if self.is_empty() or i < 0 or i >= self.num_heap_elements:
            return -1
        return 2 * i + 1 if (2 * i + 1) < self.num_heap_elements else -1

    def get_right_child_index(self, i):
        if self.is_empty() or i < 0 or i >= self.num_heap_elements:
            return -1
        return 2 * i + 2 if (2 * i + 2) < self.num_heap_elements else -1

    def heapify_down(self, idx, comp):
        """
        Check if the left or right child of current index is greater (max-heap)
        or smaller (min-heap). If so, swap that element with the current parent
        and heapify from that index.
        """
        heap_prop_idx = idx
        left = self.get_left_child_index(idx)
        right = self.get_right_child_index(idx)

        if left != -1 and comp(self.heap[left], self.heap[heap_prop_idx]):
            heap_prop_idx = left
        if right != -1 and comp(self.heap[right], self.heap[heap_prop_idx]):
            heap_prop_idx = right

        if heap_prop_idx != idx:
            self.heap[heap_prop_idx], self.heap[idx] = self.heap[idx], self.heap[heap_prop_idx]
            # fix the lower subtrees
            self.heapify_down(heap_prop_idx, comp)

    def resize_heap(self):
        self.capacity = max(1, self.capacity * self.RESIZE_FACTOR)
        self.heap.extend([None] * (self.capacity - len(self.heap)))

    def show_heap_array(self):
        print(" ".join(str(x) for x in self.heap[:self.num_heap_elements]))


def heap_sort(arr, heap_type):
    """
    In-place sort, writing from the back.
    Increasing order: max-heap; decreasing order: min-heap.
    """
    h = Heap(arr, heap_type)
    write_idx = len(arr) - 1
    while not h.is_empty():
        arr[write_idx] = h.pop()
        write_idx -= 1


# ===================== Simple MaxHeap / MinHeap (list based) =====================

class MaxHeap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def _parent(i): return (i - 1) // 2
    @staticmethod
    def _left(i): return 2 * i + 1
    @staticmethod
    def _right(i): return 2 * i + 2

    def _heapify_up(self, i):
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            p = self._parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def _heapify_down(self, i):
        max_index = i
        left, right = self._left(i), self._right(i)
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
        if i != max_index:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self._heapify_down(max_index)

    def push(self, value):
        self.heap.append(value)                 # insert at the end
        self._heapify_up(len(self.heap) - 1)    # bubble up

    def pop(self):
        if self.empty():
            raise IndexError("Heap underflow: Cannot pop from an empty heap")
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]            # move the last element to the root
        self.heap.pop()
        if not self.empty():
            self._heapify_down(0)
        return max_val

    def peek(self):
        if self.empty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    def empty(self):
        return not self.heap

    def size(self):
        return len(self.heap)

    def print_heap(self):
        print("Heap Array: [ " + "".join(f"{v} " for v in self.heap) + "]")


class MinHeap(MaxHeap):
    def _heapify_up(self, i):
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            p = self._parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def _heapify_down(self, i):
        min_index = i
        left, right = self._left(i), self._right(i)
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self._heapify_down(min_index)


if __name__ == "__main__":
    arr = [562, 300, 10, 200, 29, 360, 4, 400]
    heap = Heap(arr, HeapType.MAX_HEAP)
    print(heap.pop())
    heap.show_heap_array()

    print()
    print(heap.pop())
    heap.push(21323)
    heap.show_heap_array()

    heap_sort(arr, HeapType.MAX_HEAP)
    print(" ".join(str(a) for a in arr))

    print("\n=========== MAX HEAP ===========")
    max_heap = MaxHeap()
    print("--- Inserting Elements ---")
    for v in (10, 7, 6, 5, 4, 3):
        max_heap.push(v)
    max_heap.print_heap()
    print("\nInserting a large value (15) to trigger heapifyUp:")
    max_heap.push(15)
    max_heap.print_heap()
    print("\n--- Extracting Max Elements (Sorting behavior) ---")
    while not max_heap.empty():
        print(f"Popped Max: {max_heap.pop()} -> New ", end="")
        max_heap.print_heap()

    print("\n=========== MIN HEAP ===========")
    min_heap = MinHeap()
    print("--- Inserting Elements ---")
    for v in (10, 7, 15, 3, 5):
        min_heap.push(v)
    min_heap.print_heap()
    print("\nInserting a very small value (1) to trigger heapifyUp:")
    min_heap.push(1)
    min_heap.print_heap()
    print("\n--- Extracting Min Elements (Sorting behavior) ---")
    while not min_heap.empty():
        print(f"Popped Min: {min_heap.pop()} -> New ", end="")
        min_heap.print_heap()
