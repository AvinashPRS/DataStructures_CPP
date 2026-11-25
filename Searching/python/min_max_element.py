"""
Given an unsorted array of numbers, find the min and max element in min no. of comparisons.
Input: list of unsorted int
Output: min and max numbers

Solution:
    Doing linear traversal for finding takes 2n-2 comparisons. To use even fewer comparisons
    we can do the first level of tournament selection with the array. This takes
    n/2 comparisons for finding the winners and losers. Then finding the min and max
    amongst them takes n/2 - 1 each.
    Total: n/2 + 2*(n/2 - 1) = 3n/2 - 2

    TC: O(n)
"""


def find_min_max(arr):
    """Returns a tuple (min, max)."""
    # When there is only one element
    if len(arr) == 1:
        return arr[0], arr[0]

    # Initial value for min and max from first pair
    if arr[0] < arr[1]:
        cur_min, cur_max = arr[0], arr[1]
    else:
        cur_min, cur_max = arr[1], arr[0]

    i = 2
    while i < len(arr) - 1:
        # Check which amongst the pair is larger
        if arr[i] < arr[i + 1]:
            small, big = arr[i], arr[i + 1]
        else:
            small, big = arr[i + 1], arr[i]

        # Set min and max element
        cur_min = small if small < cur_min else cur_min
        cur_max = big if big > cur_max else cur_max
        i += 2

    # If there are odd no. of elements, one will be left
    if len(arr) % 2 != 0:
        last = arr[-1]
        cur_min = last if last < cur_min else cur_min
        cur_max = last if last > cur_max else cur_max

    return cur_min, cur_max


if __name__ == "__main__":
    arr = [2, 23, -23, -442, 99, 0, 34, 998, 634, -872]
    mn, mx = find_min_max(arr)

    print(f"Min: {mn} Max: {mx}")
