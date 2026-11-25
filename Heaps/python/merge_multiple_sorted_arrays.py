"""
Merge multiple sorted lists into a single sorted list (like merging sorted files).

Input: 2d list of int
Output: 1d sorted list

Solution:
    Approach 1: Pairwise merge sorted lists. O(n logk) but O(n) extra space.

    Approach 2: Using heap:
        For 'k' lists, keep a min-heap of size 'k', initially filled with the
        first entry of each list. Pop the smallest and push the next element of
        the list it came from.

        TC: O(nlogk), k: no. of lists, n: total elements
        SC: O(k)
"""
import heapq


class Solution:
    def merge_k_sorted_arrays(self, arrays):
        result = []
        # min-heap entries: (value, array_index, element_index)
        min_heap = []

        # Step 1: push the first element of each non-empty array
        for i, arr in enumerate(arrays):
            if arr:
                heapq.heappush(min_heap, (arr[0], i, 0))

        # Step 2: extract the min and push the next element from the same array
        while min_heap:
            value, arr_idx, el_idx = heapq.heappop(min_heap)
            result.append(value)

            next_el_idx = el_idx + 1
            if next_el_idx < len(arrays[arr_idx]):
                heapq.heappush(min_heap, (arrays[arr_idx][next_el_idx], arr_idx, next_el_idx))

        return result


if __name__ == "__main__":
    # NOTE: the first row is not actually sorted (89, 7) - kept as in the original input
    arrays = [
        [-1, 0, 5, 89, 7],
        [2, 5, 7, 9, 10],
        [-22, 67, 89, 91, 100],
        [2, 8, 9, 10, 15, 77],
    ]
    merged = Solution().merge_k_sorted_arrays(arrays)
    print("Merged array: " + " ".join(str(n) for n in merged))

    # Pythonic one-liner alternative
    print("heapq.merge:  " + " ".join(str(n) for n in heapq.merge(*arrays)))
