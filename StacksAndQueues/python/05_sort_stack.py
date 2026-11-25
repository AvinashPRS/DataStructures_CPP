"""
Sort a stack using only another stack.

Input elements are stored in original_stack. At the end of the operation,
original_stack will be empty and sorted_stack will have the elements in sorted order
(smallest on top).
TC: O(n^2), SC: O(n)
"""
import random
import sys

MAX_NUM_STACK_ELEMS = 10
MAX_VALUE = 20


def handle_error():
    print("Test failed")
    sys.exit(1)


def stack_sort(original_stack, sorted_stack):
    while original_stack:  # Original stack should be empty at the end
        e1 = original_stack.pop()

        # If sorted stack is empty OR e1 <= top element of sorted stack,
        # then push e1 onto the sorted stack
        if not sorted_stack or e1 <= sorted_stack[-1]:
            sorted_stack.append(e1)
            continue

        # While e1 > top element of sorted stack, remove the top element of
        # sorted stack and push it onto the original stack
        while sorted_stack and e1 > sorted_stack[-1]:
            original_stack.append(sorted_stack.pop())

        sorted_stack.append(e1)  # Push e1 onto the sorted stack


def test_stack():
    # Test for different sizes of the stack
    for num_elems in range(MAX_NUM_STACK_ELEMS + 1):
        original_stack = [random.randrange(MAX_VALUE) for _ in range(num_elems)]
        sorted_stack = []

        # Sort the stack. The sorted results will be in sorted_stack
        stack_sort(original_stack, sorted_stack)

        print(f"Sorted stack contents are (Size {num_elems}): ")
        prev_data = -1
        for _ in range(num_elems):
            # Pop an element from the sorted stack
            popped_value = sorted_stack.pop()
            print(popped_value, end=" ")

            # Verify if the data in stack is in ascending order
            if prev_data > popped_value:
                handle_error()

            prev_data = popped_value
        print("\n_________________________________________________")

    print("Test passed ")


if __name__ == "__main__":
    test_stack()
