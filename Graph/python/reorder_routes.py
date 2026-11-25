"""
Reorder Routes to Make All Paths Lead to the City Zero (LeetCode 1466).

Treat the network as a tree rooted at city 0. Changing the directions of paths to make
everything flow toward city 0 is equivalent to running a traversal (DFS or BFS) from 0.
As we move outward from 0, any original edge pointing away from 0 (matching our traversal
direction) is a road that must be flipped. To traverse both directions, we build an
undirected adjacency list but tag each edge with a flag (True if the edge exists in the
original graph, False if it is a simulated reverse edge).

Time Complexity: O(V + E). Space Complexity: O(V + E).
"""
from collections import deque


class Solution:
    def min_reorder(self, n, connections):
        # Adjacency list storing: (neighbor, is_original_direction)
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append((v, True))   # Original direction u -> v
            adj[v].append((u, False))  # Virtual reverse direction v -> u

        change_count = 0
        visited = [False] * n
        q = deque([0])  # Start BFS traversal from city 0
        visited[0] = True

        while q:
            curr = q.popleft()
            for neighbor, is_original in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    # If the original edge points AWAY from 0 (curr -> neighbor), flip it.
                    if is_original:
                        change_count += 1
                    q.append(neighbor)
        return change_count


# main code harness:
if __name__ == "__main__":
    solver = Solution()
    # Connections: 0->1, 1->3, 2->3, 4->0, 4->5 -> flips 0->1, 1->3, 4->5 = 3
    c1 = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    print(f"Test Case 1 Shifts: {solver.min_reorder(6, c1)} (Expected: 3)")
    c2 = [[1, 0], [1, 2], [3, 2], [3, 4]]
    print(f"Test Case 2 Shifts: {solver.min_reorder(5, c2)} (Expected: 2)")
