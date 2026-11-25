"""
There is a stream of numbers. Find the median at each instant.

Input: stream of int
Output: median at each instant

Solution:
    Keep two heaps: a max-heap for the smaller half and a min-heap for the larger
    half. The min-heap holds at most one more element than the max-heap.
    Insert each number in the right heap, rebalance, then:
      - equal sizes: median = avg of the two tops
      - otherwise:   median = min-heap top
    (Python's heapq is a min-heap, so the max-heap stores negated values.)

    TC: O(nlogn)
    SC: O(n) for heaps
"""
import heapq


def show_live_median(stream):
    medians = []
    max_heap = []   # smaller half (negated)
    min_heap = []   # larger half

    for token in stream.split(","):
        if not token:
            continue
        num = int(token)

        # 1. Insertion
        if not min_heap or num >= min_heap[0]:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -num)

        # 2. Rebalancing
        while len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        while len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # 3. Median
        if len(max_heap) == len(min_heap):
            medians.append((-max_heap[0] + min_heap[0]) / 2.0)
        else:
            medians.append(min_heap[0])

    return medians


if __name__ == "__main__":
    s = "1,0,3,5,2,0,1"
    # Outputs: 1, 0.5, 1, 2, 2, 1.5, 1,
    print("".join(f"{m:g}, " for m in show_live_median(s)))
