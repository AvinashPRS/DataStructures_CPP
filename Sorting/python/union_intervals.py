"""
Given unsorted intervals whose endpoints may be open or closed, merge intersecting
intervals and return the disjoint set.
e.g. [1,4), [1,6], (5,6), [5,8], (9,18)  ->  [1, 8], (9, 18)

Solution:
    Sort by left endpoint (on a tie, a closed endpoint comes before an open one).
    Walk the list, extending the current union while the next interval intersects it;
    otherwise emit the union and start a new one from the current interval.

    TC: O(n log n)
"""
from dataclasses import dataclass, replace


@dataclass
class Endpoint:
    is_closed: bool
    val: int


@dataclass
class Interval:
    left: Endpoint
    right: Endpoint


def union_intervals(intervals):
    if not intervals:
        return []

    # sort by left endpoint; closed (key 0) before open (key 1) on ties
    intervals = sorted(intervals, key=lambda iv: (iv.left.val, 0 if iv.left.is_closed else 1))

    disjoint_intervals = []
    union_interval = replace(intervals[0])

    for iv in intervals[1:]:
        intersects = (
            # left of current touches right of union and at least one is closed
            (union_interval.right.val == iv.left.val
             and (union_interval.right.is_closed or iv.left.is_closed))
            # or left of current lies before right of union
            or union_interval.right.val > iv.left.val
        )
        if intersects:
            # extend union_interval's right endpoint if needed
            if (union_interval.right.val < iv.right.val
                    or (union_interval.right.val == iv.right.val and iv.right.is_closed)):
                union_interval.right = iv.right
        else:
            # emit the union found so far and start a new one
            disjoint_intervals.append(union_interval)
            union_interval = replace(iv)

    # add the last union interval
    disjoint_intervals.append(union_interval)
    return disjoint_intervals


def fmt(iv):
    return (("[" if iv.left.is_closed else "(") + f"{iv.left.val}, {iv.right.val}"
            + ("]" if iv.right.is_closed else ")"))


if __name__ == "__main__":
    # sorted : [1,4), [1,6], (5,6), [5,8], (9,18)
    #      ==> [1, 8], (9, 18)
    E = Endpoint
    events = [
        Interval(E(True, 1), E(False, 4)),
        Interval(E(False, 5), E(False, 6)),
        Interval(E(True, 1), E(True, 6)),
        Interval(E(False, 9), E(False, 18)),
        Interval(E(True, 5), E(True, 8)),
    ]
    for iv in union_intervals(events):
        print(fmt(iv))
    print()
