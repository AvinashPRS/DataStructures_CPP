"""
Implement queue using stack.
Input:
Output: queue class

Solution:
    The idea is to use two stacks s1 and s2. For pushing the elements, we insert it in s1. For removing elements, we need to
    remove the first entered element, which we can get by popping the stack elements from s1 to s2. The top element
    is the first element, which we then remove. Again for enqueue we use s1 and for dequeue if s2 is not empty
    then it can be done in O(1). For dequeue we are moving 'n' elements at a time and after that for removing the
    'n' elements it will take one pop from stack only which is O(1).

    TC: enqueue: O(1)
        dequeue: O(n), for n dequeue operations
"""


class Queue:
    def __init__(self):
        self._enqueue = []
        self._dequeue = []

    def enqueue(self, data):
        """For pushing element."""
        self._enqueue.append(data)

    def dequeue(self):
        """For popping element."""
        # first check if dequeue stack is empty or not
        if not self._dequeue:
            # fill it with enqueue stack elements
            while self._enqueue:
                self._dequeue.append(self._enqueue.pop())

        if not self._dequeue:
            raise IndexError("Queue is empty")

        return self._dequeue.pop()

    def empty(self):
        """Checks if queue is empty or not."""
        return not self._enqueue and not self._dequeue


if __name__ == "__main__":
    queue = Queue()

    for i in range(6):
        queue.enqueue(i)

    while not queue.empty():
        print(queue.dequeue(), end=" ")
    print()

    # dequeue on an empty queue raises an error
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error: {e}")
