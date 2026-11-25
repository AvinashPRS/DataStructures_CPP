"""
Find the K nearest robots by sorting all robots by distance (O(n log n)).
"""
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

    # sort from closest to farthest; the lambda captures `query` from the enclosing scope
    ordered = sorted(robots, key=lambda r: (r.location.x - query.x) ** 2 +
                                           (r.location.y - query.y) ** 2)
    # keep only the first K (slicing safely handles k > len(robots))
    return ordered[:k]


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
