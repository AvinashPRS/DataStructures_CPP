"""Rapidly-exploring Random Tree (RRT) planner in a 100x100 continuous map with circular obstacles."""
import math
import random
from dataclasses import dataclass

# Environment boundaries
MAP_WIDTH = 100.0
MAP_HEIGHT = 100.0

# RRT Parameters
STEP_SIZE = 5.0          # Length of each growth step
GOAL_RADIUS = 3.0        # Proximity to goal to declare success
MAX_ITERATIONS = 5000    # Maximum tree nodes to generate
GOAL_SAMPLE_RATE = 0.1   # 10% bias to sample directly towards the goal


@dataclass
class Node:
    x: float
    y: float
    parent_idx: int = -1


@dataclass
class Obstacle:
    x: float
    y: float
    radius: float


def is_point_colliding(x, y, obstacles):
    """Check if a point falls inside any circular obstacle."""
    return any(math.hypot(x - o.x, y - o.y) <= o.radius for o in obstacles)


def is_segment_colliding(x1, y1, x2, y2, obstacles, checks=10):
    """Check if a line segment intersects an obstacle (sampled at `checks` interpolation points)."""
    for i in range(checks + 1):
        t = i / checks
        if is_point_colliding(x1 + t * (x2 - x1), y1 + t * (y2 - y1), obstacles):
            return True
    return False


def get_random_sample(goal_x, goal_y):
    """Random sample with goal biasing, so the tree explores aggressively towards the goal."""
    if random.random() < GOAL_SAMPLE_RATE:
        return Node(goal_x, goal_y)
    return Node(random.random() * MAP_WIDTH, random.random() * MAP_HEIGHT)


def get_nearest_node_idx(tree, sample):
    """Index of the node closest to the sample point."""
    return min(range(len(tree)), key=lambda i: math.hypot(tree[i].x - sample.x, tree[i].y - sample.y))


def plan_rrt(start, goal, obstacles):
    start.parent_idx = -1
    tree = [start]
    goal_node_idx = -1

    for _ in range(MAX_ITERATIONS):
        # 1. Sample a random point
        sample = get_random_sample(goal.x, goal.y)
        # 2. Find nearest node in the tree
        nearest_idx = get_nearest_node_idx(tree, sample)
        nearest = tree[nearest_idx]
        # 3. Extend towards sample point by STEP_SIZE
        angle = math.atan2(sample.y - nearest.y, sample.x - nearest.x)
        new = Node(nearest.x + STEP_SIZE * math.cos(angle),
                   nearest.y + STEP_SIZE * math.sin(angle), nearest_idx)
        # 4. Collision check
        if 0 <= new.x <= MAP_WIDTH and 0 <= new.y <= MAP_HEIGHT:
            if not is_segment_colliding(nearest.x, nearest.y, new.x, new.y, obstacles):
                tree.append(new)
                # 5. Check if we are close enough to the goal
                if math.hypot(new.x - goal.x, new.y - goal.y) <= GOAL_RADIUS:
                    goal_node_idx = len(tree) - 1
                    break

    # 6. Trace and display the path if found
    if goal_node_idx != -1:
        print("Path successfully located!")
        path = []
        idx = goal_node_idx
        while idx != -1:
            path.append(tree[idx])
            idx = tree[idx].parent_idx
        path.reverse()
        print("\nPath Coordinates (Start -> Goal):")
        for p in path:
            print(f"({p.x:g}, {p.y:g})")
        print(f"({goal.x:g}, {goal.y:g})")  # Explicit final goal snap
    else:
        print("RRT failed to find a valid path within the iteration limit.")


# main code harness:
if __name__ == "__main__":
    random.seed()  # seeded from time / OS entropy like srand(time(0))
    start = Node(10.0, 10.0)
    goal = Node(90.0, 90.0)
    # A few circular obstacles blocking the middle of the field
    obstacles = [Obstacle(40.0, 40.0, 12.0), Obstacle(50.0, 60.0, 10.0), Obstacle(30.0, 70.0, 8.0)]
    plan_rrt(start, goal, obstacles)
