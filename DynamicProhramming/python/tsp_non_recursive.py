"""Traveling Salesman Problem: bottom-up (tabulation) DP with bitmasking."""

# Large value to represent infinity for unreachable paths
INF = 10 ** 9


def main():
    dist = [[0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]]

    n = len(dist)
    num_states = 1 << n  # 2^n states

    # dp[mask][u] stores the min cost to visit remaining unvisited cities, given that
    # 'mask' represents the cities ALREADY visited and we are currently at city 'u'
    dp = [[INF] * n for _ in range(num_states)]

    # Parent table for tracking the path taken to reconstruct the tour
    parent = [[-1] * n for _ in range(num_states)]

    # Base Case: when all cities are visited, the only remaining cost is traveling
    # back from the current city 'u' to the start (city 0)
    all_visited_mask = num_states - 1
    for u in range(n):
        dp[all_visited_mask][u] = dist[u][0]

    # Bottom-up tabulation: iterate from largest masks down to the smallest masks.
    # Skip the all-visited mask since it's already filled.
    for mask in range(all_visited_mask - 1, 0, -1):
        for curr_city in range(n):
            # If the current city is not marked as visited in this mask, the state is invalid
            if not (mask & (1 << curr_city)):
                continue

            # Try traveling to any next city that hasn't been visited yet
            for next_city in range(n):
                if not (mask & (1 << next_city)):
                    next_mask = mask | (1 << next_city)
                    new_cost = dist[curr_city][next_city] + dp[next_mask][next_city]

                    if new_cost < dp[mask][curr_city]:
                        dp[mask][curr_city] = new_cost
                        parent[mask][curr_city] = next_city  # Track the best decision

    # The starting state: only city 0 is visited (mask = 1) and we are at city 0
    min_total_cost = dp[1][0]
    print(f"The minimum possible travel cost is: {min_total_cost}")

    # --- Path Reconstruction ---
    curr_mask = 1
    curr_city = 0
    path = [str(curr_city)]
    while curr_mask != all_visited_mask:
        next_city = parent[curr_mask][curr_city]
        path.append(str(next_city))
        curr_mask |= (1 << next_city)
        curr_city = next_city
    print("Optimal Path: " + " -> ".join(path) + " -> 0")  # Complete the cycle


if __name__ == "__main__":
    main()
