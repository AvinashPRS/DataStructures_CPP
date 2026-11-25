"""
Implement a FIFO Queue using a Min-Heap.

Each element gets an increasing sequence number when enqueued; the min-heap
keeps the smallest (oldest) sequence number at the root, giving FIFO order.

TC: O(logn) for enqueue and dequeue
SC: O(n)
"""
from dataclasses import dataclass, field
from typing import Any


class MinHeap:
    """Generic min-heap; elements must support < and >."""

    def __init__(self):
        self.heap = []

    @staticmethod
    def _parent(i): return (i - 1) // 2
    @staticmethod
    def _left(i): return 2 * i + 1
    @staticmethod
    def _right(i): return 2 * i + 2

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

    def push(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.empty():
            raise IndexError("Heap underflow")
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if not self.empty():
            self._heapify_down(0)
        return min_val

    def peek(self):
        if self.empty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    def empty(self):
        return not self.heap

    def size(self):
        return len(self.heap)


@dataclass(order=True)
class QueueElement:
    priority_val: int                       # sequential ID to preserve order
    data: Any = field(compare=False)


class Queue:
    def __init__(self):
        self._sequence_counter = 0
        self._min_heap = MinHeap()

    def enqueue(self, data):
        self._min_heap.push(QueueElement(self._sequence_counter, data))
        self._sequence_counter += 1         # next item gets a larger ID

    def dequeue(self):
        if self._min_heap.empty():
            raise IndexError("Queue underflow: Cannot dequeue from an empty queue")
        return self._min_heap.pop().data

    def front(self):
        if self._min_heap.empty():
            raise IndexError("Queue is empty")
        return self._min_heap.peek().data

    def empty(self):
        return self._min_heap.empty()

    def size(self):
        return self._min_heap.size()


if __name__ == "__main__":
    print_queue = Queue()

    print("--- Enqueuing Print Jobs ---")
    print_queue.enqueue("Document_A.pdf")
    print_queue.enqueue("Photo_B.png")
    print_queue.enqueue("Report_C.docx")

    print(f"Front of the queue: {print_queue.front()}\n")

    print("--- Processing Queue (FIFO Order) ---")
    while not print_queue.empty():
        print(f"Processing: {print_queue.dequeue()}")
    print()
