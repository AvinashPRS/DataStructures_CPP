"""
Implement a stack using two queues.

Time Complexity (unoptimized push / costly pop strategy):
    push(new_element): O(1)
        Appends the element directly to the end of q1.
    pop(): O(K), K = number of elements currently in the stack
        To get to the last element inserted (top of the stack), K-1 elements are shifted
        from q1 to q2 before the final element is extracted. N sequential pops on a stack
        of size N take N + (N-1) + ... + 1, i.e. O(N^2) in total.
    empty(): O(1)
"""
import sys
from collections import deque

MAX_NUM_ELEMS = 10


class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def empty(self):
        # Stack is empty only if both queues are empty
        return not self.q1 and not self.q2

    def push(self, new_element):
        # Add element to the end of queue q1
        self.q1.append(new_element)

    def pop(self):
        # If stack is empty, then raise an exception
        if self.empty():
            raise IndexError("Stack is empty")

        # Remove all elements from q1 and add them to q2 except the last item
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        # The last element in q1 is the top of stack
        e = self.q1.popleft()

        # Swap the queues q1 and q2 (q1 is now empty, all remaining elements are in q2)
        self.q1, self.q2 = self.q2, self.q1

        return e


def handle_error():
    print("Test failed")
    sys.exit(1)


def test():
    # Test for different number of elements in the stack
    for num_elems in range(MAX_NUM_ELEMS + 1):
        s = StackUsingQueues()

        # Add all the elements to the stack
        for j in range(num_elems):
            s.push(j)

        print(f"Stack size = {num_elems}, Elements are : ")

        # Remove one element at a time from the stack and print it
        for j in range(num_elems):
            output = s.pop()

            expected_val = num_elems - 1 - j
            if output != expected_val:
                handle_error()
            print(output)

        # Stack is now empty. Trying to remove an element now raises an exception
        caught_exception = False
        try:
            s.pop()
        except IndexError:
            caught_exception = True

        if not caught_exception:
            handle_error()

        print("__________________________________________")


if __name__ == "__main__":
    test()
    print("Test passed ")
