"""Cave Doors (IOI 2013): binary search to find each door's switch."""
import sys


def set_a_switch(door, switch_positions, door_for_switch, n):
    low, high = 0, n - 1

    for i in range(n):
        if door_for_switch[i] == -1:
            switch_positions[i] = 0

    result = try_combination(switch_positions)
    if result != door:
        for i in range(n):
            if door_for_switch[i] == -1:
                switch_positions[i] = 1

    while low != high:
        mid = (low + high) // 2
        for i in range(low, mid + 1):
            if door_for_switch[i] == -1:
                switch_positions[i] = 1 - switch_positions[i]
        result = try_combination(switch_positions)
        if result != door:
            high = mid
            for i in range(low, mid + 1):
                if door_for_switch[i] == -1:
                    switch_positions[i] = 1 - switch_positions[i]
        else:
            low = mid + 1
    door_for_switch[low] = door
    switch_positions[low] = 1 - switch_positions[low]


def explore_cave(n):
    switch_positions = [0] * n
    door_for_switch = [-1] * n
    for i in range(n):
        set_a_switch(i, switch_positions, door_for_switch, n)
    answer(switch_positions, door_for_switch)


# ---------------------------------------------------------------------------
# Simple local grader (the original IOI task supplies tryCombination/answer).
# A hidden cave: switch i controls door connection[i], and door connection[i]
# is open when switch i is at position correct[i].
# tryCombination returns the first closed door, or -1 if all doors are open.
# ---------------------------------------------------------------------------
_correct = []
_connection = []


def try_combination(switch_positions):
    n = len(_correct)
    door_open = [False] * n
    for i in range(n):
        door_open[_connection[i]] = switch_positions[i] == _correct[i]
    for d in range(n):
        if not door_open[d]:
            return d
    return -1


def answer(switch_positions, door_for_switch):
    ok = list(switch_positions) == _correct and list(door_for_switch) == _connection
    print("Switch positions:", " ".join(map(str, switch_positions)))
    print("Door for switch: ", " ".join(map(str, door_for_switch)))
    print("Correct!" if ok else "Wrong!")


def main():
    global _correct, _connection
    import random
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    _correct = [random.randint(0, 1) for _ in range(n)]
    _connection = list(range(n))
    random.shuffle(_connection)
    explore_cave(n)


if __name__ == "__main__":
    main()
