"""
Clone Graph.

Both solutions have identical time and space complexities:
Time Complexity: O(V + E). We visit every node and every edge exactly once.
Space Complexity: O(V) to store the mapping of original nodes to cloned nodes in the
hash map, plus the overhead of the recursion stack (DFS) or queue (BFS).
"""
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Method 1: DFS recommended:
class Solution:
    def __init__(self):
        # Hash map to store the mapping from original node to cloned node
        self.cloned_map = {}

    def clone_graph(self, node):
        if node is None:
            return None
        # If the node has already been cloned, return its clone
        if node in self.cloned_map:
            return self.cloned_map[node]
        # Create a copy of the node (without its neighbors for now)
        clone = Node(node.val)
        self.cloned_map[node] = clone
        # Recursively clone all neighbors and add them to the cloned node's neighbors list
        for neighbor in node.neighbors:
            clone.neighbors.append(self.clone_graph(neighbor))
        return clone


# Method 2: BFS, iterative - alternative approach:
class SolutionBFS:
    def clone_graph(self, node):
        if node is None:
            return None
        cloned_map = {node: Node(node.val)}  # Clone the root node and put it in the map
        q = deque([node])
        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                # If neighbor hasn't been cloned yet
                if neighbor not in cloned_map:
                    cloned_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)  # process its neighbors later
                # Connect the clone of the current node to the clone of the neighbor
                cloned_map[curr].neighbors.append(cloned_map[neighbor])
        return cloned_map[node]


def print_graph(start_node):
    if start_node is None:
        return
    q = deque([start_node])
    visited = {start_node}
    while q:
        curr = q.popleft()
        parts = []
        for nb in curr.neighbors:
            parts.append(f"{nb.val} (Addr: {hex(id(nb))})")
            if nb not in visited:
                visited.add(nb)
                q.append(nb)
        print(f"Node [{curr.val}] Address: {hex(id(curr))} -> Neighbors: [{', '.join(parts)}]")


# main code harness:
if __name__ == "__main__":
    # 1. Manually build a cyclic graph (Square shape: 1-2-3-4-1)
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    print("--- ORIGINAL GRAPH ---")
    print_graph(n1)

    # 2. Clone the graph
    cloned = Solution().clone_graph(n1)
    print("\n--- CLONED GRAPH ---")
    print_graph(cloned)

    cloned_bfs = SolutionBFS().clone_graph(n1)

    # 3. Verify that the objects are strictly different deep copies
    print("\n--- VERIFICATION ---")
    if n1 is not cloned and n1.val == cloned.val and cloned_bfs is not n1:
        print("SUCCESS: The graph values are identical, but the objects are fully independent!")
    else:
        print("FAILURE: Graph was not deep copied correctly.")
