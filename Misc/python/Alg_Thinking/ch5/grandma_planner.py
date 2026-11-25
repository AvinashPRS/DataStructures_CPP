"""Grandma Planner: shortest path through a cookie store, and number of
such shortest paths (mod 1000000). Dijkstra on (town, state)."""
import sys


def solve(adj_list, num_towns, store):
    done = [[False, False] for _ in range(num_towns + 1)]
    min_distances = [[-1, -1] for _ in range(num_towns + 1)]
    num_paths = [[0, 0] for _ in range(num_towns + 1)]
    min_distances[1][0] = 0
    num_paths[1][0] = 1

    for _ in range(num_towns * 2):
        min_distance = -1
        found = False
        for state in range(2):
            for j in range(1, num_towns + 1):
                if not done[j][state] and min_distances[j][state] >= 0:
                    if min_distance == -1 or min_distances[j][state] < min_distance:
                        min_distance = min_distances[j][state]
                        min_town_index = j
                        min_state_index = state
                        found = True
        if not found:
            break
        done[min_town_index][min_state_index] = True

        if min_state_index == 0 and store[min_town_index]:
            old_distance = min_distances[min_town_index][1]
            if old_distance == -1 or old_distance >= min_distance:
                min_distances[min_town_index][1] = min_distance
                if old_distance == min_distance:
                    num_paths[min_town_index][1] += num_paths[min_town_index][0]
                else:
                    num_paths[min_town_index][1] = num_paths[min_town_index][0]
                num_paths[min_town_index][1] %= 1000000
        else:
            for to_town, length in adj_list[min_town_index]:
                old_distance = min_distances[to_town][min_state_index]
                if old_distance == -1 or old_distance >= min_distance + length:
                    min_distances[to_town][min_state_index] = min_distance + length
                    if old_distance == min_distance + length:
                        num_paths[to_town][min_state_index] += \
                            num_paths[min_town_index][min_state_index]
                    else:
                        num_paths[to_town][min_state_index] = \
                            num_paths[min_town_index][min_state_index]
                    num_paths[to_town][min_state_index] %= 1000000
    print(f"{min_distances[num_towns][1]} {num_paths[num_towns][1]}")


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    num_towns = data[0]
    pos = 1
    adj_list = [[] for _ in range(num_towns + 1)]
    for from_town in range(1, num_towns + 1):
        for to_town in range(1, num_towns + 1):
            length = data[pos]
            pos += 1
            if from_town != to_town:
                adj_list[from_town].insert(0, (to_town, length))
    num_stores = data[pos]
    pos += 1
    store = [0] * (num_towns + 1)
    for store_num in data[pos:pos + num_stores]:
        store[store_num] = 1
    solve(adj_list, num_towns, store)


if __name__ == "__main__":
    main()
