"""
    Given a tree. Do preorder traversal without recursion.
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


def iterative_preorder_traversal(root):
    """Method 1: print while going left, use the stack to come back."""
    s = []
    curr = root
    while curr or s:
        if curr:
            s.append(curr)
            print(curr.data, end=" ")
            curr = curr.left
        else:
            curr = s.pop()
            curr = curr.right


def iterative_preorder_traversal1(root):
    """Method 2: pop a node, print it, push right then left child."""
    s = [root]
    while s:
        curr = s.pop()
        if curr:
            print(curr.data, end=" ")
            # right is below left in stack
            s.append(curr.right)
            s.append(curr.left)


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
    # post_order_traversal(root)
    print()
    iterative_preorder_traversal1(root)
    print()


if __name__ == "__main__":
    main()
