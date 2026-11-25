# Chapter 5, exercise 1: produce a permuted index of the input lines.
import sys

from rotation import compare, format_rotation, get_rotations, max_first_width


def main():
    rotations = []
    for line in sys.stdin.read().splitlines():
        rotations.extend(get_rotations(line))

    rotations.sort(key=compare)

    max_width = max_first_width(rotations)
    for r in rotations:
        print(format_rotation(r, max_width))


if __name__ == "__main__":
    main()
