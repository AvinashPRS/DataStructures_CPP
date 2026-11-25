"""Cave Doors - subtask where switch i is connected to door i."""
import sys


def explore_cave(n):
    switch_positions = [0] * n
    door_for_switch = list(range(n))
    for i in range(n):
        result = try_combination(switch_positions)
        if result == i:  # door i is closed
            switch_positions[i] = 1
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
    pass  # subtask: switch i controls door i
    explore_cave(n)


if __name__ == "__main__":
    main()
