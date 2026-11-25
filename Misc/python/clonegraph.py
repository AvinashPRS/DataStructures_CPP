"""Clone an undirected graph (BFS + hash table)."""
from collections import deque


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x          # current node label
        self.neighbors = []     # neighbours of the current node


class Solution:
    def __init__(self):
        self.hashtable = {}     # original node -> cloned node
        self.visited = set()

    def cloneNode(self, node):
        if node not in self.hashtable:
            self.hashtable[node] = UndirectedGraphNode(node.label)

    def cloneGraph(self, node):
        if node is None:
            return None
        q = deque([node])
        self.visited.add(node)
        while q:
            cur = q.popleft()
            self.cloneNode(cur)
            for neighbour in cur.neighbors:
                self.cloneNode(neighbour)
                self.hashtable[cur].neighbors.append(self.hashtable[neighbour])
                if neighbour in self.visited:
                    continue
                self.visited.add(neighbour)
                q.append(neighbour)
        return self.hashtable[node]


def print_graph(node):
    """Print the graph using BFS."""
    if not node:
        return
    visited = {node}
    q = deque([node])
    while q:
        cur = q.popleft()
        line = f"Node {cur.label} -> "
        for n in cur.neighbors:
            line += f"{n.label} "
            if n not in visited:
                visited.add(n)
                q.append(n)
        print(line)


def build_triangle():
    #          1
    #        /   \
    #       2-----3
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node3 = UndirectedGraphNode(3)
    node1.neighbors += [node2, node3]
    node2.neighbors += [node1, node3]
    node3.neighbors += [node1, node2]
    return node1


def main():
    node1 = build_triangle()
    print("Original Graph")
    print_graph(node1)

    clone = Solution().cloneGraph(node1)
    print("\nCloned Graph")
    print_graph(clone)

    print("\nMemory Addresses")
    print(f"Original Node1 : {hex(id(node1))}")
    print(f"Cloned   Node1 : {hex(id(clone))}")


if __name__ == "__main__":
    main()
