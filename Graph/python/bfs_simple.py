from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]  # adjacency list

    # Add edge for an undirected graph
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # BFS starting from a given vertex
    def bfs(self, start):
        visited = [False] * self.V
        q = deque()

        # Mark starting vertex visited and enqueue it
        visited[start] = True
        q.append(start)

        while q:
            # Get the vertex at the front
            current = q.popleft()
            print(current, end=" ")

            # Visit all neighbors
            for neighbor in self.adj[current]:
                if not visited[neighbor]:
                    # Mark visited BEFORE putting into queue
                    visited[neighbor] = True
                    q.append(neighbor)
        print()


# main code harness:
if __name__ == "__main__":
    g = Graph(7)
    #
    #           0
    #          / \
    #         1   2
    #        / \   \
    #       3   4   5
    #                \
    #                 6
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(5, 6)

    print("BFS traversal starting from vertex 0:")
    g.bfs(0)
