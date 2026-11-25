"""Dutch national flag partitioning around a pivot value."""
import random
import sys

MAX_NUM_ELEMENTS = 10
MAX_VALUE = 10
MAX_NUM_ITERATIONS = 10


def handle_error():
    print("Error occured ")
    sys.exit(1)


def dutch_sort(a, pivot_value):
    """After sorting, elements < pivot come first, then pivot values,
    then elements > pivot."""
    cur_pos, left_pos, right_pos = 0, 0, len(a) - 1
    while cur_pos <= right_pos:
        if a[cur_pos] < pivot_value:
            a[left_pos], a[cur_pos] = a[cur_pos], a[left_pos]
            left_pos += 1  # advance the left fill location
            cur_pos += 1   # process the next element
        elif a[cur_pos] > pivot_value:
            a[cur_pos], a[right_pos] = a[right_pos], a[cur_pos]
            # the element brought in from right_pos still has to be
            # processed, so don't advance cur_pos
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

    # Verify: smaller, then equal, then greater elements
    i, length = 0, len(a)
    while i < length and a[i] < pivot_value:
        i += 1
    while i < length and a[i] == pivot_value:
        i += 1
    while i < length and a[i] > pivot_value:
        i += 1
    if i != length:
        handle_error()

    print("After  : ", end="")
    print_array(a)
    print("_______________________________________________")


def main():
    for _ in range(MAX_NUM_ITERATIONS):
        length = 1 + random.randrange(MAX_NUM_ELEMENTS)
        a = [random.randrange(MAX_VALUE) for _ in range(length)]
        pivot_value = a[random.randrange(length)]
        test(a, pivot_value)
    print("Test passed")


if __name__ == "__main__":
    main()
