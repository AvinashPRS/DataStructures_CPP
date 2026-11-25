"""Dutch national flag (3-way partition) around a pivot value."""
import random
import sys

MAX_NUM_ELEMENTS = 10
MAX_VALUE = 10
MAX_NUM_ITERATIONS = 10


def handle_error():
    print("Error occured ")
    sys.exit(1)


def dutch_sort(a, pivot_value):
    """
    a: input list that has to be sorted
    pivot_value: after sorting, all elements smaller than pivot lie to the left,
    all greater lie to the right, and pivot values occur together in the middle.
    """
    cur_pos = 0
    left_pos = 0
    right_pos = len(a) - 1

    while cur_pos <= right_pos:
        if a[cur_pos] < pivot_value:
            a[left_pos], a[cur_pos] = a[cur_pos], a[left_pos]
            left_pos += 1  # Advance the left fill location
            cur_pos += 1   # Process the next element
        elif a[cur_pos] > pivot_value:
            a[cur_pos], a[right_pos] = a[right_pos], a[cur_pos]
            # Advance the right fill location. The element brought in from
            # right_pos must be processed, so don't advance cur_pos.
            right_pos -= 1
        else:
            cur_pos += 1


def print_array(a):
    print("".join(f"{x} " for x in a))


def test(a, pivot_value):
    print(f"Pivot value = {pivot_value}")
    print("Before : ", end="")
    print_array(a)

    dutch_sort(a, pivot_value)

    # Verify the result of dutch sort
    length = len(a)
    i = 0
    while i < length and a[i] < pivot_value:   # smaller elements first
        i += 1
    while i < length and a[i] == pivot_value:  # then pivot values
        i += 1
    while i < length and a[i] > pivot_value:   # then greater elements
        i += 1

    if i != length:
        handle_error()

    print("After  : ", end="")
    print_array(a)
    print("_______________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_ITERATIONS):
        length = 1 + random.randrange(MAX_NUM_ELEMENTS)
        a = [random.randrange(MAX_VALUE) for _ in range(length)]
        pivot_value = random.choice(a)  # Pick a random pivot
        test(a, pivot_value)
    print("Test passed")
