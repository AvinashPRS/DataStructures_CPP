"""
Given a weighted graph that can be either cyclic/acyclic and directed/undirected.
Given a starting and target node, find the min cost path with min number of edges.

Input : Graph g
Output: min cost

Solution:
    We can use Dijkstra's shortest path algorithm with some modifications.
    For comparing the cost we include the no. of edges as a tie-breaker:
    the priority is the tuple (distance, num_edges).

NOTE: the original C++ file did not compile and had an empty main(); this Python
version implements the intended algorithm and adds a small demo.
"""
import heapq

INF = float("inf")


class Vertex:
    def __init__(self, vid):
        self.id = vid
        self.dist = INF
        self.min_edges = 0
        self.pred = None
        self.edges = []  # list of (Vertex, weight)


def dijkstra_shortest_path(src, target):
    # make the distance of src 0
    src.dist, src.min_edges = 0, 0
    # min-heap ordered by (distance, num_edges); we push lazily instead of
    # filling it initially with all nodes
    pq = [(0, 0, src.id, src)]

    while pq:
        d, e, _, u = heapq.heappop(pq)
        if (d, e) != (u.dist, u.min_edges):
            continue  # stale entry
        # if the node is the target node, then the path has been found
        if u is target:
            break
        # relax the adjacent vertex edges
        for v, w in u.edges:
            v_dist = u.dist + w
            v_num_edges = u.min_edges + 1
            if v.dist > v_dist or (v.dist == v_dist and v.min_edges > v_num_edges):
                v.pred = u
                v.dist, v.min_edges = v_dist, v_num_edges
                heapq.heappush(pq, (v_dist, v_num_edges, v.id, v))

    display_shortest_path(target)
    print()
    return target.dist, target.min_edges


def display_shortest_path(v):
    if v is not None:
        display_shortest_path(v.pred)
        print(v.id, end=" ")


if __name__ == "__main__":
    vs = [Vertex(i) for i in range(5)]

    def add(u, v, w):
        vs[u].edges.append((vs[v], w))

    # Two paths of cost 4 from 0 to 4: 0-1-2-3-4 (4 edges) and 0-4 (1 edge)
    add(0, 1, 1); add(1, 2, 1); add(2, 3, 1); add(3, 4, 1)
    add(0, 4, 4)
    print("Path: ", end="")
    cost, edges = dijkstra_shortest_path(vs[0], vs[4])
    print(f"Min cost: {cost}, edges: {edges}")  # Expected path 0 4, cost 4, edges 1
