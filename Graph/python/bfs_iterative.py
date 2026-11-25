from collections import deque


# BFS traversal starting from a given source node 'start_node'
def bfs_iterative(adj, start_node):
    n = len(adj)
    visited = [False] * n
    q = deque()

    # Push the starting node and mark it as visited
    q.append(start_node)
    visited[start_node] = True

    while q:
        curr = q.popleft()
        print(curr, end=" ")

        # Traverse all adjacent nodes
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True  # Mark as visited immediately when pushed
                q.append(neighbor)
    print()


# main code harness:
if __name__ == "__main__":
    # Example graph with 5 nodes (0 through 4) - undirected
    adj = [
        [1, 2],
        [0, 3, 4],
        [0, 4],
        [1],
        [1, 2],
    ]
    print("BFS starting from node 0: ", end="")
    bfs_iterative(adj, 0)
