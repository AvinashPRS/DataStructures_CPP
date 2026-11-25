"""
Problem:
    Given 3 pegs and 'n' no. of rings each of increasing diameter. All the
    rings are initially on any one of the 'source' pegs and the remaining pegs are empty. Shift the rings
    from initial peg to 'destination' peg in minimum number of steps. We cannot place a bigger ring on top
    of smaller one.

Input:
    n = no. of rings
    src = source/initial peg
    dest = destination peg

Output:
    Print each move made

TC: O(2^n)
T(n) = T(n-1) + 1 + T(n-1)
     = 2^n - 1
"""

NUM_PEGS = 3


def tower_of_hanoi_move(pegs, num_rings, src, dest, aux):
    """
    Performs and prints the moves of moving the rings.

    For moving the rings to the dest peg, we first use the auxiliary peg
    to move the n-1 rings. We then move the largest ring to the dest peg and
    then using the initial peg as auxiliary peg, we move the n-1 rings from
    the current auxiliary peg to the dest peg.
    """
    # base condition
    if num_rings > 0:
        # first move the n-1 rings to the auxiliary peg
        tower_of_hanoi_move(pegs, num_rings - 1, src, aux, dest)

        # move the last ring to the destination peg
        last_ring = pegs[src].pop()
        pegs[dest].append(last_ring)

        print(f"Ring {last_ring + 1} moved from Peg {src + 1} to {dest + 1}")

        # now move the n-1 rings from aux peg to the destination peg this time using
        # initial src peg as aux peg
        tower_of_hanoi_move(pegs, num_rings - 1, aux, dest, src)


def tower_hanoi_driver(num_rings, src, dest, aux):
    """Driver function for the Hanoi steps function."""
    # for storing peg states (each peg is a stack)
    pegs = [[] for _ in range(NUM_PEGS)]

    # initialize the initial peg with rings (largest at the bottom)
    for i in range(num_rings - 1, -1, -1):
        pegs[src].append(i)

    # do the required moves
    tower_of_hanoi_move(pegs, num_rings, src, dest, aux)


if __name__ == "__main__":
    tower_hanoi_driver(3, 0, 1, 2)
    print()
    tower_hanoi_driver(4, 0, 1, 2)
