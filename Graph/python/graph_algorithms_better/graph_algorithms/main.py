"""Interactive driver: reads adjacency matrices from stdin and runs Prim's and Dijkstra's algorithms."""
import sys

from graph import Graph

RANDOM_VERTEX = 0


def read_ints():
    for line in sys.stdin:
        for tok in line.split():
            yield int(tok)


if __name__ == "__main__":
    ints = read_ints()

    print("------------------------Prim Algorithm Test--------------------")
    print("Enter number of vertices of the graph : ", end="", flush=True)
    n = next(ints)
    print("Enter the adjacency matrix to find the MST from")
    matrix = [[next(ints) for _ in range(n)] for _ in range(n)]
    graph = Graph(n, matrix)  # Instantiate a Graph object with adjacency matrix
    mst = graph.prim_algorithm(graph.get_vertices()[RANDOM_VERTEX])
    print("------------------------Prim Algorithm Results--------------------")
    total = 0
    for item in mst:
        print(f"{item.get_node1().get_node_index()},{item.get_node2().get_node_index()},{item.get_weight()}")
        total += item.get_weight()
    print(f"Minimum spanning tree's total weight is {total}")

    print("------------------------Dijkstra Algorithm Test--------------------")
    print("Enter number of vertices of the graph : ", end="", flush=True)
    n = next(ints)
    print("Enter the adjacency matrix to find the shortest path from")
    matrix2 = [[next(ints) for _ in range(n)] for _ in range(n)]
    graph2 = Graph(n, matrix2)
    print("Enter the source vertex's index")
    src = next(ints)
    print("------------------------Dijkstra Algorithm Results--------------------")
    graph2.dijkstra_algorithm(graph2.get_vertices()[src])
