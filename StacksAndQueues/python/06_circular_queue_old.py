"""
Circular queue backed by a fixed-size buffer that doubles when full (older variant).

head: index of the first element in queue, -1 if empty
tail: index of the last element in queue, -1 if empty
TC: add: amortized O(1), remove: O(1)
"""
import sys

MAX_NUM_QUEUE_ELEMS = 10


def handle_error():
    print("Test failed")
    sys.exit(1)


class Queue:
    def __init__(self):
        self.head = -1     # index of the first element in queue. -1 if empty
        self.tail = -1     # index of last element in queue. -1 if empty
        self.count = 0     # number of elements currently present in the queue
        self.max_size = 1  # maximum number of elements that can be stored
        self.buffer = [None] * self.max_size

    def add(self, new_element):
        if self.count == self.max_size:
            # If the queue is full, double the internal buffer size
            new_buffer = [None] * (self.max_size * 2)
            old_pos = self.head

            # Copy sequentially from the old queue buffer to the new buffer
            for new_pos in range(self.count):
                new_buffer[new_pos] = self.buffer[old_pos]
                old_pos = (old_pos + 1) % self.max_size

            self.buffer = new_buffer
            self.head = 0
            self.tail = self.count - 1
            self.max_size *= 2

        # Advance the tail and insert the element
        self.tail = (self.tail + 1) % self.max_size
        self.buffer[self.tail] = new_element

        if self.count == 0:
            self.head = self.tail

        self.count += 1
        return 0

    def remove(self):
        if self.count <= 0:
            raise IndexError("Queue is empty")

        removed_element = self.buffer[self.head]

        if self.head == self.tail:
            # If only 1 item existed, reset head and tail to -1
            self.head = -1
            self.tail = -1
        else:
            # Advance the head index using circular modulo logic
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
