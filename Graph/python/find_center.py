"""
Find Center of Star Graph (LeetCode 1791)

O(1) Time Complexity: Instead of constructing an adjacency list or calculating the degree
of all V vertices (which takes O(V) time), this trick solves the entire problem by
examining just 4 integer values.
O(1) Space Complexity: No extra memory is allocated.

A star graph consists of 1 central node connected to exactly n - 1 outer nodes.
Because the center node is connected to every single other node, it must appear
in every single edge of the graph. Therefore, you only need to compare the first
two edges to see which node is repeated.
"""


class Solution:
    def find_center(self, edges):
        # A star graph's center must appear in every single edge.
        # Therefore, we only need to look at the first two edges.
        u1, v1 = edges[0]
        u2, v2 = edges[1]

        # Find which node from the first edge is repeated in the second edge
        if u1 == u2 or u1 == v2:
            return u1
        return v1


# main code harness:
if __name__ == "__main__":
    solver = Solution()

    # --- TEST CASE 1 --- Center is 2. Edges: 1-2, 2-3, 4-2
    edges1 = [[1, 2], [2, 3], [4, 2]]
    print(f"Test Case 1 Center: {solver.find_center(edges1)} (Expected: 2)")

    # --- TEST CASE 2 --- Center is 1. Edges: 1-2, 5-1, 1-3, 1-4
    edges2 = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print(f"Test Case 2 Center: {solver.find_center(edges2)} (Expected: 1)")
