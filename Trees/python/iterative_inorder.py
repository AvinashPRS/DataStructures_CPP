"""
    Given a tree. Do inorder traversal without recursion.
    Solution:
        We use stack for imitating the recursive calls.
        TC: O(n)
        SC: O(h), for the stack
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def iterative_inorder_traversal(root):
    """Inorder traversal without recursion."""
    s = []
    curr = root
    # go as left as possible, then print current and go right,
    # else go back to the parent
    while curr or s:
        if curr:
            s.append(curr)
            curr = curr.left
        else:
            curr = s.pop()
            print(curr.data, end=" ")
            curr = curr.right


def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")


def build_sample_tree():
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
    return root


def main():
    root = build_sample_tree()
    post_order_traversal(root)
    print()
    iterative_inorder_traversal(root)
    print()


if __name__ == "__main__":
    main()
