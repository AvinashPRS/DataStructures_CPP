"""RRT planner with an ASCII visualisation (100x100 continuous map drawn on a 25x25 grid)."""
import math
import random
from dataclasses import dataclass

MAP_WIDTH = 100.0
MAP_HEIGHT = 100.0

# Grid rendering resolution (100x100 space mapped to a 25x25 display grid)
DISPLAY_ROWS = 25
DISPLAY_COLS = 25

# RRT Parameters
STEP_SIZE = 6.0
GOAL_RADIUS = 4.0
MAX_ITERATIONS = 5000
GOAL_SAMPLE_RATE = 0.15


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
    return any(math.hypot(x - o.x, y - o.y) <= o.radius for o in obstacles)


def is_segment_colliding(x1, y1, x2, y2, obstacles, checks=10):
    for i in range(checks + 1):
        t = i / checks
        if is_point_colliding(x1 + t * (x2 - x1), y1 + t * (y2 - y1), obstacles):
            return True
    return False


def get_random_sample(goal_x, goal_y):
    if random.random() < GOAL_SAMPLE_RATE:
        return Node(goal_x, goal_y)
    return Node(random.random() * MAP_WIDTH, random.random() * MAP_HEIGHT)


def get_nearest_node_idx(tree, sample):
    return min(range(len(tree)), key=lambda i: math.hypot(tree[i].x - sample.x, tree[i].y - sample.y))


def to_cell(x, y):
    c = min(int((x / MAP_WIDTH) * DISPLAY_COLS), DISPLAY_COLS - 1)
    r = min(int((y / MAP_HEIGHT) * DISPLAY_ROWS), DISPLAY_ROWS - 1)
    return r, c


def draw_visual_grid(path, start, goal, obstacles, title="RRT PATH VISUALIZATION"):
    """Maps continuous coordinates to a smaller, discrete console character matrix."""
    display = [['.'] * DISPLAY_COLS for _ in range(DISPLAY_ROWS)]

    # 1. Render Obstacles (map grid indices back to continuous space to check boundaries)
    for r in range(DISPLAY_ROWS):
        for c in range(DISPLAY_COLS):
            mx = (c / DISPLAY_COLS) * MAP_WIDTH
            my = (r / DISPLAY_ROWS) * MAP_HEIGHT
            if is_point_colliding(mx, my, obstacles):
                display[r][c] = '#'

    # 2. Render Path Trajectory
    for p in path:
        r, c = to_cell(p.x, p.y)
        display[r][c] = '*'

    # 3. Render Explicit Start and End Marks
    r, c = to_cell(start.x, start.y)
    display[r][c] = 'S'
    r, c = to_cell(goal.x, goal.y)
    display[r][c] = 'E'

    # 4. Print (inverted row printing so the Y-axis ascends vertically)
    print(f"\n================ {title} ================\n")
    for r in range(DISPLAY_ROWS - 1, -1, -1):
        print("  " + "".join(ch + " " for ch in display[r]))
    print("\n" + "=" * (len(title) + 34))


def plan_rrt(start, goal, obstacles):
    start.parent_idx = -1
    tree = [start]
    goal_node_idx = -1

    for _ in range(MAX_ITERATIONS):
        sample = get_random_sample(goal.x, goal.y)
        nearest_idx = get_nearest_node_idx(tree, sample)
        nearest = tree[nearest_idx]
        angle = math.atan2(sample.y - nearest.y, sample.x - nearest.x)
        new = Node(nearest.x + STEP_SIZE * math.cos(angle),
                   nearest.y + STEP_SIZE * math.sin(angle), nearest_idx)
        if 0 <= new.x <= MAP_WIDTH and 0 <= new.y <= MAP_HEIGHT:
            if not is_segment_colliding(nearest.x, nearest.y, new.x, new.y, obstacles):
                tree.append(new)
                if math.hypot(new.x - goal.x, new.y - goal.y) <= GOAL_RADIUS:
                    goal_node_idx = len(tree) - 1
                    break

    if goal_node_idx != -1:
        print("Path successfully located!")
        path = []
        idx = goal_node_idx
        while idx != -1:
            path.append(tree[idx])
            idx = tree[idx].parent_idx
        path.reverse()
        draw_visual_grid(path, start, goal, obstacles)
    else:
        print("RRT failed to locate a valid continuous path.")


# main code harness:
if __name__ == "__main__":
    random.seed()
    start = Node(10.0, 10.0)
    goal = Node(90.0, 90.0)
    # Continuous map circular blocking elements (X, Y, Radius)
    obstacles = [Obstacle(40.0, 45.0, 14.0), Obstacle(60.0, 65.0, 14.0), Obstacle(35.0, 75.0, 10.0)]
    plan_rrt(start, goal, obstacles)
