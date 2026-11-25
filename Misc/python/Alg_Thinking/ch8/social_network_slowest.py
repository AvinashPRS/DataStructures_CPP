"""Social Network - too slow (uses too many BFS calls)."""
import sys


def find_distances(adj_list, person, num_people):
    min_moves = [-1] * (num_people + 1)
    min_moves[person] = 0
    cur_positions = [person]
    while cur_positions:
        new_positions = []
        for from_person in cur_positions:
            for to_person in adj_list[from_person]:
                if min_moves[to_person] == -1:
                    min_moves[to_person] = 1 + min_moves[from_person]
                    new_positions.append(to_person)
        cur_positions = new_positions
    return min_moves


def size(num_people, min_moves):
    return sum(1 for i in range(1, num_people + 1) if min_moves[i] != -1)


def main():
    tokens = sys.stdin.read().split()
    num_people, num_community, num_ops = int(tokens[0]), int(tokens[1]), int(tokens[2])
    adj_list = [[] for _ in range(num_people + 1)]
    pos = 3
    for _ in range(num_ops):
        op = tokens[pos]
        pos += 1
        if op == "A":
            person1, person2 = int(tokens[pos]), int(tokens[pos + 1])
            pos += 2
            min_moves = find_distances(adj_list, person1, num_people)
            size1 = size(num_people, min_moves)
            same_community = min_moves[person2] != -1
            min_moves = find_distances(adj_list, person2, num_people)
            size2 = size(num_people, min_moves)
            if same_community or size1 + size2 <= num_community:
                adj_list[person1].insert(0, person2)
                adj_list[person2].insert(0, person1)
        elif op == "E":
            person1, person2 = int(tokens[pos]), int(tokens[pos + 1])
            pos += 2
            min_moves = find_distances(adj_list, person1, num_people)
            print("Yes" if min_moves[person2] != -1 else "No")
        else:
            person1 = int(tokens[pos])
            pos += 1
            min_moves = find_distances(adj_list, person1, num_people)
            print(size(num_people, min_moves))


if __name__ == "__main__":
    main()
