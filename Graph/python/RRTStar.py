"""RRT* planner (choose-best-parent + rewiring) with an ASCII visualisation."""
import math
import random
from dataclasses import dataclass

MAP_WIDTH = 100.0
MAP_HEIGHT = 100.0

# Grid rendering resolution (100x100 space mapped to a 25x25 display grid)
DISPLAY_ROWS = 25
DISPLAY_COLS = 25

# RRT* Parameters
STEP_SIZE = 6.0          # Length of each growth step
GOAL_RADIUS = 4.0        # Proximity to goal to declare success
MAX_ITERATIONS = 3000    # Maximum iterations to optimize the tree
GOAL_SAMPLE_RATE = 0.15  # 15% bias to sample directly towards the goal
REWIRE_RADIUS = 15.0     # Search radius to find near neighbors for optimization


@dataclass
class Node:
    x: float
    y: float
    parent_idx: int = -1
    cost: float = 0.0  # Total cost accumulated from the start node to this node


@dataclass
class Obstacle:
    x: float
    y: float
    radius: float


def is_point_colliding(x, y, obstacles):
    return any(math.hypot(x - o.x, y - o.y) <= o.radius for o in obstacles)


def is_segment_colliding(x1, y1, x2, y2, obstacles, checks=12):
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


def draw_visual_grid(path, start, goal, obstacles):
    display = [['.'] * DISPLAY_COLS for _ in range(DISPLAY_ROWS)]
    # 1. Render Obstacles
    for r in range(DISPLAY_ROWS):
        for c in range(DISPLAY_COLS):
            if is_point_colliding((c / DISPLAY_COLS) * MAP_WIDTH, (r / DISPLAY_ROWS) * MAP_HEIGHT, obstacles):
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

    print("\n================ RRT* PATH VISUALIZATION ================\n")
    for r in range(DISPLAY_ROWS - 1, -1, -1):
        print("  " + "".join(ch + " " for ch in display[r]))
    print("\n=========================================================")


def plan_rrt_star(start, goal, obstacles):
    start.parent_idx, start.cost = -1, 0.0
    tree = [start]
    best_goal_node_idx = -1
    min_goal_cost = float("inf")

    for _ in range(MAX_ITERATIONS):
        # 1. Sample a random point
        sample = get_random_sample(goal.x, goal.y)
        # 2. Find nearest node in the tree
        nearest_idx = get_nearest_node_idx(tree, sample)
        nearest = tree[nearest_idx]
        # 3. Steer towards sample point by STEP_SIZE
        angle = math.atan2(sample.y - nearest.y, sample.x - nearest.x)
        nx = nearest.x + STEP_SIZE * math.cos(angle)
        ny = nearest.y + STEP_SIZE * math.sin(angle)

        # Skip if outside map boundaries or instantly colliding
        if nx < 0 or nx > MAP_WIDTH or ny < 0 or ny > MAP_HEIGHT:
            continue
        if is_segment_colliding(nearest.x, nearest.y, nx, ny, obstacles):
            continue

        # --- RRT* Optimization Step 1: Choose Best Parent ---
        best_parent_idx = nearest_idx
        min_cost = nearest.cost + math.hypot(nx - nearest.x, ny - nearest.y)
        near_indices = []
        # Gather all existing nodes within REWIRE_RADIUS
        for i, t in enumerate(tree):
            d = math.hypot(t.x - nx, t.y - ny)
            if d <= REWIRE_RADIUS:
                near_indices.append(i)
                # Does connecting to this near node give a lower total cost?
                potential = t.cost + d
                if potential < min_cost and not is_segment_colliding(t.x, t.y, nx, ny, obstacles):
                    min_cost = potential
                    best_parent_idx = i

        # Commit the node with its optimized parent and cost
        new = Node(nx, ny, best_parent_idx, min_cost)
        tree.append(new)
        new_idx = len(tree) - 1

        # --- RRT* Optimization Step 2: Rewire Nearby Nodes ---
        for ni in near_indices:
            nb = tree[ni]
            rewire_cost = new.cost + math.hypot(new.x - nb.x, new.y - nb.y)
            # If pathing THROUGH our new node is cheaper for the neighbor, rewire its parent
            if rewire_cost < nb.cost and not is_segment_colliding(new.x, new.y, nb.x, nb.y, obstacles):
                nb.parent_idx = new_idx
                nb.cost = rewire_cost

        # Keep track of the best path touching the goal radius
        if math.hypot(new.x - goal.x, new.y - goal.y) <= GOAL_RADIUS and new.cost < min_goal_cost:
            min_goal_cost = new.cost
            best_goal_node_idx = new_idx

    # Trace path
    if best_goal_node_idx != -1:
        print(f"Optimized Path located! Total Cost: {min_goal_cost:g}")
        path = []
        idx = best_goal_node_idx
        while idx != -1:
            path.append(tree[idx])
            idx = tree[idx].parent_idx
        path.reverse()
        draw_visual_grid(path, start, goal, obstacles)
    else:
        print("RRT* failed to locate a valid path.")


# main code harness:
if __name__ == "__main__":
    random.seed()
    start = Node(10.0, 10.0)
    goal = Node(90.0, 90.0)
    obstacles = [Obstacle(40.0, 45.0, 14.0), Obstacle(60.0, 65.0, 14.0), Obstacle(35.0, 75.0, 10.0)]
    plan_rrt_star(start, goal, obstacles)
