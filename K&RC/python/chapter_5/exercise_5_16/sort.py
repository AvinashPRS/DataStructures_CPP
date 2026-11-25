"""Exercise 5-16: sort lines with options: -n, -r, -f, -d (directory order)

run: python3 sort.py -df < file_in.txt
"""
import sys

MAX_NR_OF_LINES = 5000

order = 1      # 1 ascendent, -1 descendent
fold = False   # case insensitive comparison
directory = False  # compare only letters, digits and blanks
comp = None


def atof(s):
    """Parse the leading floating point number of s like C's atof."""
    s = s.lstrip()
    end = 0
    best = 0.0
    while end < len(s):
        end += 1
        try:
            best = float(s[:end])
        except ValueError:
            if s[:end] not in ("+", "-", ".", "+.", "-.") and \
                    not s[:end].lower().endswith(("e", "e+", "e-")):
                break
    return best


def numcmp(s1, s2):
    nr1 = atof(s1)
    nr2 = atof(s2)
    if nr1 < nr2:
        return order * -1
    if nr1 > nr2:
        return order * 1
    return 0


def estrcmp(s1, s2):
    i = j = 0
    while i < len(s1) and j < len(s2):
        if directory:
            while i < len(s1) and not s1[i].isalnum() and not s1[i].isspace():
                i += 1
            while j < len(s2) and not s2[j].isalnum() and not s2[j].isspace():
                j += 1
            if i >= len(s1) or j >= len(s2):
                break

        c1, c2 = s1[i], s2[j]
        if fold:
            c1, c2 = c1.lower(), c2.lower()
        result = ord(c1) - ord(c2)
        if result != 0:
            return order * result
        i += 1
        j += 1

    # One string is a prefix of the other: the shorter one comes first
    return order * ((i < len(s1)) - (j < len(s2)))


def parse_arg_list(args):
    global comp, order, fold, directory
    for arg in args:
        if len(arg) > 1 and arg[0] == "-":
            for flag in arg[1:]:
                if flag not in "nrfd":
                    return False
                if flag == "n":
                    comp = numcmp
                elif flag == "r":
                    order = -1
                elif flag == "f":
                    fold = True
                elif flag == "d":
                    directory = True
        else:
            return False
    return True


def read_lines(max_nr_of_lines):
    lines = []
    for line in sys.stdin:
        if len(lines) >= max_nr_of_lines:
            return None
        lines.append(line.rstrip("\n"))
    return lines


def write_lines(lines):
    for line in lines:
        print(line)


def swap(v, i, j):
    v[i], v[j] = v[j], v[i]


def quick_sort(v, start, end, cmp):
    if start >= end:
        return

    swap(v, start, (start + end) // 2)

    last = start
    for i in range(start + 1, end + 1):
        if cmp(v[i], v[start]) < 0:
            last += 1
            swap(v, last, i)

    swap(v, start, last)
    quick_sort(v, start, last - 1, cmp)
    quick_sort(v, last + 1, end, cmp)


def main(argv):
    global comp
    comp = estrcmp
    if not parse_arg_list(argv[1:]):
        print("Error: invalid arguments.")
        return 1

    lines = read_lines(MAX_NR_OF_LINES)
    if lines is None:
        print("Error: input too large.")
        return 1

    quick_sort(lines, 0, len(lines) - 1, comp)
    write_lines(lines)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
