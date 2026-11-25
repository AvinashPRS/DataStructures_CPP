"""
Given a directed graph, find whether a cycle (deadlock) exists.

DFS with three colours:
    white: initial state
    grey:  visited once and being processed
    black: processing finished
Reaching a grey node during DFS means there is a loop.
    TC: O(V + E)
    SC: O(V)
"""

WHITE, GREY, BLACK = 0, 1, 2


class Vertex:
    def __init__(self, data):
        self.color = WHITE
        self.data = data
        self.edges = []


def create_graph(n):
    return [Vertex(i) for i in range(n)]


def add_edge(u, v):
    u.edges.append(v)


def print_graph(g):
    print("GRAPH:")
    for u in g:
        print(f"{u.data}: " + "".join(f"{v.data} " for v in u.edges))
    print()


def is_cycle_present(curr, prev):
    # Grey means the node is already on the recursion stack
    if curr.color == GREY:
        return True
    curr.color = GREY
    for nxt in curr.edges:
        if nxt is not prev and nxt.color != BLACK and is_cycle_present(nxt, curr):
            return True
    curr.color = BLACK
    return False


def is_deadlock_present(g):
    for curr in g:
        if curr.color == WHITE and is_cycle_present(curr, None):
            return True
    return False


def main():
    g = create_graph(5)
    add_edge(g[0], g[1])
    add_edge(g[1], g[2])
    add_edge(g[2], g[0])
    add_edge(g[2], g[3])
    add_edge(g[3], g[4])
    print_graph(g)
    print(f"Deadlock present: {int(is_deadlock_present(g))}")


if __name__ == "__main__":
    main()
