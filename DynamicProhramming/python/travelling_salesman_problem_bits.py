"""Travelling Salesman Problem: top-down DP with bitmasking, with tour reconstruction."""

# Use a sufficiently large value representing infinity for unreachable paths
INF = 1e9


class TSPSolver:
    def __init__(self, matrix):
        self.distance_matrix = matrix
        self.num_cities = len(matrix)
        # memo[mask][pos] stores the minimum cost to visit the remaining unvisited
        # cities represented by 'mask', starting from city 'pos'
        self.memo = [[-1.0] * self.num_cities for _ in range(1 << self.num_cities)]
        # parent[mask][pos] stores the next city to visit, to reconstruct the optimal tour
        self.parent = [[-1] * self.num_cities for _ in range(1 << self.num_cities)]

    def solve_tsp(self, mask, pos):
        """Recursive DP function with bitmasking"""
        # Base Case: all cities visited; return distance back to the starting city (0)
        if mask == (1 << self.num_cities) - 1:
            return self.distance_matrix[pos][0]

        # Return the result immediately if it has already been computed
        if self.memo[mask][pos] != -1.0:
            return self.memo[mask][pos]

        min_cost = INF
        best_next_city = -1

        # Try to visit all next unvisited cities
        for next_city in range(self.num_cities):
            if (mask & (1 << next_city)) == 0:
                current_cost = (self.distance_matrix[pos][next_city] +
                                self.solve_tsp(mask | (1 << next_city), next_city))
                if current_cost < min_cost:
                    min_cost = current_cost
                    best_next_city = next_city

        self.parent[mask][pos] = best_next_city
        self.memo[mask][pos] = min_cost
        return min_cost

    def compute_and_print_tour(self):
        # Start at city 0, with only city 0 marked as visited (mask = 1)
        total_distance = self.solve_tsp(1, 0)
        print(f"Minimum Distance: {total_distance:.2f}")

        # Reconstruct and print the optimal path sequence
        mask = 1
        curr_city = 0
        path = [str(curr_city)]
        while True:
            next_city = self.parent[mask][curr_city]
            if next_city == -1:
                break
            path.append(str(next_city))
            mask |= (1 << next_city)
            curr_city = next_city
        print("Optimal Tour Path: " + " -> ".join(path) + " -> 0")  # Return to start


if __name__ == "__main__":
    # Example 4x4 Distance Matrix (Symmetric TSP); rows/cols are cities 0..3
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    solver = TSPSolver(graph)
    solver.compute_and_print_tour()
