"""Binary tree helper utilities (Python version of Binary_tree_utils.h)."""
import random
import sys

from binary_tree_prototype import BinaryTreeNode

INT_MAX = 2**31 - 1


def generate_rand_binary_tree(n, is_unique=False):
    """Generates a random binary tree with n + 1 nodes.
    If is_unique, the node values are n, n-1, ..., 0."""
    if is_unique:
        root = BinaryTreeNode(n)
        n -= 1
    else:
        root = BinaryTreeNode(random.randint(0, INT_MAX))
    # list of (parent, 'left'/'right') empty child slots
    slots = [(root, "left"), (root, "right")]
    while n > 0:
        n -= 1
        x = random.randrange(len(slots))
        parent, side = slots.pop(x)
        node = BinaryTreeNode(n if is_unique else random.randint(0, INT_MAX))
        setattr(parent, side, node)
        slots.append((node, "left"))
        slots.append((node, "right"))
    return root


def delete_binary_tree(n):
    """Python is garbage collected; this just detaches the children."""
    if n:
        if n.left:
            delete_binary_tree(n.left)
        if n.right:
            delete_binary_tree(n.right)
        n.left = n.right = None


def is_two_binary_trees_equal(r1, r2):
    if r1 and r2:
        return (is_two_binary_trees_equal(r1.left, r2.left) and
                is_two_binary_trees_equal(r1.right, r2.right) and
                r1.data == r2.data)
    return not r1 and not r2


def generate_preorder(r):
    ret = []

    def helper(node):
        if node:
            ret.append(node.data)
            helper(node.left)
            helper(node.right)
    helper(r)
    return ret


def generate_inorder(r):
    ret = []

    def helper(node):
        if node:
            helper(node.left)
            ret.append(node.data)
            helper(node.right)
    helper(r)
    return ret


def generate_postorder(r):
    ret = []

    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            ret.append(node.data)
    helper(r)
    return ret


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    t = generate_rand_binary_tree(9, is_unique=True)
    print("preorder: ", generate_preorder(t))
    print("inorder:  ", generate_inorder(t))
    print("postorder:", generate_postorder(t))
    print("equal to itself:", is_two_binary_trees_equal(t, t))
