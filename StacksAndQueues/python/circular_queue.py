"""
Implement a circular queue using an array.

Input:
Output: queue class

Solution:
    We use two index trackers front and back, initially both are 0. When we enqueue then we make rear = (rear+1) mod capacity.
    This way it always stays inside the array. For dequeue we make front = (front+1). We keep track whether the array has become full or not also.
    If it has become full, we first rotate the array such that front is positioned at index 0 and rear stays at the back of array, after
    that we resize by a constant factor. The vacant places get appended after rear tracker.

    TC: enqueue: O(n), for 'n' operations of enqueue and amortized is O(1)
        dequeue: O(1)
"""


class Queue:
    RESIZE_FACTOR = 2

    def __init__(self, n):
        self.q = [None] * n
        self.front = 0
        self.rear = 0
        self.num_elements = 0

    def enqueue(self, data):
        """For pushing element."""
        # if the array is full, rotate and then resize
        if self.num_elements == len(self.q):
            # first rotate the array, otherwise rear might overwrite data.
            # When full, rear == front, so front moves to index 0
            self.q = self.q[self.rear:] + self.q[: self.rear]
            self.front = 0
            # change rear index
            self.rear = len(self.q)
            # resize the array
            self.q.extend([None] * ((self.RESIZE_FACTOR - 1) * len(self.q)))

        self.q[self.rear] = data
        self.num_elements += 1
        # increment rear
        self.rear = (self.rear + 1) % len(self.q)

    def dequeue(self):
        """For popping element."""
        # check if the queue is empty or not
        if self.num_elements == 0:
            raise IndexError("Queue is empty")

        popped_el = self.q[self.front]
        self.front = (self.front + 1) % len(self.q)
        self.num_elements -= 1

        return popped_el

    def empty(self):
        """Checks if queue is empty or not."""
        return self.num_elements == 0


if __name__ == "__main__":
    queue = Queue(5)

    for i in range(6):
        queue.enqueue(i)

    while not queue.empty():
        print(queue.dequeue(), end=" ")
    print()
