"""
Find the K nearest robots - variant using a custom comparator object.

C++ uses a functor struct (CompareDistance) for std::priority_queue. In Python,
the equivalent is a wrapper class whose __lt__ defines heap ordering. To get a
max-heap (farthest robot on top) with heapq's min-heap, __lt__ returns True when
`self` is FARTHER than `other`.
"""
import heapq
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Robot:
    id: int
    location: Point


class CompareDistance:
    """Captures the query point; is_closer(a, b) is True if a is closer than b."""

    def __init__(self, query):
        self.query = query

    def dist_sq(self, r):
        return ((r.location.x - self.query.x) ** 2 +
                (r.location.y - self.query.y) ** 2)

    def __call__(self, a, b):
        return self.dist_sq(a) < self.dist_sq(b)


class HeapItem:
    """Wraps a robot so heapq orders by the comparator (farthest first -> max-heap)."""
    __slots__ = ("robot", "comp")

    def __init__(self, robot, comp):
        self.robot = robot
        self.comp = comp

    def __lt__(self, other):
        return self.comp(other.robot, self.robot)


def find_k_nearest_robots(robots, query, k):
    if k <= 0 or not robots:
        return []

    comp = CompareDistance(query)
    max_heap = []

    for robot in robots:
        if len(max_heap) < k:
            heapq.heappush(max_heap, HeapItem(robot, comp))
        elif comp(robot, max_heap[0].robot):
            # robot is closer than the current farthest one
            heapq.heapreplace(max_heap, HeapItem(robot, comp))

    nearest = []
    while max_heap:
        nearest.append(heapq.heappop(max_heap).robot)

    # reverse to order from closest to farthest
    nearest.reverse()
    return nearest


if __name__ == "__main__":
    robots = [
        Robot(101, Point(2.0, 3.0)),
        Robot(102, Point(5.0, 4.0)),
        Robot(103, Point(9.0, 6.0)),
        Robot(104, Point(4.0, 7.0)),
        Robot(105, Point(1.0, 1.0)),
    ]
    query_point = Point(3.0, 3.0)
    k = 3

    closest = find_k_nearest_robots(robots, query_point, k)
    print(f"The {k} nearest robots to ({query_point.x:g}, {query_point.y:g}) are:")
    for r in closest:
        print(f"Robot ID: {r.id} at ({r.location.x:g}, {r.location.y:g})")
