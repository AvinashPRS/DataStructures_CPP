"""Halloween Haul: minimum streets walked and total candy collected."""
import sys

TEST_CASES = 5


class Node:
    def __init__(self, candy=0, left=None, right=None):
        self.candy = candy
        self.left = left
        self.right = right


def tree_candy(tree):
    if not tree.left and not tree.right:
        return tree.candy
    return tree_candy(tree.left) + tree_candy(tree.right)


def tree_streets(tree):
    if not tree.left and not tree.right:
        return 0
    return tree_streets(tree.left) + tree_streets(tree.right) + 4


def tree_height(tree):
    if not tree.left and not tree.right:
        return 0
    return 1 + max(tree_height(tree.left), tree_height(tree.right))


def tree_solve(tree):
    candy = tree_candy(tree)
    height = tree_height(tree)
    num_streets = tree_streets(tree) - height
    print(f"{num_streets} {candy}")


def read_tree_helper(line, pos):
    """pos is a one-element list used as a mutable index."""
    tree = Node()
    if line[pos[0]] == "(":
        pos[0] += 1
        tree.left = read_tree_helper(line, pos)
        pos[0] += 1
        tree.right = read_tree_helper(line, pos)
        pos[0] += 1
        return tree
    tree.candy = ord(line[pos[0]]) - ord("0")
    pos[0] += 1
    if line[pos[0]] not in (")", " ", "\0"):
        tree.candy = tree.candy * 10 + ord(line[pos[0]]) - ord("0")
        pos[0] += 1
    return tree


def read_tree(line):
    return read_tree_helper(line + "\0", [0])


def main():
    for _ in range(TEST_CASES):
        line = sys.stdin.readline().rstrip("\n")
        if not line:
            break
        tree_solve(read_tree(line))


if __name__ == "__main__":
    main()
