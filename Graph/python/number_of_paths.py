"""
Algorithm to count paths between two nodes in a directed graph using DFS.

Uses Depth First Search to count the number of possible (simple) paths between two nodes in a
directed graph represented by an adjacency matrix. Recursively traverses the graph to find all
paths from the source node `u` to the destination node `v`.

Author: Aditya Borate (https://github.com/adi776borate)
See: https://en.wikipedia.org/wiki/Path_(graph_theory)
"""


def count_paths_dfs(A, u, v, n, visited):
    """Helper: DFS counting the number of paths from u to v."""
    if u == v:
        return 1  # Base case: Reached the destination node

    visited[u] = True  # Mark the current node as visited
    path_count = 0
    for i in range(n):
        if A[u][i] == 1 and not visited[i]:  # edge exists and the node is not visited
            path_count += count_paths_dfs(A, i, v, n, visited)

    visited[u] = False  # Unmark the current node (backtracking) - important step
    return path_count


def count_paths(A, u, v, n):
    """Counts the number of paths from node u to node v in a directed graph using DFS."""
    # Check for invalid nodes or empty graph
    if u >= n or v >= n or not A or not A[0]:
        return 0
    visited = [False] * n
    return count_paths_dfs(A, u, v, n, visited)


def test():
    # Test case 1: Simple directed graph with multiple paths
    g1 = [[0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    assert count_paths(g1, 0, 4, 5) == 3

    # Test case 2: No possible path (disconnected graph)
    g2 = [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    assert count_paths(g2, 0, 4, 5) == 0

    # Test case 3: Cyclic graph with multiple paths
    g3 = [[0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [1, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0]]
    assert count_paths(g3, 0, 4, 5) == 3

    # Test case 4: Single node graph -> 1 path from node 0 to 0
    assert count_paths([[0]], 0, 0, 1) == 1

    # Test case 5: Empty graph
    assert count_paths([[]], 0, 0, 0) == 0

    # Test case 6: Invalid nodes (out of bounds)
    assert count_paths([[0, 1, 0], [0, 0, 1], [0, 0, 0]], 0, 5, 3) == 0

    print("All tests have successfully passed!")


# ---------------------------------------------------------------------------
# Alternative versions (were commented out in the C++ file)
# ---------------------------------------------------------------------------

class GraphDAG:
    """DAG version: no visited array needed because there are no cycles."""

    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def count_paths(self, src, dst):
        if src == dst:
            return 1  # Reached destination: one valid path found
        return sum(self.count_paths(nb, dst) for nb in self.adj[src])


class GraphCyclic:
    """If the graph may contain cycles, count simple paths using a visited array for the
    current DFS path (with backtracking)."""

    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def _dfs(self, src, dst, visited):
        if src == dst:
            return 1
        visited[src] = True
        count = 0
        for nb in self.adj[src]:
            if not visited[nb]:
                count += self._dfs(nb, dst, visited)
        # Backtracking - we only want to prevent a node from appearing twice in the same path.
        # Once we finish exploring one path, the node becomes available for another path.
        visited[src] = False
        return count

    def count_paths(self, src, dst):
        return self._dfs(src, dst, [False] * self.V)


# main code harness:
if __name__ == "__main__":
    test()  # Run self-test implementations

    for cls in (GraphDAG, GraphCyclic):
        g = cls(5)
        for u, v in [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (1, 4), (3, 4)]:
            g.add_edge(u, v)
        print(f"{cls.__name__}: Number of paths from 0 to 4 = {g.count_paths(0, 4)}")

    # Directed graph including a cycle: 0 -> 1 -> 2 -> 0
    g = GraphCyclic(5)
    for u, v in [(0, 1), (1, 2), (1, 3), (2, 0), (2, 4), (3, 2), (3, 4)]:
        g.add_edge(u, v)
    print("Number of paths from 0 to 4 (cyclic graph):", g.count_paths(0, 4))
