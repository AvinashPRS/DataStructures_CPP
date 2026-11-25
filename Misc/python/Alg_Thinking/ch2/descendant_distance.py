"""Descendant Distance: nodes with the most descendants at distance d."""
import sys
from functools import cmp_to_key


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.score = 0


def find_node(nodes, name):
    for n in nodes:
        if n.name == name:
            return n
    return None


def read_tree(tokens, num_lines):
    nodes = []
    for _ in range(num_lines):
        parent_name = next(tokens)
        num_children = int(next(tokens))
        parent_node = find_node(nodes, parent_name)
        if parent_node is None:
            parent_node = Node(parent_name)
            nodes.append(parent_node)
        parent_node.children = []
        for _ in range(num_children):
            child_name = next(tokens)
            child_node = find_node(nodes, child_name)
            if child_node is None:
                child_node = Node(child_name)
                nodes.append(child_node)
            parent_node.children.append(child_node)
    return nodes


def score_one(n, d):
    if d == 1:
        return len(n.children)
    return sum(score_one(c, d - 1) for c in n.children)


def score_all(nodes, d):
    for n in nodes:
        n.score = score_one(n, d)


def compare(n1, n2):
    if n1.score > n2.score:
        return -1
    if n1.score < n2.score:
        return 1
    return (n1.name > n2.name) - (n1.name < n2.name)


def output_info(nodes):
    i = 0
    num_nodes = len(nodes)
    while i < 3 and i < num_nodes and nodes[i].score > 0:
        print(f"{nodes[i].name} {nodes[i].score}")
        i += 1
        while i < num_nodes and nodes[i].score == nodes[i - 1].score:
            print(f"{nodes[i].name} {nodes[i].score}")
            i += 1


def main():
    tokens = iter(sys.stdin.read().split())
    num_cases = int(next(tokens))
    for case_num in range(1, num_cases + 1):
        print(f"Tree {case_num}:")
        n = int(next(tokens))
        d = int(next(tokens))
        nodes = read_tree(tokens, n)
        score_all(nodes, d)
        nodes.sort(key=cmp_to_key(compare))
        output_info(nodes)
        if case_num < num_cases:
            print()


if __name__ == "__main__":
    main()
