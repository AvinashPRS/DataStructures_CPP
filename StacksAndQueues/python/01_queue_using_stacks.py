"""
Implement a queue using two stacks.

Solution:
    Elements are always pushed onto s1. When an element is to be removed (or peeked)
    and s2 is empty, all elements of s1 are moved to s2, which reverses their order so
    that the oldest element is on top of s2.
    TC: add: O(1), remove/front: amortized O(1)
"""
import sys

MAX_NUM_QUEUE_ELEMS = 10


class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def _fill_s2_if_empty(self):
        """Shift elements from s1 to s2 when s2 is empty."""
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def add(self, new_element):
        # Add elements only to stack s1
        self.s1.append(new_element)

    def remove(self):
        self._fill_s2_if_empty()

        if not self.s2:
            raise IndexError("Queue is empty")

        # The top of s2 corresponds to the head of the queue
        return self.s2.pop()

    def front(self):
        """Returns the front element without removing it."""
        self._fill_s2_if_empty()

        if not self.s2:
            raise IndexError("Queue is empty")

        return self.s2[-1]

    def peek(self):
        """Alias for front()."""
        return self.front()

    def empty(self):
        # Queue is empty only if both stacks are empty
        return not self.s1 and not self.s2


def handle_error():
    print("Test failed")
    sys.exit(1)


def test():
    # Test for different number of elements in the queue
    for num_elems in range(MAX_NUM_QUEUE_ELEMS + 1):
        q = QueueUsingStacks()

        # Add all elements to the queue
        for j in range(num_elems):
            q.add(j)

        print(f"Queue size = {num_elems}, Elements are : ", end="")

        # Remove one element at a time from the queue and print it
        for j in range(num_elems):
            expected_val = j

            # Verify peek() and front() match the expected element before deletion
            if q.peek() != expected_val or q.front() != expected_val:
                handle_error()

            output_remove = q.remove()
            if output_remove != expected_val:
                handle_error()
            print(output_remove, end=" ")

        # Queue is now empty. Trying to remove should raise an exception
        caught_exception = False
        try:
            q.remove()
        except IndexError:
            caught_exception = True

        if not caught_exception:
            handle_error()

        print()
        print("__________________________________________")


if __name__ == "__main__":
    test()
    print("All tests passed successfully!")
