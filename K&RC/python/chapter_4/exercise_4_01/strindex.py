"""Exercise 4-1: strindex(s, t) returns the position of the rightmost
occurrence of t in s, or -1 if there is none."""
import sys


def strindex(source, pattern):
    print("line len: %d" % len(source))

    for i in range(len(source), -1, -1):
        k = 0
        while k < len(pattern) and i + k < len(source) \
                and source[i + k] == pattern[k]:
            k += 1
        if k > 0 and k == len(pattern):
            return i

    return -1


def main():
    pattern = "example"
    line = sys.stdin.readline()
    print(line)

    print("Pattern found at index %d" % strindex(line, pattern))


if __name__ == "__main__":
    main()

# NOTE: It is simple to find the rightmost pattern by iterating the initial
# string from the end to the beginning.
