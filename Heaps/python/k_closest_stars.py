"""
Given a list of coordinates for points in 2D plane. Find the 'k' closest points from origin.

Input: list of coordinates, int k
Output: list of k closest coordinates

Solution:
    Traverse the coordinates and calculate the distance from origin as we go.
    To find the 'k' smallest distances we use a max-heap of size 'k'.
    Since it is a max-heap, it removes the farthest point every time size exceeds k.
    (Python's heapq is a min-heap, so we push negated distances.)

    TC: O(nlogk), k: heap size, n: no. of elements
    SC: O(k) for heap
"""
import heapq
import math
from collections import namedtuple

Coordinate = namedtuple("Coordinate", ["x", "y"])


def get_distance(pt):
    return math.sqrt(pt.x * pt.x + pt.y * pt.y)


def find_k_closest_points(pts, k):
    max_heap = []   # entries: (-dist, index, x, y)

    for i, pt in enumerate(pts):
        heapq.heappush(max_heap, (-get_distance(pt), i, pt.x, pt.y))
        # if size is greater than k, pop the farthest coordinate
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    k_closest_pts = []
    while max_heap:
        _, _, x, y = heapq.heappop(max_heap)
        k_closest_pts.append(Coordinate(x, y))
    return k_closest_pts


if __name__ == "__main__":
    pts = [Coordinate(-1, 0), Coordinate(5, 5), Coordinate(2, 3), Coordinate(9, 9), Coordinate(1, 0)]
    for p in find_k_closest_points(pts, 2):
        print(f"{p.x}, {p.y}")
