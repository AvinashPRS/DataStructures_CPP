"""
An array increases then decreases, possibly multiple times. Sort such an array.

Input: list of int
Output: sorted list

Solution:
    Split the array into monotonic runs. Increasing runs are added directly,
    decreasing runs are reversed first. Then merge the sorted runs with a min-heap:
    the heap holds the current element of each run; pop the smallest and push the
    next element from the same run.

    TC: O(nlogk), k: no. of runs, n: total elements
    SC: O(k) for the heap (+ O(n) for the runs)
"""
import heapq


def merge_multiple_sorted_vectors(arr):
    sorted_list = []
    min_heap = []   # (value, run_index, element_index)

    for i, run in enumerate(arr):
        if run:
            heapq.heappush(min_heap, (run[0], i, 0))

    while min_heap:
        value, run_idx, el_idx = heapq.heappop(min_heap)
        sorted_list.append(value)
        if el_idx + 1 < len(arr[run_idx]):
            heapq.heappush(min_heap, (arr[run_idx][el_idx + 1], run_idx, el_idx + 1))

    return sorted_list


def sort_increasing_decreasing_elements(arr):
    multiple_sorted_arrays = []
    n = len(arr)
    if n == 0:
        return []

    start = 0
    increasing = True
    for i in range(1, n + 1):
        # add the run when a junction point is reached or at the end
        if (i == n or
                (increasing and arr[i - 1] >= arr[i]) or
                (not increasing and arr[i - 1] < arr[i])):
            run = arr[start:i]
            if not increasing:
                run.reverse()
            multiple_sorted_arrays.append(run)
            start = i
            increasing = not increasing     # change the run type

    return merge_multiple_sorted_vectors(multiple_sorted_arrays)


if __name__ == "__main__":
    arr = [-1, 0, 5, 89, 7, 2, 5, 7, 9, 10, -22, 67, 89, 91, 100, 2, 8, 9, 10, 15, 77]
    result = sort_increasing_decreasing_elements(arr)
    print(" ".join(str(a) for a in result))
    assert result == sorted(arr), "Test failed"
