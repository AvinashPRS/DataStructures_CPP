"""3-Way Partitioning (Dutch National Flag Sort). TC: O(N), SC: O(1)"""
import random
import sys


def handle_error():
    print("Error occurred")
    sys.exit(1)


def dutch_sort(a, pivot_value):
    if not a:
        return

    cur_pos = 0
    left_pos = 0
    right_pos = len(a) - 1

    # main logic block: note just one while loop
    while cur_pos <= right_pos:
        if a[cur_pos] < pivot_value:
            a[left_pos], a[cur_pos] = a[cur_pos], a[left_pos]
            left_pos += 1
            cur_pos += 1
        elif a[cur_pos] > pivot_value:
            a[cur_pos], a[right_pos] = a[right_pos], a[cur_pos]
            right_pos -= 1  # Don't advance cur_pos; evaluate the newly swapped element
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
    i = 0
    while i < len(a) and a[i] < pivot_value:   # 1. less than pivot first
        i += 1
    while i < len(a) and a[i] == pivot_value:  # 2. equal to pivot next
        i += 1
    while i < len(a) and a[i] > pivot_value:   # 3. greater than pivot last
        i += 1

    if i != len(a):
        handle_error()

    print("After  : ", end="")
    print_array(a)
    print("_______________________________________________")


if __name__ == "__main__":
    MAX_NUM_ELEMENTS = 10
    MAX_VALUE = 10
    MAX_NUM_ITERATIONS = 10

    for _ in range(MAX_NUM_ITERATIONS):
        length = random.randint(1, MAX_NUM_ELEMENTS)
        a = [random.randint(0, MAX_VALUE - 1) for _ in range(length)]
        # Pick a random pivot value from within the newly generated values
        pivot_value = random.choice(a)
        test(a, pivot_value)

    print("Test passed")
