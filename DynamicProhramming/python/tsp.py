"""
Traveling Salesman Problem (TSP) using Memoization (Top-Down Dynamic Programming),
tracking visited cities with a set.

Given a list of cities and the distances between each pair, find the shortest
possible route that visits every city exactly once and returns to the origin city.

Graph model:
  Input: a complete, weighted graph G = (V, E), where V = {v1..vn} are cities,
         E are the paths between cities and d(vi, vj) is the travel cost.
  Output: a permutation of vertices (a cycle) minimizing
          sum_{i=1}^{n-1} d(v_pi(i), v_pi(i+1)) + d(v_pi(n), v_pi(1))
"""

# Large value to represent infinity for unreachable paths
INF = 10 ** 9


def tsp(visited, pos, n, dist, memo, parent):
    """
    visited: set containing the indices of all cities visited so far
    pos:     current city index the salesman is at
    n:       total number of cities
    dist:    2D distance/cost matrix between cities
    memo:    dict pairing the unique state to its minimum cost
    parent:  dict pairing the unique state to the optimal next city to visit
    Return value: minimum cost to complete the tour from this state
    """
    # Base Case: all cities visited, return the cost to go back to the starting city (0)
    if len(visited) == n:
        return dist[pos][0]

    curr_state = (frozenset(visited), pos)

    # Return cached result if this state has already been computed
    if curr_state in memo:
        return memo[curr_state]

    min_cost = INF
    best_next_city = -1

    # Try visiting all other unvisited cities from the current position
    for next_city in range(n):
        if next_city not in visited:
            # Mark the next city as visited
            visited.add(next_city)

            new_cost = dist[pos][next_city] + tsp(visited, next_city, n, dist, memo, parent)
            if new_cost < min_cost:
                min_cost = new_cost
                best_next_city = next_city

            # Backtrack: remove the city from the visited set for other recursive paths
            visited.remove(next_city)

    # Record the optimal choice for path reconstruction
    parent[curr_state] = best_next_city

    # Cache and return the optimal cost for this specific state
    memo[curr_state] = min_cost
    return min_cost


def print_path(n, parent):
    """Reconstructs and prints the path using the choices saved in the parent dict"""
    visited = {0}
    curr_city = 0
    path = [str(curr_city)]

    # Follow the recorded best choices until all cities are visited
    while len(visited) < n:
        next_city = parent[(frozenset(visited), curr_city)]
        path.append(str(next_city))
        visited.add(next_city)
        curr_city = next_city

    # Complete the loop by returning to the start
    print("Optimal Path: " + " -> ".join(path) + " -> 0")


if __name__ == "__main__":
    # Example: adjacency matrix representation of a graph with 4 cities
    dist = [[0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]]
    n = len(dist)

    # memo:   (visited_set, current_city) -> min_cost
    # parent: (visited_set, current_city) -> optimal_next_city
    memo = {}
    parent = {}

    # Start by adding the starting city (0)
    visited = {0}
    total_min_cost = tsp(visited, 0, n, dist, memo, parent)

    print(f"The minimum possible travel cost is: {total_min_cost}")
    print_path(n, parent)
