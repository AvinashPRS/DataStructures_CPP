"""
compound_graph: GraphNode and GraphEdge combined in one module
(the C++ file concatenated both headers into a single translation unit).
"""
from graph_edge import GraphEdge  # noqa: F401
from graph_node import GraphNode  # noqa: F401

__all__ = ["GraphNode", "GraphEdge"]
