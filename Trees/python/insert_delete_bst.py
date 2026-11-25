class Node:
    """Definition of BST Node."""

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def insert(root, value):
    """Insert a value into the BST; returns the (possibly new) root."""
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    return root


def find_min(root):
    """Minimum value node in a subtree (inorder successor helper)."""
    current = root
    while current and current.left is not None:
        current = current.left
    return current


def delete_node(root, key):
    """Delete key from the BST; returns the new root."""
    if root is None:  # key is not in the tree
        return root
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        # Case 1: no child, or Case 2: one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Case 3: two children -> copy inorder successor, then delete it
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def main():
    root = None
    # Test Insertion
    root = insert(root, 50)
    for v in (30, 20, 40, 70, 60, 80):
        insert(root, v)

    print("Inorder traversal of the BST: ", end="")
    inorder(root)
    print()

    # Test Deletion
    print("\nDelete 20 (Leaf Node):")
    root = delete_node(root, 20)
    print("Inorder traversal: ", end="")
    inorder(root)
    print()

    print("\nDelete 30 (Node with single child):")
    root = delete_node(root, 30)
    print("Inorder traversal: ", end="")
    inorder(root)
    print()

    print("\nDelete 50 (Node with two children):")
    root = delete_node(root, 50)
    print("Inorder traversal: ", end="")
    inorder(root)
    print()


if __name__ == "__main__":
    main()
