class Solution:
    def _has_cycle(self, node, graph, state):
        # If state is 1, we hit a node currently in our DFS path -> Cycle detected!
        if state[node] == 1:
            return True
        # If state is 2, it has already been processed and confirmed safe
        if state[node] == 2:
            return False

        # Mark node as "Visiting"
        state[node] = 1

        # Check all outgoing edges
        for neighbor in graph[node]:
            if self._has_cycle(neighbor, graph, state):
                return True  # If any neighbor leads to a cycle, this node is unsafe

        # Mark node as "Safe"
        state[node] = 2
        return False

    def eventual_safe_nodes(self, graph):
        n = len(graph)
        state = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe
        safe_nodes = []
        for i in range(n):
            # If the node does not lead to a cycle, it is safe
            if not self._has_cycle(i, graph, state):
                safe_nodes.append(i)
        return safe_nodes


# main code harness:
if __name__ == "__main__":
    solver = Solution()
    # graph[i] is a list of nodes adjacent to i
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    result = solver.eventual_safe_nodes(graph)
    print("Eventual Safe Nodes:", result)  # Expected Output: [2, 4, 5, 6]
