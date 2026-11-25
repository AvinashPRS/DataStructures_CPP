"""Exercise 7-7: pattern finding program that takes input from a set of
named files or, if no files are named, from the standard input.

Options: -x print lines that don't match, -n print line numbers.

run: python3 find.py -n "Some people" file_1.txt file_2.txt
"""
import sys

program_name = sys.argv[0]
except_ = False
number = False


def parse_arg_list(argv):
    """Return the index of the pattern argument, or None on error."""
    global except_, number
    if len(argv) < 3:
        sys.stderr.write("Usage: %s [-xn]... PATTERN [FILE]...\n"
                         % program_name)
        return None

    pos = 1
    while pos < len(argv) and argv[pos].startswith("-"):
        for c in argv[pos][1:]:
            if c == "x":
                except_ = True
            elif c == "n":
                number = True
            else:
                sys.stderr.write("%s: illegal option %s.\n" % (program_name, c))
                return None
        pos += 1
    return pos


def find_pattern(pattern, file_p):
    for line_number, line in enumerate(file_p, 1):
        if (pattern in line) != except_:
            if number:
                sys.stdout.write("%d: " % line_number)
            sys.stdout.write(line)


def main(argv):
    pattern_arg_pos = parse_arg_list(argv)
    if pattern_arg_pos is None or pattern_arg_pos >= len(argv):
        return 1

    pattern = argv[pattern_arg_pos]
    file_names = argv[pattern_arg_pos + 1:]

    if file_names:
        for i, name in enumerate(file_names):
            try:
                with open(name, "r") as file_p:
                    print(name)
                    find_pattern(pattern, file_p)
            except OSError:
                sys.stderr.write("%s: can't open %s.\n" % (program_name, name))
                return 1
            if i < len(file_names) - 1:
                print()
    else:
        find_pattern(pattern, sys.stdin)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
