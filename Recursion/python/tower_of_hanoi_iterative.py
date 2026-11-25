"""
Iterative Tower of Hanoi.

For i in 1 .. 2^n - 1:
    i % 3 == 1: legal move between src and dest
    i % 3 == 2: legal move between src and aux
    i % 3 == 0: legal move between aux and dest
If the number of disks is even, destination and auxiliary swap roles.
"""


def initialize_towers(t, n):
    """Push standard "base" limits so we don't pop from an empty tower."""
    # We add a dummy largest element (n + 1) to act as a floor boundary
    t[0].extend(range(n + 1, 0, -1))
    t[1].append(n + 1)  # note the dummy large element is added
    t[2].append(n + 1)  # note the dummy large element is added


def move_disk_between_pegs(t, src, dest, names):
    """Print and execute the legal move between two pegs."""
    src_top = t[src][-1]
    dest_top = t[dest][-1]

    # If source peg top is smaller, it legally moves to destination
    if src_top < dest_top:
        t[dest].append(t[src].pop())
        print(f"Move disk {src_top} from Peg {names[src]} to Peg {names[dest]}")
    # If destination peg top is smaller, it moves to source instead
    else:
        t[src].append(t[dest].pop())
        print(f"Move disk {dest_top} from Peg {names[dest]} to Peg {names[src]}")


def iterative_hanoi(n):
    # Representation of the 3 rods (0 = Source, 1 = Auxiliary, 2 = Destination)
    t = [[], [], []]
    peg_names = ["A", "B", "C"]

    initialize_towers(t, n)

    total_moves = 2 ** n - 1

    # If number of disks is even, destination and auxiliary swap roles
    src, aux, dest = 0, 1, 2
    if n % 2 == 0:
        aux, dest = dest, aux

    # Iterate through all moves from 1 to 2^n - 1
    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            move_disk_between_pegs(t, src, dest, peg_names)
        elif i % 3 == 2:
            move_disk_between_pegs(t, src, aux, peg_names)
        else:
            move_disk_between_pegs(t, aux, dest, peg_names)


if __name__ == "__main__":
    disks = int(input("Enter the number of disks: "))

    if disks < 1:
        print("Please enter a valid number of disks (>= 1).")
    else:
        print("The sequence of moves involved in the Tower of Hanoi:")
        iterative_hanoi(disks)
