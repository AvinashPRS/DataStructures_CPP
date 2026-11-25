"""
General graph toolkit: weighted directed graph, DFS, BFS, Union-Find, and topological sorting
(DFS-based and Kahn's BFS-based).  (The C++ original used std::unique_ptr for node ownership;
in Python ordinary references and garbage collection cover that.)
"""
from collections import deque


class WeightedEdge:
    """Weighted Edge of graph."""

    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Vertex:
    """Graph node."""

    def __init__(self, data):
        self.data = data
        self.edges = []


def create_node(data):
    return Vertex(data)


def add_edge(g, src, dst, weight=1):
    """Adds a directed edge between two vertices."""
    g[src].edges.append(WeightedEdge(src, dst, weight))


def _dfs_helper(g, curr, visited, out):
    visited.add(curr)
    out.append(curr.data)
    for e in curr.edges:  # Traverse adjacent edges
        nb = g[e.end]
        if nb not in visited:
            _dfs_helper(g, nb, visited, out)


def dfs(g):
    """Driver for DFS of graph. TC: O(V + E)"""
    visited, out = set(), []
    for v in g:
        if v not in visited:
            _dfs_helper(g, v, visited, out)
    print(" ".join(map(str, out)) + " ")
    return out


def bfs(g):
    """BFS of graph. TC: O(V + E)"""
    visited, out = set(), []
    for v in g:
        if v in visited:
            continue
        q = deque([v])
        visited.add(v)  # Mark visited IMMEDIATELY when pushed to avoid infinite loop
        while q:
            curr = q.popleft()
            out.append(curr.data)
            for e in curr.edges:
                nb = g[e.end]
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)
    print(" ".join(map(str, out)) + " ")
    return out


def print_graph(g):
    for v in g:
        print(f"{v.data}: " + "".join(f"{g[e.end].data}({e.weight}) " for e in v.edges))


def create_graph(n_vertices):
    return [create_node(i) for i in range(n_vertices)]


# ----------------------------------- UNION-FIND -----------------------------------

class UnionFind:
    def __init__(self, n_nodes):
        self.root = list(range(n_nodes))
        self.size = [1] * n_nodes

    def get_root(self, idx):
        """Finds the root of component with path compression."""
        if idx == self.root[idx]:
            return idx
        self.root[idx] = self.get_root(self.root[idx])
        return self.root[idx]

    def union(self, a, b):
        """Union operation using size-based weight consideration."""
        ra, rb = self.get_root(a), self.get_root(b)
        if ra == rb:
            return  # elements are already in the same component
        if self.size[rb] < self.size[ra]:
            self.root[rb] = ra
            self.size[ra] += self.size[rb]
        else:
            self.root[ra] = rb
            self.size[rb] += self.size[ra]

    def find(self, a, b):
        return self.get_root(a) == self.get_root(b)

    def connected_components(self):
        result = sorted(self.size[i] for i in range(len(self.root)) if self.root[i] == i)
        print(" ".join(map(str, result)) + " ")
        return result


# ------------------------------- TOPOLOGICAL SORTING -------------------------------

def _topo_sort_dfs_helper(src, g, order, visited):
    """DFS that detects cycles instead of overflowing the stack. Returns True on cycle."""
    visited[src] = 1  # 1 = Visiting (in recursion stack)
    for e in g[src].edges:
        if visited[e.end] == 1:
            return True  # Cycle detected!
        if visited[e.end] == 0 and _topo_sort_dfs_helper(e.end, g, order, visited):
            return True
    visited[src] = 2  # 2 = Fully processed
    order.appendleft(src)  # Pushing to front automatically sorts correctly
    return False


def all_topological_sort_orders(g):
    """For every root index, the topological order of nodes reachable from it (if acyclic)."""
    n = len(g)
    all_orders = []
    for i in range(n):
        order = deque()
        visited = [0] * n
        if not _topo_sort_dfs_helper(i, g, order, visited):
            all_orders.append(list(order))
    return all_orders


def _topological_dfs(curr, g, order, rec_stack, visited):
    if visited[curr]:
        return False
    visited[curr] = True
    rec_stack[curr] = True
    for e in g[curr].edges:
        if rec_stack[e.end]:
            return True  # Cycle
        if _topological_dfs(e.end, g, order, rec_stack, visited):
            return True
    rec_stack[curr] = False
    order.append(curr)
    return False


def topological_dfs(g):
    """DFS tracking approach. Returns [] if a cycle exists."""
    n = len(g)
    visited, rec_stack, order = [False] * n, [False] * n, []
    for i in range(n):
        if not visited[i] and _topological_dfs(i, g, order, rec_stack, visited):
            return []  # Empty list indicates cycle error
    return order[::-1]  # DFS topology needs reversal at end


def topological_bfs(g):
    """Kahn's Algorithm (BFS-based Topological Sort). Returns [] if a cycle exists."""
    indegree = [0] * len(g)
    for v in g:
        for e in v.edges:
            indegree[e.end] += 1
    q = deque(i for i in range(len(g)) if indegree[i] == 0)  # nodes with 0 in-degree
    order = []
    while q:
        curr = q.popleft()
        order.append(curr)
        for e in g[curr].edges:
            indegree[e.end] -= 1
            if indegree[e.end] == 0:
                q.append(e.end)
    # If order size doesn't equal node count, a cycle exists!
    # Note: DO NOT reverse; Kahn's naturally returns the proper dependency order.
    return order if len(order) == len(g) else []


# main code harness:
if __name__ == "__main__":
    graph = create_graph(6)
    # Directed Acyclic Graph (DAG) for testing Topological algorithms
    for s, d in [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]:
        add_edge(graph, s, d)

    print("--- Graph Layout Structure ---")
    print_graph(graph)
    print("\n--- DFS Traversal Output ---")
    dfs(graph)
    print("\n--- BFS Traversal Output ---")
    bfs(graph)
    print("\n--- Topological Sorting (Kahn's BFS Method) ---")
    print(" ".join(map(str, topological_bfs(graph))) + " ")
    print("\n--- Topological Sorting (DFS Method) ---")
    print(" ".join(map(str, topological_dfs(graph))) + " ")

    print("\n--- Union-Find Validation Example ---")
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    print("Is 0 connected to 2?", "Yes" if uf.find(0, 2) else "No")
    print("Is 0 connected to 3?", "Yes" if uf.find(0, 3) else "No")
    print("Component sizes list: ", end="")
    uf.connected_components()
