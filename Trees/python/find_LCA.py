r"""
    Given two tree nodes, find the LCA.
    Solution:
        We start the traversal of the tree; when we find any of the required
        nodes, we return that node as the LCA candidate. If both nodes are in
        the same subtree, the first appearing node will be the ancestor.
        If we get candidates from both left and right subtree, then the LCA is
        the current node.
        TC: O(n)
        SC: O(h), for recursive stack

    Also included (from the notes in the C++ file):
        * lca_naive      - check every node with has_node(): O(n^2)
        * lca_with_paths - store root->node paths and compare: O(n)
"""
from collections import namedtuple


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_lca(root, node1, node2):
    """Finds the LCA of two nodes (by value)."""
    if root is None:
        return None
    if root.data == node1.data or root.data == node2.data:
        return root
    left = find_lca(root.left, node1, node2)
    right = find_lca(root.right, node1, node2)
    # nodes on different subtrees -> this is the LCA
    if left and right:
        return root
    return left if left else right


# contains ancestor info: number of required nodes found and the LCA (or None)
AncestorInfo = namedtuple("AncestorInfo", ["nodes_found", "ancestor"])


def search_lca(root, node1, node2):
    """EPI solution."""
    if root is None:
        return AncestorInfo(0, None)
    left = search_lca(root.left, node1, node2)
    if left.ancestor:
        return left
    right = search_lca(root.right, node1, node2)
    if right.ancestor:
        return right
    nodes_found = (left.nodes_found + right.nodes_found +
                   int(root.data == node1.data or root.data == node2.data))
    return AncestorInfo(nodes_found, root if nodes_found == 2 else None)


# ---------------- Naive approach: O(N^2) time, O(h) space ----------------
def has_node(root, node):
    """True if node is present in the subtree of root."""
    if root is None:
        return False
    return root is node or has_node(root.left, node) or has_node(root.right, node)


def lca_naive(root, n1, n2):
    if root is None:
        return None
    if has_node(root.left, n1) and has_node(root.right, n2):
        return root
    if has_node(root.left, n2) and has_node(root.right, n1):
        return root
    lca_left = lca_naive(root.left, n1, n2)
    lca_right = lca_naive(root.right, n1, n2)
    return lca_left if lca_left is not None else lca_right


# ---------------- Better approach: compare root-to-node paths ----------------
def find_path(root, path, n):
    """Fills path with the nodes from root to n. Returns True if found."""
    if root is None:
        return False
    path.append(root)
    if root is n or find_path(root.left, path, n) or find_path(root.right, path, n):
        return True
    path.pop()
    return False


def lca_with_paths(root, n1, n2):
    path1, path2 = [], []
    if not find_path(root, path1, n1) or not find_path(root, path2, n2):
        return None
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] is not path2[i]:
            return path1[i - 1]  # where the paths diverge
        i += 1
    return path1[i - 1]


def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")


def main():
    r"""
                    1
                  /   \
                2      3
               /  \   /
              4    5  6
                     /
                    7
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    post_order_traversal(root)
    print()
    print(find_lca(root, root.right.left, root.right.left.left).data)
    print(search_lca(root, root.right.left, root.right.left.left).ancestor.data)
    # the alternative approaches, LCA of 4 and 7
    print(lca_naive(root, root.left.left, root.right.left.left).data)
    print(lca_with_paths(root, root.left.left, root.right.left.left).data)


if __name__ == "__main__":
    main()
