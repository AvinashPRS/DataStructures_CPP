"""
Find height of the tree using bottom-up dynamic programming.

Given a rooted tree with node 1, find the height of the tree.
Example:
    4
    1 2
    1 3
    2 4
which can be represented as
      1
     / \\
    2   3
    |
    4
Height of the tree : - 2
(note: this implementation counts nodes on the longest path, so it prints 3)
"""
import sys
from collections import defaultdict

sys.setrecursionlimit(200000)


def depth_first_search(u, adj, visited, dp):
    visited[u] = True
    child_height = 1
    for v in adj[u]:
        if not visited[v]:
            depth_first_search(v, adj, visited, dp)
            # select maximum sub-tree height from all children
            child_height = max(child_height, dp[v] + 1)
    # assign the max child height to current visited node
    dp[u] = child_height


def main():
    # number of nodes
    print("Enter number of nodes of the tree : ")
    number_of_nodes = int(input())

    # Tree contains exactly n-1 edges where n denotes the number of nodes
    print("Enter edges of the tree : ")
    edges = [tuple(map(int, input().split())) for _ in range(number_of_nodes - 1)]

    # adjacency list; u, v denotes an undirected edge of tree
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # initialize all nodes as unvisited and depth of all nodes to 0
    visited = [False] * (number_of_nodes + 1)
    dp = [0] * (number_of_nodes + 1)

    depth_first_search(1, adj, visited, dp)
    print(f"Height of the Tree : {dp[1]}")


if __name__ == "__main__":
    main()
