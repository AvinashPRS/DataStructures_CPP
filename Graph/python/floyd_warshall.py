"""
Floyd-Warshall algorithm.

A dynamic programming technique to find the shortest paths between all pairs of vertices in a
weighted graph. Handles positive and negative edge weights, but not negative cycles.

Initialize the distance matrix with given edge weights; distance from each vertex to itself is 0.
For each vertex k (as intermediate) and each pair (i, j):
  - if k is not on the shortest path from i to j, keep dist[i][j];
  - otherwise update dist[i][j] = dist[i][k] + dist[k][j] if that is smaller.
When we pick k, vertices {0, 1, ..., k-1} have already been considered as intermediates.

https://www.geeksforgeeks.org/cpp/floyd-warshall-algorithm-cpp/
"""

INF = float("inf")


def print_solution(dist):
    print("The following matrix shows the shortest distances between every pair of vertices:")
    for row in dist:
        print("".join(("INF" if d == INF else str(d)) + "\t" for d in row))


def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]
    for k in range(V):          # Intermediate vertex
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print_solution(dist)
    return dist


# Alternative interactive version (from TheAlgorithms, kept commented-out in the C++ file):
#   https://github.com/TheAlgorithms/C-Plus-Plus/blob/master/dynamic_programming/floyd_warshall.cpp
def floyd_warshall_interactive():
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    graph = [[0 if i == j else INF for j in range(V)] for i in range(V)]
    for i in range(E):
        print(f"\nEdge {i + 1}")
        src = int(input("Enter source: "))
        dst = int(input("Enter destination: "))
        graph[src][dst] = int(input("Enter weight: "))
    floyd_warshall(graph)


# main code harness:
if __name__ == "__main__":
    #        10
    #   (0)------->(3)
    #    |         /|\
    #  5 |          |
    #    |          | 1
    #   \|/         |
    #   (1)------->(2)
    #        3
    graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
    floyd_warshall(graph)
