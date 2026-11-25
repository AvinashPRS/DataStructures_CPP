"""
Implement queue with Max API. The queue should be able to return max element currently.
Input:
Output: queue class with max method

Solution:
    We use a second queue which stores the max element currently. Things to note:
    1. Any element which has come before and is greatest will remain the greatest
       till it is popped.
    2. Any element which comes at a later stage and was not the greatest when it came
       might become the greatest, so we need to keep track of all the elements coming.
    3. If the current element is greater than all the previous elements, then no need of previous elements.
       So we remove the previous elements so that the greatest is always at the front and
       can be accessed in O(1).
    This is because of the fact that once we get a max element,
    any element not greater than or equal to after that is not going to be max.
    Since this is FIFO, so the max element should be at front.
    For enqueue:
        Pop elements from tracker queue till the last element is bigger/equal than this
    For dequeue:
        Check if the front of tracker queue is equal to popped element, pop if equal
    For max:
        return front of tracker queue

    TC: enqueue: O(n), for 'n' enqueue operations
        dequeue: O(1)
        max: O(1)
    SC: O(n), n: no. of elements, required for tracking max element
"""
from collections import deque


class Queue:
    def __init__(self):
        self._q = deque()
        self._max_tracker = deque()

    def enqueue(self, data):
        """For pushing element."""
        self._q.append(data)

        # track the max element: drop all smaller elements from the back
        while self._max_tracker and self._max_tracker[-1] < data:
            self._max_tracker.pop()
        self._max_tracker.append(data)

    def dequeue(self):
        """For popping element."""
        if not self._q:
            raise IndexError("Queue is empty")

        popped_data = self._q.popleft()

        # check if the current element is max also
        if self._max_tracker[0] == popped_data:
            self._max_tracker.popleft()

        return popped_data

    def empty(self):
        """Checks if queue is empty or not."""
        return not self._q

    def max(self):
        """Returns the max element."""
        if not self._max_tracker:
            raise IndexError("Queue is empty")
        return self._max_tracker[0]


if __name__ == "__main__":
    q = Queue()

    for i in range(6):
        q.enqueue(i)
        print(f"Max: {q.max()}", end=" ")
    print()
    while not q.empty():
        print(f"Max: {q.max()}", end=" ")
        print(q.dequeue(), end=" ")
    print()
