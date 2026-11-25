"""
Given a graph, find whether there exists a cycle or not.

Input: Directed graph
Output: bool

Solution:
    We can use DFS for this. We associate three states using 3 colors: white, grey and black.
    White: initial state
    Grey: Visited once and being processed
    Black: Processed once

    We start with white color, then for each node being visited for the first time we make
    it grey and recurse further. Once the call returns back to a node, we make the color for
    that node black, indicating it has finished processing. While doing DFS if we encounter
    a node which is grey, then we have a loop.

TC: O(V + E)
SC: O(V)
"""
from enum import Enum


class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


class Vertex:
    def __init__(self, data):
        self.color = Color.WHITE  # default state white
        self.data = data
        self.edges = []


# creates a graph with given no. of vertices with serial data values and no edges
def create_graph(n):
    return [Vertex(i) for i in range(n)]


# for adding an edge from 'u' to 'v'
def add_edge(u, v):
    u.edges.append(v)


def print_graph(g):
    print("GRAPH:")
    for u in g:
        print(f"{u.data}: " + " ".join(str(v.data) for v in u.edges))
    print()


# using DFS we check if any node reaches back to a node on the current recursion stack
def is_cycle_present(curr, prev):
    # if the color is grey, the current node is already in the recursion stack
    # and because of the cycle that node has been reached again
    if curr.color == Color.GREY:
        return True
    # else if it is the first time, make it grey
    curr.color = Color.GREY
    # do DFS for its adjacent nodes
    for nxt in curr.edges:
        if nxt is not prev and nxt.color != Color.BLACK and is_cycle_present(nxt, curr):
            return True
    # processing done, change the state to black
    curr.color = Color.BLACK
    return False


# checks if deadlock is present or not. Basically we check for existence of a cycle.
def is_deadlock_present(g):
    for curr in g:
        if curr.color == Color.WHITE and is_cycle_present(curr, None):
            return True
    return False


# main code harness:
if __name__ == "__main__":
    g = create_graph(5)
    add_edge(g[0], g[1])
    add_edge(g[1], g[2])
    add_edge(g[2], g[0])
    add_edge(g[2], g[3])
    add_edge(g[3], g[4])
    print_graph(g)
    print("Deadlock present:", int(is_deadlock_present(g)))
