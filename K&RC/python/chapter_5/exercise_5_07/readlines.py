"""Exercise 5-7: readlines storing lines in an array supplied by main
instead of calling alloc, then sort them with quicksort."""
import sys

MAXLINES = 5000   # max number of lines to be sorted
MAXSTORE = 10000  # max number of chars from all lines to be stored


def readlines(max_nr_of_lines):
    """Return the list of lines, or None if the input is too big."""
    lines = []
    stored = 0
    for line in sys.stdin:
        line = line.rstrip("\n")  # Delete newline
        if len(lines) >= max_nr_of_lines or stored + len(line) + 1 > MAXSTORE:
            return None
        lines.append(line)
        stored += len(line) + 1
    return lines


def writelines(lines):
    for line in lines:
        print(line)


def swap(v, i, j):
    v[i], v[j] = v[j], v[i]


def quick_sort(v, left, right):
    # Do nothing if the array contains less than 2 elements
    if left >= right:
        return

    swap(v, left, (left + right) // 2)
    last = left

    for i in range(left + 1, right + 1):
        if v[i] < v[left]:
            last += 1
            swap(v, last, i)

    swap(v, left, last)
    quick_sort(v, left, last - 1)
    quick_sort(v, last + 1, right)


def main():
    lines = readlines(MAXLINES)
    if lines is not None:
        quick_sort(lines, 0, len(lines) - 1)
        print("-----")
        writelines(lines)
        return 0
    print("Error: input too big to sort.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
