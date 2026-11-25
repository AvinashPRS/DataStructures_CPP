"""
Find the K nearest robots to a query point using a max-heap of size K.

We keep the farthest of the K closest robots at the top so it can be removed
when a closer robot shows up. Python's heapq is a min-heap, so we store the
negated squared distance.
Squared distance is used to avoid sqrt() during comparisons.
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


def get_squared_distance(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    return dx * dx + dy * dy


def find_k_nearest_robots(robots, query, k):
    if k <= 0 or not robots:
        return []

    max_heap = []   # entries: (-dist_sq, robot_index)
    for i, robot in enumerate(robots):
        dist_sq = get_squared_distance(robot.location, query)
        if len(max_heap) < k:
            heapq.heappush(max_heap, (-dist_sq, i))
        elif dist_sq < -max_heap[0][0]:
            heapq.heapreplace(max_heap, (-dist_sq, i))

    nearest = []
    while max_heap:
        nearest.append(robots[heapq.heappop(max_heap)[1]])

    # reverse so the output is ordered from closest to farthest
    nearest.reverse()
    return nearest


# ---- Variant: robots with integer coords, distance from an arbitrary reference point ----

@dataclass
class IntRobot:
    id: int
    x: int
    y: int


def get_distance(robot, ref_x=0, ref_y=0):
    dx, dy = robot.x - ref_x, robot.y - ref_y
    return dx * dx + dy * dy


def find_k_nearest_robots_ref(robots, k, ref_x=0, ref_y=0):
    if k <= 0:
        return []
    max_heap = []
    for i, robot in enumerate(robots):
        heapq.heappush(max_heap, (-get_distance(robot, ref_x, ref_y), i))
        if len(max_heap) > k:       # remove the farthest robot
            heapq.heappop(max_heap)
    nearest = []
    while max_heap:
        nearest.append(robots[heapq.heappop(max_heap)[1]])
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

    print("\n--- Integer robots, reference point (0, 0) and (3, 2) ---")
    int_robots = [IntRobot(1, -1, 0), IntRobot(2, 5, 5), IntRobot(3, 2, 3), IntRobot(4, 9, 9), IntRobot(5, 1, 0)]
    for ref in ((0, 0), (3, 2)):
        print(f"Reference point: {ref}")
        for r in find_k_nearest_robots_ref(int_robots, 2, *ref):
            print(f"Robot ID: {r.id} Position: ({r.x}, {r.y}) Distance squared: {get_distance(r, *ref)}")
