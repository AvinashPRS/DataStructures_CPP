"""Exercise 6-4: print the distinct words in its input sorted into
decreasing order of frequency of occurrence.

run: python3 words_frequency.py < words_frequency.py
"""
import sys

MAX_NR_OF_NODES = 1000


class TreeNode:
    def __init__(self, word):
        self.word = word
        self.count = 1
        self.left = None
        self.right = None


def add_to_tree(node, word):
    if node is None:
        return TreeNode(word)
    if word == node.word:
        node.count += 1
    elif word < node.word:
        node.left = add_to_tree(node.left, word)
    else:
        node.right = add_to_tree(node.right, word)
    return node


def copy_tree_to_array(arr, node):
    if node is not None:
        copy_tree_to_array(arr, node.left)
        if len(arr) < MAX_NR_OF_NODES:
            arr.append(node)
        copy_tree_to_array(arr, node.right)


def get_words(text):
    """Yield the words (alphanumeric + underscore, starting with a letter or
    underscore) and the single other characters of text."""
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c in " \t":
            i += 1
            continue
        if c.isalpha() or c == "_":
            j = i + 1
            while j < n and (text[j].isalnum() or text[j] == "_"):
                j += 1
            yield text[i:j]
            i = j
        else:
            yield c
            i += 1


def tree_node_cmp(n1, n2):
    if n1.count > n2.count:
        return -1
    if n1.count < n2.count:
        return 1
    return 0


def swap(v, i, j):
    v[i], v[j] = v[j], v[i]


def quick_sort(v, start, end, comp):
    if start >= end:
        return
    swap(v, start, (start + end) // 2)
    last = start
    for i in range(start + 1, end + 1):
        if comp(v[i], v[start]) < 0:
            last += 1
            swap(v, last, i)
    swap(v, start, last)
    quick_sort(v, start, last - 1, comp)
    quick_sort(v, last + 1, end, comp)


def main():
    tree_root = None
    for word in get_words(sys.stdin.read()):
        if word[0].isalpha():
            tree_root = add_to_tree(tree_root, word)

    nodes = []
    copy_tree_to_array(nodes, tree_root)
    quick_sort(nodes, 0, len(nodes) - 1, tree_node_cmp)

    for node in nodes:
        print("%4d %s" % (node.count, node.word))


if __name__ == "__main__":
    main()
