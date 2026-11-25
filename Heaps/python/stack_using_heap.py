"""
Implement Stack using Heap

Solution:
    The key property of a stack is LIFO, so we need the most recent element at the
    root of the heap. Associate each element with an increasing counter; the most
    recent has the largest count and with a max-heap it is always on top.
    (Python's heapq is a min-heap, so we push the negated counter.)

    Similarly, with a min-heap we can implement a queue.

    TC: O(logn) for push and pop
    SC: O(n) for heap
"""
import heapq


class Stack:
    def __init__(self):
        self._priority = 0
        self._max_heap = []     # entries: (-priority, data)

    def push(self, data):
        heapq.heappush(self._max_heap, (-self._priority, data))
        self._priority += 1     # increment priority for next element

    def pop(self):
        if not self._max_heap:
            raise IndexError("Stack is empty")
        return heapq.heappop(self._max_heap)[1]

    def empty(self):
        return not self._max_heap

    def top(self):
        if not self._max_heap:
            raise IndexError("Stack is empty")
        return self._max_heap[0][1]


if __name__ == "__main__":
    s = Stack()
    for i in range(8):
        s.push(i)
    print(s.pop())
    print(s.top())
    print(int(s.empty()))

    while not s.empty():
        print(s.pop(), end=" ")
    print()
    # s.pop()  # pop when stack is empty, raises IndexError
