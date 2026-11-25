"""Exercise 1-14: histogram of the frequencies of characters (a-z, 0-9)."""
import sys

ALPHA_NR = 26
NUM_NR = 10


def main():
    chars_freq = [0] * (ALPHA_NR + NUM_NR)

    # Count characters from the standard input
    for c in sys.stdin.read():
        if "a" <= c <= "z":
            chars_freq[ord(c) - ord("a")] += 1
        elif "0" <= c <= "9":
            chars_freq[ord(c) - ord("0") + ALPHA_NR] += 1

    # Print horizontal histogram
    for i in range(ALPHA_NR + NUM_NR):
        if i < ALPHA_NR:
            label = chr(ord("a") + i)
        else:
            label = chr(ord("0") + i - ALPHA_NR)
        print("%s: %s" % (label, "#" * chars_freq[i]))


if __name__ == "__main__":
    main()
