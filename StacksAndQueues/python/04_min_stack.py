"""
Stack that supports retrieving the minimum element in O(1).

Solution:
    Along with the main stack keep a min stack. While pushing, push the element on the
    min stack too if it is <= the current minimum. While popping, if the popped element
    equals the top of the min stack, pop the min stack as well.
    TC: O(1) for push, pop and min
"""
import random
import sys

MAX_NUM_STACK_ELEMS = 100
MAX_VALUE = 10


def handle_error():
    print("Test failed")
    sys.exit(1)


def add_element(main_stack, min_stack, data_to_add):
    main_stack.append(data_to_add)

    if not min_stack or data_to_add <= min_stack[-1]:
        min_stack.append(data_to_add)


def remove_element(main_stack, min_stack):
    if not main_stack:
        raise IndexError("Stack is empty")

    popped_element = main_stack.pop()

    if popped_element == min_stack[-1]:
        min_stack.pop()

    return popped_element


def find_smallest(number_array, max_index):
    """Brute-force minimum of number_array[0..max_index], used for verification."""
    if max_index < 0:
        return 0xFFFFFFF
    return min(number_array[: max_index + 1])


def test_stack():
    number_array = [0] * MAX_NUM_STACK_ELEMS

    # Test for different sizes of the stacks
    for num_elems in range(MAX_NUM_STACK_ELEMS + 1):
        main_stack = []
        min_stack = []

        for j in range(num_elems):
            number_array[j] = random.randrange(MAX_VALUE)

            add_element(main_stack, min_stack, number_array[j])

            if min_stack[-1] != find_smallest(number_array, j):
                handle_error()

        for j in range(num_elems):
            # Verify the remaining sub-segment of array values matches the min_stack
            if min_stack[-1] != find_smallest(number_array, num_elems - 1 - j):
                handle_error()

            remove_element(main_stack, min_stack)

        if min_stack or main_stack:
            handle_error()

        caught_exception = False
        try:
            remove_element(main_stack, min_stack)
        except IndexError:
            caught_exception = True

        if not caught_exception:
            handle_error()

    print("Test passed ")


if __name__ == "__main__":
    test_stack()
