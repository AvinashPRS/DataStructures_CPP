INF = float("inf")


# Wrapper class for storing an edge
class Edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight


# Wrapper class for storing a graph
class Graph:
    # Constructs a graph with V vertices and E edges
    def __init__(self, V, E):
        self.vertex_num = V
        self.edge_num = E
        self.edges = []

    # Adds the given edge to the graph
    def add_edge(self, src, dst, weight):
        if len(self.edges) < self.edge_num:
            self.edges.append(Edge(src, dst, weight))


# Utility function to print distances
def print_dist(dist, V):
    print("\nVertex  Distance")
    for i in range(V):
        print(f"{i}\t{dist[i]}" if dist[i] != INF else f"{i}\tINF")


# Finds the shortest path from given source to all other vertices using Bellman-Ford.
# It also detects negative weight cycle.
def bellman_ford(graph, src):
    V = graph.vertex_num
    # Initialize distances array as INF for all except source
    dist = [INF] * V
    dist[src] = 0

    # Calculate shortest path distance from source to all edges
    # A path can contain maximum (|V|-1) edges
    for _ in range(V - 1):
        for e in graph.edges:
            if dist[e.src] != INF and dist[e.src] + e.weight < dist[e.dst]:
                dist[e.dst] = dist[e.src] + e.weight

    # Iterate inner loop once more to check for negative cycle
    for e in graph.edges:
        if dist[e.src] != INF and dist[e.src] + e.weight < dist[e.dst]:
            print("Graph contains negative weight cycle. Hence, shortest distance not guaranteed.")
            return

    print_dist(dist, V)


# Driver Function
if __name__ == "__main__":
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    G = Graph(V, E)
    for i in range(E):
        print(f"\nEdge {i + 1}")
        src = int(input("Enter source: "))
        dst = int(input("Enter destination: "))
        weight = int(input("Enter weight: "))
        G.add_edge(src, dst, weight)
    gsrc = int(input("\nEnter source: "))
    bellman_ford(G, gsrc)
