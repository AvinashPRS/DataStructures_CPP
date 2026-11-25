# DFS traversal starting from a given source node 'start_node'
def dfs_iterative(adj, start_node):
    n = len(adj)
    visited = [False] * n
    s = [start_node]  # Push the starting node onto the stack

    while s:
        curr = s.pop()

        # Nodes can be pushed onto the stack multiple times,
        # so we check and process them only on their first extraction (pop)
        if not visited[curr]:
            visited[curr] = True
            print(curr, end=" ")

        # Traverse neighbors in reverse order to match the traditional recursive DFS ordering
        # (so the lower index neighbor gets processed first)
        for neighbor in reversed(adj[curr]):
            if not visited[neighbor]:
                s.append(neighbor)
    print()


# main code harness:
if __name__ == "__main__":
    adj = [
        [1, 2],
        [0, 3, 4],
        [0, 4],
        [1],
        [1, 2],
    ]
    print("Iterative DFS starting from node 0: ", end="")
    dfs_iterative(adj, 0)
