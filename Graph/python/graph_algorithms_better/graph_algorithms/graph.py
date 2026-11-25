"""
Graph object built from an adjacency matrix, with Prim's MST and Dijkstra's shortest path.
(The AdjacencyList representation was left un-implemented in the original.)

A typical adjacency-list construction would be:

    def create_adjacency_list(self):
        self.adjacency_list = {node: [] for node in self.vertices}  # even vertices with no edges
        for edge in self.edges:
            self.adjacency_list[edge.get_node1()].append(edge)
            # For an UNDIRECTED graph, add the edge to both vertices.
            self.adjacency_list[edge.get_node2()].append(edge)
"""
import heapq
import itertools

from graph_edge import GraphEdge
from graph_node import GraphNode

INF = 99999  # a random high value integer used as the INF value


class Graph:
    # Graph Object Constructor supporting the Adjacency matrix representation interface.
    def __init__(self, number_of_vertices, adjacency_matrix):
        self.number_of_vertices = number_of_vertices
        self.adjacency_matrix = adjacency_matrix
        self.edges = []
        self.vertices = []
        # Convert the adjacency matrix representation into our Edge representation.
        self.create_nodes()
        self.create_edges()

    def add_node(self, index):
        """Insert a GraphNode into the Graph."""
        node = GraphNode(index)
        self.vertices.append(node)
        node.set_edges([])
        return node

    def add_edge(self, node1, node2, weight):
        """Insert a GraphEdge into the Graph (and into the source node's edge list)."""
        edge = GraphEdge(weight, node1, node2)
        self.edges.append(edge)
        node1.get_edges().append(edge)
        return edge

    # ============================== Algorithms ==============================

    def prim_algorithm(self, node):
        """Prim's Algorithm to find the Minimum Spanning Tree. Returns a list of edges."""
        distance = [INF] * self.number_of_vertices
        distance[0] = 0
        counter = itertools.count()  # tie-breaker; min-heap ordered by edge weight
        pq = []
        mst = []
        for edge in node.get_edges():
            heapq.heappush(pq, (edge.get_weight(), next(counter), edge))
        while pq:
            _, _, min_edge = heapq.heappop(pq)
            dst = min_edge.get_node2().get_node_index()
            if min_edge.get_weight() < distance[dst]:
                distance[dst] = min_edge.get_weight()
                for edge in min_edge.get_node2().get_edges():
                    if not min_edge.same_endpoints(edge):
                        heapq.heappush(pq, (edge.get_weight(), next(counter), edge))
                mst.append(min_edge)
        return mst

    def dijkstra_algorithm(self, node):
        """Dijkstra Algorithm to find the shortest path from `node`; prints the path to every node."""
        src = node.get_node_index()
        distance_from_source = [INF] * self.number_of_vertices
        distance_from_source[src] = 0
        parent_vertices = [src] * self.number_of_vertices
        counter = itertools.count()
        pq = []
        for edge in node.get_edges():
            heapq.heappush(pq, (edge.get_weight(), next(counter), edge))
        while pq:
            _, _, min_edge = heapq.heappop(pq)
            n1 = min_edge.get_node1().get_node_index()
            n2 = min_edge.get_node2().get_node_index()
            s = min_edge.get_weight() + distance_from_source[n1]
            if s < distance_from_source[n2]:
                distance_from_source[n2] = s
                parent_vertices[n2] = n1
                for edge in min_edge.get_node2().get_edges():
                    if not min_edge.same_endpoints(edge):
                        heapq.heappush(pq, (edge.get_weight(), next(counter), edge))
        for j in range(self.number_of_vertices):
            print(f"Path to Node {j} is ", end="")
            self._print_parents(j, src, parent_vertices)
            print()
        return []

    def _print_parents(self, index, source_index, parent_vertices):
        """Recursive helper for Dijkstra to print the output path."""
        if index != source_index:
            self._print_parents(parent_vertices[index], source_index, parent_vertices)
            print(" -> ", end="")
        print(index, end="")

    def create_nodes(self):
        """Insert nodes using the number of vertices input."""
        for i in range(self.number_of_vertices):
            self.add_node(i)

    def create_edges(self):
        """Insert edges using the adjacency matrix input."""
        for i in range(self.number_of_vertices):
            for j in range(self.number_of_vertices):
                if self.adjacency_matrix[i][j] != 0:
                    self.add_edge(self.vertices[i], self.vertices[j], self.adjacency_matrix[i][j])

    def get_vertices(self):
        return self.vertices
