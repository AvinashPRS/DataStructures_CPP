"""
    Given K sorted arrays, select one element from each array such that the interval
    diff. for those K elements is min.
    Eg: Suppose result is {22, 3, 9, 89} : Here interval is [3, 89] for K diff arrays
    Solution:
        Start with the first element of each of the K arrays.
        While none of the arrays is finished:
            1. pick the min amongst K and compute interval diff, then remove it
            2. min_diff = min(min_diff, current interval diff)
            3. take the next element from the array the min element belonged to
            4. if that array has no more elements, exit
        Once an array is finished, the lower limit can't increase any more, so the
        interval can only grow.
        The C++ version keeps the K candidates in a BST (std::multimap); here a
        min-heap plus the running maximum is used.
        TC: O(nlogk), n: total number of elements
        SC: O(k)
"""
import heapq


def find_k_smallest_interval(arr):
    """Finds the smallest interval difference for K elements."""
    # each entry: (value, array index, element index)
    k_interval = [(a[0], i, 0) for i, a in enumerate(arr)]
    heapq.heapify(k_interval)
    upper_limit = max(a[0] for a in arr)
    min_diff = float("inf")
    while True:
        lower_limit, i, j = k_interval[0]
        min_diff = min(min_diff, upper_limit - lower_limit)
        # the array of the lower limit has no more elements -> done
        if j + 1 == len(arr[i]):
            return min_diff
        # replace the lower limit with the next element of its array
        heapq.heapreplace(k_interval, (arr[i][j + 1], i, j + 1))
        upper_limit = max(upper_limit, arr[i][j + 1])


def main():
    arr = [
        [5, 10, 15],
        [3, 6, 9, 12, 15],
        [8, 16, 24],
    ]
    print(find_k_smallest_interval(arr))


if __name__ == "__main__":
    main()
