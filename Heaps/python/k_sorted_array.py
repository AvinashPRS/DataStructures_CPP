"""
Given an array where each element is at most k places away from its sorted
position, sort the array.

Input: list of int
Output: sorted list

Solution:
    The first element of the sorted output must be among the first k+1 elements,
    so keep a min-heap of size k+1. Pop the min into the write position and
    push the next element. Continue until the heap is empty.

    TC: O(nlogk), k: heap size, n: no. of elements
    SC: O(k) for heap
"""
import heapq


def k_sorted_data(arr, k):
    if not arr:
        return arr

    n = len(arr)
    initial_elements = min(k + 1, n)
    min_heap = arr[:initial_elements]
    heapq.heapify(min_heap)

    write_idx = 0
    i = initial_elements
    while min_heap:
        arr[write_idx] = heapq.heappop(min_heap)
        write_idx += 1
        # push the next element into the window if it exists
        if i < n:
            heapq.heappush(min_heap, arr[i])
            i += 1

    return arr


if __name__ == "__main__":
    arr = [3, -1, 2, 6, 24, 15, 28]
    k = 2
    k_sorted_data(arr, k)
    print(" ".join(str(a) for a in arr))   # -1 2 3 6 15 24 28
