"""GraphNode: a vertex that holds the list of edges it is connected with."""


class GraphNode:
    def __init__(self, node_index):
        # Each GraphNode holds a list of edges that it is connected with.
        self._edges = []
        # node index that recognizes the node.
        self._node_index = node_index

    def get_edges(self):
        return self._edges

    def set_edges(self, edges):
        self._edges = list(edges)

    def get_node_index(self):
        return self._node_index

    # Graph.cpp in this folder calls getIndex(); provide both names.
    get_index = get_node_index

    def __repr__(self):
        return f"GraphNode({self._node_index})"
