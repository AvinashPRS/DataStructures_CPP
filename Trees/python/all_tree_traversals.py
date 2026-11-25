r"""
All binary tree traversals, recursive and iterative.

    Constructed Binary Tree:
             1
           /   \
          2     3
         / \   /
        4   5 6
"""
from collections import deque


class Node:
    """Definition of a Binary Tree Node."""

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# 1. Pre-order Traversal (Root -> Left -> Right)
def pre_order(root):
    if root is None:
        return
    print(root.data, end=" ")
    pre_order(root.left)
    pre_order(root.right)


# 2. In-order Traversal (Left -> Root -> Right)
def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)


# 3. Post-order Traversal (Left -> Right -> Root)
def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data, end=" ")


# 4. Level-order Traversal (Breadth-First Search)
def level_order(root):
    if root is None:
        return
    q = deque([root])
    while q:
        current = q.popleft()
        print(current.data, end=" ")
        if current.left is not None:
            q.append(current.left)
        if current.right is not None:
            q.append(current.right)


# ============================== ITERATIVE TRAVERSALS ==============================

# 1. Iterative Pre-order Traversal (Root -> Left -> Right)
def iterative_pre_order(root):
    if root is None:
        return
    st = [root]
    while st:
        current = st.pop()
        print(current.data, end=" ")
        # push RIGHT first so LEFT is processed first (LIFO)
        if current.right is not None:
            st.append(current.right)
        if current.left is not None:
            st.append(current.left)


# 2. Iterative In-order Traversal (Left -> Root -> Right)
def iterative_in_order(root):
    st = []
    current = root
    while current is not None or st:
        # reach the leftmost node of the current node
        while current is not None:
            st.append(current)
            current = current.left
        current = st.pop()
        print(current.data, end=" ")
        # node and its left subtree are done; now the right subtree
        current = current.right


# 3. Iterative Post-order Traversal (Left -> Right -> Root) using Two Stacks
def iterative_post_order(root):
    if root is None:
        return
    st1 = [root]   # for processing nodes
    st2 = []       # stores the reversed post-order sequence
    while st1:
        current = st1.pop()
        st2.append(current)
        # push left first so right is processed first out of st1
        if current.left is not None:
            st1.append(current.left)
        if current.right is not None:
            st1.append(current.right)
    while st2:
        print(st2.pop().data, end=" ")


# 4. Iterative Level-order Traversal (Breadth-First Search)
def iterative_level_order(root):
    if root is None:
        return
    q = deque([root])
    while q:
        current = q.popleft()
        print(current.data, end=" ")
        if current.left is not None:
            q.append(current.left)
        if current.right is not None:
            q.append(current.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    for label, fn in (("Pre-order Traversal:  ", pre_order),
                      ("In-order Traversal:   ", in_order),
                      ("Post-order Traversal: ", post_order),
                      ("Level-order Traversal: ", level_order),
                      ("Iterative Pre-order Traversal:  ", iterative_pre_order),
                      ("Iterative In-order Traversal:   ", iterative_in_order),
                      ("Iterative Post-order Traversal: ", iterative_post_order),
                      ("Iterative Level-order Traversal: ", iterative_level_order)):
        print(label, end="")
        fn(root)
        print()


if __name__ == "__main__":
    main()
