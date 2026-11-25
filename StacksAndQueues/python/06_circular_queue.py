"""
Circular queue backed by a fixed-size buffer that doubles when full.

head: index of the first element in queue
tail: index of free slot just after the last element in queue
TC: add: amortized O(1), remove: O(1)
"""
import sys

MAX_NUM_QUEUE_ELEMS = 10


def handle_error():
    print("Test failed")
    sys.exit(1)


class Queue:
    def __init__(self):
        self.head = 0      # index of the first element in queue
        self.tail = 0      # index of free slot just after last element in queue
        self.count = 0     # number of elements currently present in the queue
        self.max_size = 1  # maximum number of elements that can be stored in the queue
        self.buffer = [None] * self.max_size

    def add(self, new_element):
        if self.count == self.max_size:
            # If the queue is full, then resize the queue
            new_buffer = [None] * (self.max_size * 2)
            old_pos = self.head

            # Copy from the old queue buffer to the new buffer
            for new_pos in range(self.count):
                new_buffer[new_pos] = self.buffer[old_pos]
                old_pos = (old_pos + 1) % self.max_size

            self.buffer = new_buffer
            self.head = 0
            self.tail = self.count
            self.max_size *= 2

        # Insert the element at the tail of the queue and advance the tail
        self.buffer[self.tail] = new_element
        self.tail = (self.tail + 1) % self.max_size
        self.count += 1

        # Return the result code indicating success
        return 0

    def remove(self):
        # Can't remove an item from an empty queue
        if self.count <= 0:
            raise IndexError("Queue is empty")

        removed_element = self.buffer[self.head]

        # Advance the head to the next location
        self.head = (self.head + 1) % self.max_size
        self.count -= 1

        return removed_element

    def print_queue(self):
        items = []
        pos = self.head
        for _ in range(self.count):
            items.append(str(self.buffer[pos]))
            pos = (pos + 1) % self.max_size

        print("Queue: " + "".join(i + " " for i in items))
        print("___________________________________________________")


def test():
    q = Queue()

    # Test for different number of elements in the circular queue
    for num_elems in range(MAX_NUM_QUEUE_ELEMS + 1):
        # Add elements to the queue
        for i in range(num_elems):
            q.add(i)
            print(f"Inserting element {i}")
            q.print_queue()

        # Remove all elements from the queue
        for i in range(num_elems):
            result = q.remove()

            print(f"Removing element {result} from queue")
            q.print_queue()

            if result != i:
                handle_error()

        # The queue is now empty. So trying to remove an element should raise an error
        caught_exception = False
        try:
            q.remove()
        except IndexError:
            caught_exception = True

        if not caught_exception:
            handle_error()


if __name__ == "__main__":
    test()
    print("Test passed ")
