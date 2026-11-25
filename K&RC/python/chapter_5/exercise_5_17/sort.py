"""Exercise 5-17: sort with field-searching capability, so sorting may be
done on fields within lines, each field sorted according to an independent
set of options (-n numeric, -r reverse, -f fold case, -d directory order).

run: python3 sort.py -3nr -2f < file_in.txt
"""
import re
import sys

MAX_NR_OF_LINES = 5000


class Options:
    def __init__(self):
        self.index = 0
        self.numeric = False
        self.order = 1
        self.fold = False
        self.directory = False


def atof(s):
    m = re.match(r"\s*[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?", s)
    return float(m.group(0)) if m else 0.0


def numcmp(s1, s2, opt):
    nr1, nr2 = atof(s1), atof(s2)
    if nr1 < nr2:
        return -opt.order
    if nr1 > nr2:
        return opt.order
    return 0


def estrcmp(s1, s2, opt):
    i = j = 0
    while i < len(s1) and j < len(s2):
        if opt.directory:
            while i < len(s1) and not s1[i].isalnum() and not s1[i].isspace():
                i += 1
            while j < len(s2) and not s2[j].isalnum() and not s2[j].isspace():
                j += 1
            if i >= len(s1) or j >= len(s2):
                break

        c1, c2 = s1[i], s2[j]
        if opt.fold:
            c1, c2 = c1.lower(), c2.lower()
        result = ord(c1) - ord(c2)
        if result != 0:
            return opt.order * result
        i += 1
        j += 1

    # One string is a prefix of the other: the shorter one comes first
    return opt.order * ((i < len(s1)) - (j < len(s2)))


def compare(s1, s2, opt):
    return numcmp(s1, s2, opt) if opt.numeric else estrcmp(s1, s2, opt)


def str_nth_blank_pos(s, n):
    """Position right after the n-th run of blanks in s."""
    pos = 0
    while n and pos < len(s):
        if s[pos] in " \t":
            while pos < len(s) and s[pos] in " \t":
                pos += 1
            n -= 1
        else:
            pos += 1
    return pos


def field(s, index):
    return s[str_nth_blank_pos(s, index - 1):str_nth_blank_pos(s, index)]


def parse_arg_list(args):
    """Return (global_options, list_of_field_options) or None if invalid."""
    fields = []
    global_opt = Options()

    for arg in args:
        if not (len(arg) > 1 and arg[0] == "-"):
            return None

        opt = Options()
        m = re.match(r"-(\d*)([nrfd]*)$", arg)
        if not m:
            return None
        if m.group(1):
            opt.index = int(m.group(1))
        for flag in m.group(2):
            if flag == "n":
                opt.numeric = True
            elif flag == "r":
                opt.order = -1
            elif flag == "f":
                opt.fold = True
            elif flag == "d":
                opt.directory = True

        if opt.index:
            fields.append(opt)
        elif len(args) > 1:
            return None  # several args are only allowed with field indexes
        else:
            global_opt = opt

    return global_opt, fields


def make_cmp(global_opt, fields):
    if not fields:
        return lambda a, b: compare(a, b, global_opt)

    def fieldscmp(s1, s2):
        for opt in fields:
            result = compare(field(s1, opt.index), field(s2, opt.index), opt)
            if result != 0:
                return result
        return 0

    return fieldscmp


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
    parsed = parse_arg_list(argv[1:])
    if parsed is None:
        print("Error: invalid arguments.")
        return 1

    lines = [line.rstrip("\n") for line in sys.stdin]
    if len(lines) > MAX_NR_OF_LINES:
        print("Error: input too large.")
        return 1

    quick_sort(lines, 0, len(lines) - 1, make_cmp(*parsed))
    for line in lines:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
