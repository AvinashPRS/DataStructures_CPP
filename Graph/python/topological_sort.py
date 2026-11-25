"""
Topological Sort Algorithm (https://en.wikipedia.org/wiki/Topological_sorting)

Topological sorting of a directed graph is a linear ordering of its vertices such that for
every directed edge (u, v) from vertex u to vertex v, u comes before v in the ordering.

A topological sort is possible only in a directed acyclic graph (DAG).
This file finds a topological sort using a Depth First Search (reverse post-order).

NOTE: the C++ cycle check (ans.size() < n) can never fire; this version detects cycles
properly using a "visiting" state and raises ValueError("cycle detected in graph").
"""


class Graph:
    """Represents a directed graph."""

    def __init__(self, nodes):
        self.n = nodes                          # Number of nodes
        self.adj = [[] for _ in range(nodes)]   # Adjacency list representation

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def get_adjacency_list(self):
        return self.adj

    def get_num_nodes(self):
        return self.n


def _dfs(v, visited, graph, s):
    visited[v] = 1  # visiting
    for neighbour in graph[v]:
        if visited[neighbour] == 1:
            raise ValueError("cycle detected in graph")
        if not visited[neighbour]:
            _dfs(neighbour, visited, graph, s)
    visited[v] = 2  # done
    s.append(v)


def topological_sort(g):
    n = g.get_num_nodes()
    adj = g.get_adjacency_list()
    visited = [0] * n
    s = []  # stack
    for i in range(n):
        if not visited[i]:
            _dfs(i, visited, adj, s)
    return s[::-1]  # pop everything off the stack


def test():
    print("Testing for graph 1")
    g1 = Graph(6)
    for u, v in [(4, 0), (5, 0), (5, 2), (2, 3), (3, 1), (4, 1)]:
        g1.add_edge(u, v)
    ans1 = topological_sort(g1)
    print("Topological Sorting Order:", " ".join(map(str, ans1)))
    assert ans1 == [5, 4, 2, 3, 1, 0]
    print("Test Passed\n")

    print("Testing for graph 2")
    g2 = Graph(5)
    for u, v in [(0, 1), (0, 2), (1, 2), (2, 3), (1, 3), (2, 4)]:
        g2.add_edge(u, v)
    ans2 = topological_sort(g2)
    print("Topological Sorting Order:", " ".join(map(str, ans2)))
    assert ans2 == [0, 1, 2, 4, 3]
    print("Test Passed\n")

    print("Testing for graph 3")
    g3 = Graph(3)
    for u, v in [(0, 1), (1, 2), (2, 0)]:
        g3.add_edge(u, v)
    try:
        topological_sort(g3)
        assert False, "expected a cycle"
    except ValueError as err:
        assert str(err) == "cycle detected in graph"
    print("Test Passed")


# main code harness:
if __name__ == "__main__":
    test()
