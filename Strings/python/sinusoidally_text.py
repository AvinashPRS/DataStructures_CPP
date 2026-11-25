"""
Problem:
    Given a text t, print it in sinusoidal fashion
    e.g: "mynameis"
      y       e
    m   n   m   i
          a       s

Input:
    t: string

Output:
    Nothing just print the text

TC: O(n), n: no. of chars
"""


def print_sinusoidally(s):
    """
    There are three rows involved in the printing. Also each row
    only has indices with a fixed constant difference.
        row 1: 1, 5, 9 ...
        row 2: 0, 2, 4, 6 ...
        row 3: 3, 7, 11 ...
    """
    # print the indices at 1, 5 .. positions
    print("".join(" " + s[i] + "  " for i in range(1, len(s), 4)))

    # print the indices at 0, 2 .. positions, each char separated by 1 space
    print("".join(s[i] + " " for i in range(0, len(s), 2)))

    # print the indices at 3, 7 .. positions, each char preceded by three spaces
    print("".join("   " + s[i] for i in range(3, len(s), 4)))


if __name__ == "__main__":
    print_sinusoidally("abcdefghijklmnopqrstuvwxyz")
