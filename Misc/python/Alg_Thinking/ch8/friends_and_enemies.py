"""Friends and Enemies: union-find tracking each set's enemy set.
Ops: 1 = setFriends, 2 = setEnemies, 3 = areFriends, 4 = areEnemies, 0 = end."""
import sys


def find(x, parent):
    """Find with path compression."""
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:
        parent[x], x = root, parent[x]
    return root


def union_sets(person1, person2, parent, size):
    set1 = find(person1, parent)
    set2 = find(person2, parent)
    if set1 != set2:
        if size[set1] > size[set2]:
            set1, set2 = set2, set1
        parent[set1] = set2
        size[set2] += size[set1]
    return set2


def set_friends(person1, person2, parent, size, enemy_of):
    set1 = find(person1, parent)
    set2 = find(person2, parent)
    bigger_set = union_sets(person1, person2, parent, size)
    if enemy_of[set1] != -1 and enemy_of[set2] != -1:
        union_sets(enemy_of[set1], enemy_of[set2], parent, size)
    other_set = set2 if bigger_set == set1 else set1
    if enemy_of[bigger_set] == -1:
        enemy_of[bigger_set] = enemy_of[other_set]


def set_enemies(person1, person2, parent, size, enemy_of):
    set1 = find(person1, parent)
    set2 = find(person2, parent)
    enemy = enemy_of[set1]
    if enemy == -1:
        enemy_of[set1] = person2
    else:
        union_sets(enemy, person2, parent, size)
    enemy = enemy_of[set2]
    if enemy == -1:
        enemy_of[set2] = person1
    else:
        union_sets(enemy, person1, parent, size)


def are_friends(person1, person2, parent):
    return find(person1, parent) == find(person2, parent)


def are_enemies(person1, person2, parent, enemy_of):
    enemy = enemy_of[find(person1, parent)]
    return enemy != -1 and find(enemy, parent) == find(person2, parent)


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    num_people = data[0]
    parent = list(range(num_people))
    size = [1] * num_people
    enemy_of = [-1] * num_people
    pos = 1
    while pos + 2 < len(data) + 1:
        op, person1, person2 = data[pos], data[pos + 1], data[pos + 2]
        pos += 3
        if op == 0:
            break
        if op == 1:
            if are_enemies(person1, person2, parent, enemy_of):
                print(-1)
            else:
                set_friends(person1, person2, parent, size, enemy_of)
        elif op == 2:
            if are_friends(person1, person2, parent):
                print(-1)
            else:
                set_enemies(person1, person2, parent, size, enemy_of)
        elif op == 3:
            print(1 if are_friends(person1, person2, parent) else 0)
        elif op == 4:
            print(1 if are_enemies(person1, person2, parent, enemy_of) else 0)


if __name__ == "__main__":
    main()
