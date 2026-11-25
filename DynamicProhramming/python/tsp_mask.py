"""
Traveling Salesman Problem (TSP) using Memoization (Top-Down Dynamic Programming)
with Bitmasking.

Given a list of cities and the distances between each pair, find the shortest
possible route that visits every city exactly once and returns to the origin city.
"""

# Large value to represent infinity for unreachable paths
INF = 10 ** 9


def tsp(mask, pos, n, dist, memo, parent):
    """
    mask:   bitmask representing visited cities
    pos:    current city index
    n:      total number of cities
    dist:   the 2D distance matrix
    memo:   the caching table for minimum costs
    parent: the tracking table to store the optimal next step
    Return value: minimum cost from this state
    """
    # Base Case: all cities visited, return cost to go back to starting city (0)
    if mask == (1 << n) - 1:
        return dist[pos][0]

    # Return cached result if already computed
    if memo[mask][pos] != -1:
        return memo[mask][pos]

    min_cost = INF
    best_next_city = -1

    # Try visiting all other unvisited cities
    for next_city in range(n):
        if (mask & (1 << next_city)) == 0:
            # total cost of moving to next_city and solving the rest of the tour
            new_cost = dist[pos][next_city] + tsp(mask | (1 << next_city), next_city, n, dist, memo, parent)
            if new_cost < min_cost:
                min_cost = new_cost
                best_next_city = next_city

    # Record the optimal next city for this specific state
    parent[mask][pos] = best_next_city

    # Cache and return the cost
    memo[mask][pos] = min_cost
    return min_cost


def print_path(n, parent):
    """Reconstructs and prints the exact tour from the parent table"""
    mask = 1  # Start at city 0 (binary: ...0001)
    curr_city = 0
    path = [str(curr_city)]

    # Trace the path forward until all bits are set
    while mask != (1 << n) - 1:
        next_city = parent[mask][curr_city]
        path.append(str(next_city))
        mask |= (1 << next_city)
        curr_city = next_city

    # Complete the cycle by returning to the start
    print("Optimal Path: " + " -> ".join(path) + " -> 0")


if __name__ == "__main__":
    dist = [[0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]]
    n = len(dist)

    # Tables of size (2^n) x n
    memo = [[-1] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    # Start at city 0, mask is 1 (only city 0 visited)
    total_min_cost = tsp(1, 0, n, dist, memo, parent)

    print(f"The minimum possible travel cost is: {total_min_cost}")
    print_path(n, parent)
