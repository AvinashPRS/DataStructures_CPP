"""Exercise 5-13: tail -n prints the last n lines of its input (default 10).

run: python3 tail.py -5 < file_in.txt
"""
import sys

MAX_NR_OF_LINES = 5000
DEFAULT_NR_OF_LINES_TO_PRINT = 10


def is_arg_list_valid(args):
    if len(args) > 1:
        return False
    if len(args) == 1 and (args[0][:1] != "-" or not args[0][1:].isdigit()):
        return False
    return True


def read_lines(max_nr_of_lines):
    lines = []
    for line in sys.stdin:
        if len(lines) >= max_nr_of_lines:
            return None
        lines.append(line.rstrip("\n"))
    return lines


def write_lines(lines, nr_of_lines_to_print):
    start_pos = max(0, len(lines) - nr_of_lines_to_print)
    for line in lines[start_pos:]:
        print(line)


def main(argv):
    args = argv[1:]
    if not is_arg_list_valid(args):
        print("Error: invalid arguments.\n")
        return 1

    nr_of_lines_to_print = DEFAULT_NR_OF_LINES_TO_PRINT
    if len(args) == 1:
        nr_of_lines_to_print = int(args[0][1:])

    lines = read_lines(MAX_NR_OF_LINES)
    if lines is None:
        print("Error: input too large.\n")
        return 1

    write_lines(lines, nr_of_lines_to_print)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
