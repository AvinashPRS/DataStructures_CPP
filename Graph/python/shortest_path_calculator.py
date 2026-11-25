"""Design Graph With Shortest Path Calculator (LeetCode 2642)."""
import heapq

INF = float("inf")


class Graph:
    # Initializes the object with n nodes and the given (directed) edges
    def __init__(self, n, edges):
        self.num_nodes = n
        self.adj_list = [[] for _ in range(n)]  # (neighbor, cost)
        for frm, to, cost in edges:
            self.adj_list[frm].append((to, cost))

    # Adds a directed edge to the graph
    def add_edge(self, edge):
        frm, to, cost = edge
        self.adj_list[frm].append((to, cost))

    # Finds the minimum path cost between node1 and node2 using Dijkstra's Algorithm
    def shortest_path(self, node1, node2):
        dist = [INF] * self.num_nodes
        dist[node1] = 0
        pq = [(0, node1)]  # min-heap of (accumulated_cost, node)

        while pq:
            current_cost, u = heapq.heappop(pq)
            # Optimization: If we reached our target destination, return immediately
            if u == node2:
                return current_cost
            # Skip if a cheaper path to u has already been explored
            if current_cost > dist[u]:
                continue
            for v, w in self.adj_list[u]:
                if current_cost + w < dist[v]:
                    dist[v] = current_cost + w
                    heapq.heappush(pq, (dist[v], v))

        # -1 if node2 is unreachable from node1
        return -1 if dist[node2] == INF else dist[node2]


# main code harness:
if __name__ == "__main__":
    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [2, 3, 3]])
    # Path: 0 -> 1 -> 2 -> 3 (Cost: 2 + 1 + 3 = 6)
    print(f"Shortest path (0 to 3): {g.shortest_path(0, 3)} (Expected: 6)")
    print(f"Shortest path (3 to 0): {g.shortest_path(3, 0)} (Expected: -1)")
    print("Adding direct shortcut edge from 1 to 3 with cost 1...")
    g.add_edge([1, 3, 1])
    # New Path: 0 -> 1 -> 3 (Cost: 2 + 1 = 3)
    print(f"New shortest path (0 to 3): {g.shortest_path(0, 3)} (Expected: 3)")
