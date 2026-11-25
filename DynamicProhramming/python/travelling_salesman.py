"""Travelling Salesman Problem by brute force over all permutations (vertex 0 fixed)."""
import math
from itertools import permutations


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[math.inf] * vertices for _ in range(vertices)]
        # Distance from a vertex to itself is 0
        for i in range(vertices):
            self.adj[i][i] = 0

    def add_edge(self, u, v, weight):
        """Add undirected edge"""
        self.adj[u][v] = weight
        self.adj[v][u] = weight

    def vertices(self):
        return self.V

    def get_weight(self, u, v):
        return self.adj[u][v]


def tsp(graph):
    """
    Returns (min path weight, best path). The best path defines the optimum tour,
    starting and ending at city 0.

    Fix vertex 0 as the starting point and only permute 1, 2, ..., V-1. This avoids
    generating equivalent tours that merely start at a different vertex.
    """
    V = graph.vertices()
    min_path_weight = math.inf
    best_path = []

    for perm in permutations(range(1, V)):
        current_path_weight = 0
        current = 0
        valid_path = True
        current_path = [0]

        # Visit vertices according to current permutation
        for nxt in perm:
            weight = graph.get_weight(current, nxt)
            # No edge exists
            if weight == math.inf:
                valid_path = False
                break
            current_path_weight += weight
            current_path.append(nxt)
            current = nxt

        # Return to starting vertex - returning weight also needs to be added
        if valid_path:
            return_weight = graph.get_weight(current, 0)
            if return_weight == math.inf:
                valid_path = False
            else:
                current_path_weight += return_weight
                current_path.append(0)

        # Update minimum
        if valid_path and current_path_weight < min_path_weight:
            min_path_weight = current_path_weight
            best_path = current_path

    return min_path_weight, best_path


if __name__ == "__main__":
    V = 4
    graph = Graph(V)

    #         10
    #    0 -------- 1
    #    |          |
    #  12|          |15
    #    |          |
    #    3 -------- 2
    #         20
    #
    # Valid Hamiltonian cycle: 0 -> 1 -> 2 -> 3 -> 0
    # Cost: 10 + 15 + 20 + 12 = 57
    graph.add_edge(0, 1, 10)
    graph.add_edge(1, 2, 15)
    graph.add_edge(2, 3, 20)
    graph.add_edge(3, 0, 12)

    min_path_weight, best_path = tsp(graph)

    if min_path_weight == math.inf:
        print("No Hamiltonian cycle exists.")
    else:
        print(f"Minimum path weight: {min_path_weight:g}")
        print("Path: " + " ".join(str(v) for v in best_path) + " ")
