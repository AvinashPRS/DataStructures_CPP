"""
Python port of binary_trees.h + binary_tree_print.c

The C project keeps one function per file ("0-binary_tree_node.c", ...).
Those file names are not valid Python module names, so this module acts as
the "header": it defines the node type and the printer, and lazily resolves
every public function name to the numbered file that implements it.

    from binary_trees import binary_tree_node, binary_tree_print
    import binary_trees as bt; bt.bst_insert(...)

Double pointers (binary_tree_t **tree) are modelled as a one-element list:
    root = [None]
    bst_insert(root, 98)      # root[0] is now the tree
"""
import importlib.util
import os
import sys

_DIR = os.path.dirname(os.path.abspath(__file__))


class BinaryTreeNode:
    """struct binary_tree_s"""
    __slots__ = ("n", "parent", "left", "right")

    def __init__(self, n=0, parent=None):
        self.n = n
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        return "BinaryTreeNode(%d)" % self.n


# typedefs
binary_tree_t = bst_t = avl_t = heap_t = BinaryTreeNode


# ------------------------------------------------------------------ printer
def _print_t(tree, offset, depth, s):
    if tree is None:
        return 0
    is_left = tree.parent is not None and tree.parent.left is tree
    b = "(%03d)" % tree.n
    width = len(b)
    left = _print_t(tree.left, offset, depth + 1, s)
    right = _print_t(tree.right, offset + left + width, depth + 1, s)
    for i in range(width):
        s[depth][offset + left + i] = b[i]
    if depth and is_left:
        for i in range(width + right):
            s[depth - 1][offset + left + width // 2 + i] = "-"
        s[depth - 1][offset + left + width // 2] = "."
    elif depth and not is_left:
        for i in range(left + width):
            s[depth - 1][offset - width // 2 + i] = "-"
        s[depth - 1][offset + left + width // 2] = "."
    return left + width + right


def _height(tree):
    hl = 1 + _height(tree.left) if tree.left else 0
    hr = 1 + _height(tree.right) if tree.right else 0
    return max(hl, hr)


def binary_tree_print(tree):
    """Prints a binary tree (port of stackoverflow.com/a/13755911)."""
    if tree is None:
        return
    height = _height(tree)
    s = [[" "] * 255 for _ in range(height + 1)]
    _print_t(tree, 0, 0, s)
    for row in s:
        print("".join(row).rstrip())


# ------------------------------------------------ lazy function resolution
_FUNCS = {
    "binary_tree_node": "0-binary_tree_node",
    "binary_tree_insert_left": "1-binary_tree_insert_left",
    "binary_tree_insert_right": "2-binary_tree_insert_right",
    "binary_tree_delete": "3-binary_tree_delete",
    "binary_tree_is_leaf": "4-binary_tree_is_leaf",
    "binary_tree_is_root": "5-binary_tree_is_root",
    "binary_tree_preorder": "6-binary_tree_preorder",
    "binary_tree_inorder": "7-binary_tree_inorder",
    "binary_tree_postorder": "8-binary_tree_postorder",
    "binary_tree_height": "9-binary_tree_height",
    "binary_tree_depth": "10-binary_tree_depth",
    "binary_tree_size": "11-binary_tree_size",
    "binary_tree_leaves": "12-binary_tree_leaves",
    "binary_tree_nodes": "13-binary_tree_nodes",
    "binary_tree_balance": "14-binary_tree_balance",
    "binary_tree_is_full": "15-binary_tree_is_full",
    "binary_tree_is_perfect": "16-binary_tree_is_perfect",
    "binary_tree_sibling": "17-binary_tree_sibling",
    "binary_tree_uncle": "18-binary_tree_uncle",
    "binary_trees_ancestor": "100-binary_trees_ancestor",
    "binary_tree_levelorder": "101-binary_tree_levelorder",
    "binary_tree_is_complete": "102-binary_tree_is_complete",
    "binary_tree_rotate_left": "103-binary_tree_rotate_left",
    "binary_tree_rotate_right": "104-binary_tree_rotate_right",
    "binary_tree_is_bst": "110-binary_tree_is_bst",
    "bst_insert": "111-bst_insert",
    "array_to_bst": "112-array_to_bst",
    "bst_search": "113-bst_search",
    "bst_remove": "114-bst_remove",
    "binary_tree_is_avl": "120-binary_tree_is_avl",
    "avl_insert": "121-avl_insert",
    "array_to_avl": "122-array_to_avl",
    "avl_remove": "123-avl_remove",
    "sorted_array_to_avl": "124-sorted_array_to_avl",
    "binary_tree_is_heap": "130-binary_tree_is_heap",
    "heap_insert": "131-heap_insert",
    "swap": "131-heap_insert",
    "convert": "131-heap_insert",
    "array_to_heap": "132-array_to_heap",
    "heap_extract": "133-heap_extract",
    "heap_to_sorted_array": "134-heap_to_sorted_array",
}

_modules = {}


def load(name):
    """Import one of the numbered files (e.g. load('111-bst_insert'))."""
    if name not in _modules:
        path = os.path.join(_DIR, name + ".py")
        spec = importlib.util.spec_from_file_location("bt_" + name.replace("-", "_"), path)
        mod = importlib.util.module_from_spec(spec)
        _modules[name] = mod
        spec.loader.exec_module(mod)
    return _modules[name]


def __getattr__(attr):
    if attr in _FUNCS:
        return getattr(load(_FUNCS[attr]), attr)
    raise AttributeError("module 'binary_trees' has no attribute %r" % attr)


__all__ = ["BinaryTreeNode", "binary_tree_t", "bst_t", "avl_t", "heap_t",
           "binary_tree_print", "load"] + list(_FUNCS)

if _DIR not in sys.path:
    sys.path.insert(0, _DIR)
