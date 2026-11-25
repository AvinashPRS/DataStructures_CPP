"""
Given a list of disjoint intervals (start, end) and an input interval, return the
updated set of disjoint intervals.
e.g. <1,4>, <5,6>, <7,8> with input <2,6> -> <1,6>, <7,8>

Solution:
    Add the intervals before the input interval; once we hit an intersecting interval,
    take the union. Keep doing that. Then add the remaining non-intersecting intervals.

    TC: O(n) if sorted, O(n log n) here since we sort first.
"""
import heapq
from dataclasses import dataclass


@dataclass
class Interval:
    start: int
    end: int


def is_intersecting(a, b):
    """Checks if two intervals intersect."""
    return (a.start <= b.end <= a.end) or (b.start <= a.end <= b.end)


def merge_disjoint_intervals_unsorted(intervals, new_interval):
    """Merges a new interval into an UNSORTED set of disjoint intervals."""
    # 1. Sort the intervals by start time using a lambda. TC: O(n log n)
    intervals = sorted(intervals, key=lambda iv: iv.start)
    new_interval = Interval(new_interval.start, new_interval.end)

    disjoint_intervals = []
    i, n = 0, len(intervals)

    # 2. Add all non-intersecting intervals that sit BEFORE new_interval
    while i < n and not is_intersecting(intervals[i], new_interval) \
            and intervals[i].end < new_interval.start:
        disjoint_intervals.append(intervals[i])
        i += 1

    # 3. Consume and unify all overlapping intervals into new_interval
    while i < n and is_intersecting(intervals[i], new_interval):
        new_interval.start = min(intervals[i].start, new_interval.start)
        new_interval.end = max(intervals[i].end, new_interval.end)
        i += 1

    disjoint_intervals.append(new_interval)

    # 4. Add all remaining intervals (guaranteed to be AFTER)
    disjoint_intervals.extend(intervals[i:])

    return disjoint_intervals


def merge_intervals_with_heap(intervals, new_interval):
    """
    Alternative: merges unsorted intervals using a min heap.
    TC: O(n log n), SC: O(n)
    """
    # Heap ordered by (start, end): earliest start first, earlier end breaks ties
    min_heap = [(iv.start, iv.end) for iv in intervals]
    min_heap.append((new_interval.start, new_interval.end))
    heapq.heapify(min_heap)

    merged = []
    cur_start, cur_end = heapq.heappop(min_heap)

    while min_heap:
        nxt_start, nxt_end = heapq.heappop(min_heap)
        if nxt_start <= cur_end:
            # Overlap: merge
            cur_end = max(cur_end, nxt_end)
        else:
            # No overlap: current is complete
            merged.append(Interval(cur_start, cur_end))
            cur_start, cur_end = nxt_start, nxt_end

    # Don't forget the final remaining interval
    merged.append(Interval(cur_start, cur_end))
    return merged


def print_intervals(intervals):
    for iv in intervals:
        print(f"<{iv.start}, {iv.end}>")


if __name__ == "__main__":
    # Input is deliberately scrambled and unsorted
    intervals = [Interval(14, 15), Interval(1, 5), Interval(-22, -1),
                 Interval(11, 13), Interval(6, 10)]
    new_interval = Interval(2, 13)

    print("Merged Intervals (from unsorted input):")
    print_intervals(merge_disjoint_intervals_unsorted(intervals, new_interval))

    print("Merged Intervals (using Min-Heap):")
    print_intervals(merge_intervals_with_heap(intervals, new_interval))
