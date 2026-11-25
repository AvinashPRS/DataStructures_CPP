"""GraphEdge: weighted edge between two GraphNodes (Node1 = output node, Node2 = input node)."""


class GraphEdge:
    def __init__(self, weight, node1, node2):
        self._weight = weight  # weight of the edge.
        self._node1 = node1    # Node 1 is the output node.
        self._node2 = node2    # Node 2 is the input node.

    # Simple getter methods for variables.
    def get_weight(self):
        return self._weight

    def get_node1(self):
        return self._node1

    def get_node2(self):
        return self._node2

    def same_endpoints(self, edge):
        """Two edges are 'equal' if they join the same pair of nodes, in either order
        (mirrors the C++ operator==(GraphEdge*))."""
        return ((edge._node1 is self._node1 and edge._node2 is self._node2) or
                (edge._node1 is self._node2 and edge._node2 is self._node1))

    def __repr__(self):
        return f"GraphEdge({self._node1.get_node_index()}->{self._node2.get_node_index()}, w={self._weight})"
