"""Hybrid A* for a car-like vehicle (bicycle kinematic model) on a 20x20 grid with heading bins."""
import heapq
import itertools
import math
from dataclasses import dataclass

# --- Configuration Parameters ---
MAP_W = 20        # Grid Width (X)
MAP_H = 20        # Grid Height (Y)
NUM_THETAS = 72   # Discrete heading bins (360 degrees / 5-degree increments)

GRID_RESOLUTION = 1.0
WHEELBASE = 1.5   # Vehicle length metric (L)
MAX_STEER = 0.6   # Maximum steering angle in radians (~35 degrees)
MOVE_STEP = 0.8   # Forward driving distance per step


@dataclass
class State:
    """Continuous real-world state."""
    x: float
    y: float
    theta: float
    direction: int = 0  # 1 = Forward, -1 = Backward, 0 = none yet


@dataclass
class Node:
    f: float
    g: float
    state: State
    parent_idx: int
    self_idx: int


def state_to_3d_index(x, y, theta):
    """Convert continuous poses into discrete 3D index bins."""
    xi = min(max(0, int(x / GRID_RESOLUTION)), MAP_W - 1)
    yi = min(max(0, int(y / GRID_RESOLUTION)), MAP_H - 1)
    theta %= 2 * math.pi  # Normalize heading between 0 and 2*PI
    ti = int((theta / (2 * math.pi)) * NUM_THETAS) % NUM_THETAS
    return xi + yi * MAP_W + ti * (MAP_W * MAP_H)


def euclidean_heuristic(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)


def move_vehicle(cur, steering_angle, step_size, direction):
    """Bicycle Kinematic Model update."""
    d = step_size * direction
    # If steering is nearly straight, move linearly to avoid divide-by-zero
    if abs(steering_angle) < 1e-4:
        return State(cur.x + d * math.cos(cur.theta), cur.y + d * math.sin(cur.theta), cur.theta, direction)
    # Apply kinematic equations based on steering orientation
    turn_radius = WHEELBASE / math.tan(steering_angle)
    new_theta = cur.theta + d / turn_radius
    return State(cur.x + turn_radius * (math.sin(new_theta) - math.sin(cur.theta)),
                 cur.y - turn_radius * (math.cos(new_theta) - math.cos(cur.theta)),
                 new_theta, direction)


def is_valid(x, y, grid):
    """Check boundary criteria and cross-reference 2D wall data."""
    if x < 0 or x >= MAP_W or y < 0 or y >= MAP_H:
        return False
    return grid[int(y / GRID_RESOLUTION)][int(x / GRID_RESOLUTION)] == 0  # Walkable if 0


def hybrid_a_star(grid, start, goal):
    total_bins = MAP_W * MAP_H * NUM_THETAS
    closed = [False] * total_bins
    g_costs = [float("inf")] * total_bins
    registry = {}  # bin index -> Node
    counter = itertools.count()
    open_list = []

    start_idx = state_to_3d_index(start.x, start.y, start.theta)
    g_costs[start_idx] = 0
    registry[start_idx] = Node(euclidean_heuristic(start.x, start.y, goal.x, goal.y), 0.0, start, -1, start_idx)
    heapq.heappush(open_list, (registry[start_idx].f, next(counter), start_idx))

    steering_inputs = [-MAX_STEER, 0.0, MAX_STEER]  # Left, Straight, Right
    directions = [1, -1]                             # Forward, Reverse Gear
    goal_idx = -1

    while open_list:
        _, _, idx = heapq.heappop(open_list)
        if closed[idx]:
            continue
        closed[idx] = True
        curr = registry[idx]

        # Proximity threshold to safely catch goal
        if euclidean_heuristic(curr.state.x, curr.state.y, goal.x, goal.y) < 1.0:
            goal_idx = idx
            break

        # Branch out kinematic possibilities
        for d in directions:
            for steer in steering_inputs:
                nxt = move_vehicle(curr.state, steer, MOVE_STEP, d)
                if not is_valid(nxt.x, nxt.y, grid):
                    continue
                nidx = state_to_3d_index(nxt.x, nxt.y, nxt.theta)
                if closed[nidx]:
                    continue
                # Penalize reverse driving and gear shifts to favour forward movement
                edge = MOVE_STEP
                if d == -1:
                    edge *= 2.5
                if curr.state.direction != d and curr.state.direction != 0:
                    edge += 1.0
                new_g = curr.g + edge
                if new_g < g_costs[nidx]:
                    g_costs[nidx] = new_g
                    h = euclidean_heuristic(nxt.x, nxt.y, goal.x, goal.y)
                    registry[nidx] = Node(new_g + h, new_g, nxt, idx, nidx)
                    heapq.heappush(open_list, (new_g + h, next(counter), nidx))

    # --- Trace and Visually Render Path Output ---
    if goal_idx == -1:
        print("Kinematic constraints prevented locating an applicable pathway.")
        return

    print("Target State Reached Flawlessly!")
    path = []
    t = goal_idx
    while t != -1:
        path.append(registry[t].state)
        t = registry[t].parent_idx
    path.reverse()

    display = [['▒' if grid[r][c] == 1 else '.' for c in range(MAP_W)] for r in range(MAP_H)]
    for s in path:
        xi, yi = int(s.x), int(s.y)
        if 0 <= xi < MAP_W and 0 <= yi < MAP_H:
            display[yi][xi] = '*'
    display[int(start.y)][int(start.x)] = 'S'
    display[int(goal.y)][int(goal.x)] = 'E'

    print("\n================ HYBRID A* PATH VISUALIZATION ================\n")
    for r in range(MAP_H - 1, -1, -1):  # Print top-down orientation
        print(f"{r:2d}  " + "".join(ch + " " for ch in display[r]))
    print("    " + "".join(f"{c % 10} " for c in range(MAP_W)))
    print("\n==============================================================")


# main code harness:
if __name__ == "__main__":
    # 20x20 grid with an obstacle wall dividing the room midway
    grid = [[0] * MAP_W for _ in range(MAP_H)]
    for i in range(4, 16):
        grid[10][i] = 1  # horizontal wall in the middle

    # (X, Y, Heading-Theta, Initial Gear Direction)
    start = State(2.5, 2.5, 0.0, 0)               # Bottom-Left, Facing Right
    goal = State(17.5, 17.5, math.pi / 2.0, 0)    # Top-Right, Facing Straight Up
    hybrid_a_star(grid, start, goal)
