"""
Depth First Search Algorithm using Stack (https://en.wikipedia.org/wiki/Depth-first_search)

Authors: Ayaan Khan (http://github.com/ayaankhan98), Saurav Uppoor (https://github.com/sauravUppoor)

DFS is a Graph Traversal Algorithm. Time Complexity O(|V| + |E|).

Working
1. Mark all vertices as unvisited (colour it WHITE).
2. Push starting vertex into the stack and colour it GREY.
3. Once a node is popped out of the stack and is coloured GREY, we colour it BLACK.
4. Push all its neighbours which are not coloured BLACK.
5. Repeat steps 4 and 5 until the stack is empty.
"""

WHITE = 0  # node hasn't been explored
GREY = 1   # node is in stack waiting to be explored
BLACK = 2  # node has already been explored


def add_edge(adj, u, v):
    """Adds a directed edge u -> v (1-indexed input)."""
    adj[u - 1].append(v - 1)


def dfs(graph, start):
    """Returns the nodes (1-indexed) in the order of DFS traversal."""
    checked = [WHITE] * len(graph)  # status of each node
    traversed_path = []
    checked[start] = GREY
    stack = [start]

    # while stack is not empty we keep exploring the node on top of stack
    while stack:
        act = stack.pop()
        if checked[act] == GREY:
            traversed_path.append(act + 1)
            # exploring the neighbours of the current node
            for it in graph[act]:
                stack.append(it)
                if checked[it] != BLACK:
                    checked[it] = GREY
            checked[act] = BLACK  # Node has been explored
    return traversed_path


def tests():
    print("Case 1: ")
    g1 = [[] for _ in range(3)]
    add_edge(g1, 1, 2); add_edge(g1, 2, 3); add_edge(g1, 3, 1)
    assert dfs(g1, 0) == [1, 2, 3]
    print("Passed")

    print("Case 2: ")
    g2 = [[] for _ in range(4)]
    add_edge(g2, 1, 2); add_edge(g2, 1, 3); add_edge(g2, 2, 4); add_edge(g2, 4, 1)
    assert dfs(g2, 0) == [1, 3, 2, 4]
    print("Passed")

    print("Case 3: ")
    g3 = [[] for _ in range(4)]
    add_edge(g3, 1, 2); add_edge(g3, 1, 3); add_edge(g3, 2, 4); add_edge(g3, 4, 1)
    assert dfs(g3, 1) == [2, 4, 1, 3]
    print("Passed")


if __name__ == "__main__":
    tests()  # execute the tests

    vertices = int(input("Enter the Vertices : "))
    edges = int(input("Enter the Edges : "))
    adj = [[] for _ in range(vertices)]
    print("Enter the vertices which have edges between them : ")
    for _ in range(edges):
        u, v = map(int, input().split())
        add_edge(adj, u, v)
    print("Enter the starting vertex [1,n]: ")
    start_pos = int(input()) - 1
    print(" ".join(map(str, dfs(adj, start_pos))))
