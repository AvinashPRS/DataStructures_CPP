"""Social Network - too slow (inefficient union-find: relabels everyone)."""
import sys


def find(person, community_of):
    return community_of[person]


def union_communities(person1, person2, community_of, size,
                      num_community, num_people):
    community1 = find(person1, community_of)
    community2 = find(person2, community_of)
    if community1 == community2:
        return
    if size[community1] + size[community2] > num_community:
        return
    for i in range(1, num_people + 1):
        if community_of[i] == community1:
            community_of[i] = community2
            size[community2] += 1


def main():
    tokens = sys.stdin.read().split()
    num_people, num_community, num_ops = int(tokens[0]), int(tokens[1]), int(tokens[2])
    parent = list(range(num_people + 1))  # community_of
    size = [1] * (num_people + 1)
    pos = 3
    for _ in range(num_ops):
        op = tokens[pos]
        pos += 1
        if op == "A":
            person1, person2 = int(tokens[pos]), int(tokens[pos + 1])
            pos += 2
            union_communities(person1, person2, parent, size, num_community, num_people)
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
