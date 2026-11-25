"""
Find if Path Exists in Graph (BFS).

Time Complexity: O(V + E). Space Complexity: O(V + E).
"""
from collections import deque


class Solution:
    def valid_path(self, n, edges, source, destination):
        # Optimization: If source and destination are the same, path trivially exists
        if source == destination:
            return True

        # 1. Build the bidirectional adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 2. Setup BFS structures
        q = deque([source])
        visited = [False] * n
        visited[source] = True

        # 3. Process traversal level-by-level
        while q:
            curr = q.popleft()
            if curr == destination:
                return True
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
        return False


# main code harness:
if __name__ == "__main__":
    solver = Solution()
    # Graph: 0-1, 1-2, 2-0. Source = 0, Destination = 2
    print(f"Test Case 1 (Valid): {solver.valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2)} (Expected: True)")
    # Graph: 0-1, 0-2, 3-5, 5-4. Source = 0, Destination = 5
    print(f"Test Case 2 (Invalid): {solver.valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4]], 0, 5)} (Expected: False)")
