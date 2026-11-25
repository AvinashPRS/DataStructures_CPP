"""
Find if Path Exists in Graph (recursive DFS).

Time Complexity: O(V + E). Space Complexity: O(V + E) for the adjacency list,
plus O(V) recursion depth in the worst case (a line graph).
"""


class Solution:
    # Helper function to perform recursive DFS traversal
    def _dfs(self, curr, destination, adj, visited):
        # Base case: If we reached the destination, a path exists
        if curr == destination:
            return True
        visited[curr] = True
        # Recursively check all unvisited neighbors
        for neighbor in adj[curr]:
            if not visited[neighbor] and self._dfs(neighbor, destination, adj, visited):
                return True
        return False

    def valid_path(self, n, edges, source, destination):
        if source == destination:
            return True
        # 1. Build the bidirectional adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # 2. Track visited nodes to handle cycles
        visited = [False] * n
        # 3. Initiate the DFS traversal from the source node
        return self._dfs(source, destination, adj, visited)


# main code harness:
if __name__ == "__main__":
    solver = Solution()
    print(f"Test Case 1 (Valid): {solver.valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2)} (Expected: True)")
    print(f"Test Case 2 (Invalid): {solver.valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4]], 0, 5)} (Expected: False)")
