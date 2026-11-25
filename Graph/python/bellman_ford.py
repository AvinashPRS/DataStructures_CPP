"""
Bellman-Ford algorithm.

Time Complexity: O(V * E) because it processes all edges V-1 times.
Space Complexity: O(V) to store the array tracking shortest distances.

Bellman-Ford is a single-source shortest path algorithm that can handle graphs with
negative edge weights, unlike Dijkstra's algorithm. It also detects negative weight cycles.
"""
from dataclasses import dataclass

INF = float("inf")


@dataclass
class Edge:
    src: int
    dest: int
    weight: int


def bellman_ford(V, edges, src):
    """Returns shortest distances from src, or an empty list if a negative-weight cycle exists."""
    # Initialize distances from src to all other vertices as infinite
    dist = [INF] * V
    dist[src] = 0

    # Step 1: Relax all edges |V| - 1 times.
    # A shortest path from src to any other vertex can have at most |V| - 1 edges.
    for _ in range(V - 1):
        for e in edges:
            # If the source vertex has a valid distance, relax the edge
            if dist[e.src] != INF and dist[e.src] + e.weight < dist[e.dest]:
                dist[e.dest] = dist[e.src] + e.weight

    # Step 2: Check for negative-weight cycles.
    # If we can still relax an edge, then a negative cycle exists.
    for e in edges:
        if dist[e.src] != INF and dist[e.src] + e.weight < dist[e.dest]:
            return []  # Negative cycle detected!
    return dist


# main code harness:
if __name__ == "__main__":
    V = 5
    edges = [Edge(*t) for t in [
        (0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2),
        (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3),
    ]]
    source = 0
    distances = bellman_ford(V, edges, source)
    if not distances:
        print("Graph contains a negative-weight cycle! Shortest paths cannot be determined.")
    else:
        print(f"Vertex Distance from Source {source}:")
        for i in range(V):
            print(f"{i} \t\t {-1 if distances[i] == INF else distances[i]}")
