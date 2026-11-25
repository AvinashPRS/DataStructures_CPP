"""
Find the longest sub-array with an equal number of 0's and 1's.

Solution:
    Treat 1 as +1 and 0 as -1 and keep a running sum. If the same running sum is
    seen at indices i and j, then a[i+1..j] has equal 0's and 1's. Store the first
    index at which every running sum is seen (running sum 0 at index -1).

    TC: O(n)
    SC: O(n)
"""
import random

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 2


def find_sub_array(a):
    """Returns (max_length, start_index, end_index)."""
    first_ix_for_sum = {0: -1}
    running_sum = max_length = 0
    start_index = end_index = -1

    for i, x in enumerate(a):
        running_sum += 1 if x else -1
        if running_sum not in first_ix_for_sum:
            first_ix_for_sum[running_sum] = i
        else:
            first_index = first_ix_for_sum[running_sum]
            if i - first_index > max_length:
                max_length = i - first_index
                start_index = first_index + 1
                end_index = i

    return max_length, start_index, end_index


def brute_force_sub_array(a):
    max_length = 0
    for i in range(len(a) - 1):
        running_sum = 2 * a[i] - 1
        for j in range(i + 1, len(a)):
            running_sum += 2 * a[j] - 1
            if running_sum == 0:
                max_length = max(max_length, j - i + 1)
    return max_length


def test():
    length = max(2, random.randint(1, MAX_NUM_ELEMS))
    a = [random.randrange(MAX_VALUE) for _ in range(length)]
    print(*a)

    result, start_index, end_index = find_sub_array(a)
    print(f"Length of longest sub array with equal 0's and 1's  = {result}, \n"
          f"\t(start index = {start_index}, end index = {end_index})")

    assert result == brute_force_sub_array(a), "Test failed"
    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
