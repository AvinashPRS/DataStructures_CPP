"""
Given a max-heap in array form. Find the k largest elements from the heap without modifying the array.

Input: int list
Output: k largest ints

Solution:
    Use a max-heap of (value, index). The root is the largest, so push it first.
    Every time we pop the max element, add it to the result and push its children.
    Since a parent is always >= its children, the next largest must be among the
    children of already-extracted nodes.

    TC: O(klogk)
    SC: O(k) for heap
"""
import heapq


def k_largest_heap_elements(heap, k):
    if not heap or k <= 0:
        return []

    # max-heap via negated values: (-data, idx)
    max_heap = [(-heap[0], 0)]
    k_largest = []

    while max_heap and len(k_largest) < k:
        neg_data, idx = heapq.heappop(max_heap)
        k_largest.append(-neg_data)

        # add its child nodes if they exist
        left_idx, right_idx = 2 * idx + 1, 2 * idx + 2
        if left_idx < len(heap):
            heapq.heappush(max_heap, (-heap[left_idx], left_idx))
        if right_idx < len(heap):
            heapq.heappush(max_heap, (-heap[right_idx], right_idx))

    return k_largest


if __name__ == "__main__":
    k = 3
    heap = [562, 314, 401, 28, 156, 359, 271, 11, 3]
    print("".join(f"{a}, " for a in k_largest_heap_elements(heap, k)))  # 562, 401, 359,
