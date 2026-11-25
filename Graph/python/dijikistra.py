import heapq

INF = float("inf")


class Graph:
    def __init__(self, V):
        self.V = V  # Number of vertices
        self.adj = [[] for _ in range(V)]  # adj[u] stores tuples of (weight, v)

    # Function to add an undirected edge to the graph
    def add_edge(self, u, v, w):
        self.adj[u].append((w, v))  # Store (weight, neighbor)
        self.adj[v].append((w, u))  # Comment out this line if the graph is directed

    # Dijkstra's algorithm logic
    def dijkstra(self, src):
        # Step 1: Min-heap of (distance, vertex)
        pq = []
        # Step 2: Initialize distance array with infinity
        dist = [INF] * self.V
        # Step 3: Insert source vertex into priority queue and set its distance to 0
        heapq.heappush(pq, (0, src))
        dist[src] = 0

        # Step 4: Process the queue until it's empty
        while pq:
            current_d, u = heapq.heappop(pq)  # vertex with min distance

            # Skip processing if we already found a shorter path to u
            if current_d > dist[u]:
                continue

            # Traverse all adjacent neighbors of u
            for weight, v in self.adj[u]:
                # Step 5: Edge Relaxation
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        self._print_solution(src, dist)

    def _print_solution(self, src, dist):
        print(f"Shortest distances from source node {src}:")
        print("Vertex\tDistance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{'INF' if dist[i] == INF else dist[i]}")


# main code harness:
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 9)
    g.add_edge(0, 2, 6)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 3, 1)
    g.add_edge(3, 4, 7)
    g.dijkstra(0)
