# Chapter 3, exercise 2: print the four quartiles of a set of integers
# (largest quartile first).
import sys


def main():
    print("Please enter the numbers, followed by end-of-file.")
    numbers = sorted(int(tok) for tok in sys.stdin.read().split())

    count = len(numbers)
    if count < 4:
        print("You must enter at least 4 numbers.")
        return 1

    quartile_size = count // 4
    quartile_remainder = count % 4

    out = []
    for i in range(count - 1, -1, -1):
        if i == count - 1:
            out.append("First quartile: ")
        elif i == 3 * quartile_size - 1 + quartile_remainder:
            out.append("\nSecond quartile: ")
        elif i == 2 * quartile_size - 1 + (quartile_remainder - 1 if quartile_remainder > 1 else 0):
            out.append("\nThird quartile: ")
        elif i == quartile_size - 1 + (1 if quartile_remainder == 3 else 0):
            out.append("\nFourth quartile: ")
        out.append(f"{numbers[i]} ")
    print("".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
