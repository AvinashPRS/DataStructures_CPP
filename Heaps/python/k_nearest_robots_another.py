"""
Find the K nearest robots - variant where the comparator is defined inline.

C++ passes a lambda comparator to std::priority_queue. Python's heapq has no
comparator argument, so the equivalent is a key function (closure over `query`)
and storing (-key, tiebreak, item) tuples to get max-heap behaviour.
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


def find_k_nearest_robots(robots, query, k):
    if k <= 0 or not robots:
        return []

    # "lambda" capturing query from the surrounding scope
    get_dist_sq = lambda r: ((r.location.x - query.x) ** 2 +
                             (r.location.y - query.y) ** 2)

    max_heap = []   # (-dist_sq, insertion order, robot)
    for i, robot in enumerate(robots):
        heapq.heappush(max_heap, (-get_dist_sq(robot), i, robot))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    nearest = []
    while max_heap:
        nearest.append(heapq.heappop(max_heap)[2])
    nearest.reverse()
    return nearest


def find_k_nearest_robots_nsmallest(robots, query, k):
    """Idiomatic Python alternative: heapq.nsmallest uses a bounded heap internally."""
    if k <= 0:
        return []
    return heapq.nsmallest(k, robots, key=lambda r: (r.location.x - query.x) ** 2 +
                                                    (r.location.y - query.y) ** 2)


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

    for fn in (find_k_nearest_robots, find_k_nearest_robots_nsmallest):
        closest = fn(robots, query_point, k)
        print(f"[{fn.__name__}] The {k} nearest robots to ({query_point.x:g}, {query_point.y:g}) are:")
        for r in closest:
            print(f"Robot ID: {r.id} at ({r.location.x:g}, {r.location.y:g})")
