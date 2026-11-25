"""Social Network - fastest, with union by size and path compression."""
import sys


def find(x, parent):
    """Find with path compression."""
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:
        parent[x], x = root, parent[x]
    return root


def union_communities(person1, person2, parent, size, num_community):
    community1 = find(person1, parent)
    community2 = find(person2, parent)
    if community1 != community2 and \
            size[community1] + size[community2] <= num_community:
        if size[community1] > size[community2]:
            community1, community2 = community2, community1
        parent[community1] = community2
        size[community2] += size[community1]


def main():
    tokens = sys.stdin.read().split()
    num_people, num_community, num_ops = int(tokens[0]), int(tokens[1]), int(tokens[2])
    parent = list(range(num_people + 1))
    size = [1] * (num_people + 1)
    pos = 3
    for _ in range(num_ops):
        op = tokens[pos]
        pos += 1
        if op == "A":
            person1, person2 = int(tokens[pos]), int(tokens[pos + 1])
            pos += 2
            union_communities(person1, person2, parent, size, num_community)
        elif op == "E":
            person1, person2 = int(tokens[pos]), int(tokens[pos + 1])
            pos += 2
            print("Yes" if find(person1, parent) == find(person2, parent) else "No")
        else:
            person1 = int(tokens[pos])
            pos += 1
            print(size[find(person1, parent)])


if __name__ == "__main__":
    main()
