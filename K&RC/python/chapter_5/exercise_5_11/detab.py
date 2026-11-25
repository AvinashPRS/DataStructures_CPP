"""Exercise 5-11: detab accepting a list of tab stops as arguments.

run: python3 detab.py 4 8 12 16 < file_tabs.txt > file_spaces.txt
"""
import sys

DEFAULT_TAB_LENGTH = 8


def is_tab_stop_arg_list_valid(args):
    for i, arg in enumerate(args):
        if not arg.isdigit() or (i > 0 and int(args[i - 1]) > int(arg)):
            return False
    return True


def main(argv):
    args = argv[1:]
    if not is_tab_stop_arg_list_valid(args):
        print("Error: invalid tab stop list.\n")
        return 1

    out = sys.stdout
    arg_pos = 0
    line_pos = 0
    tab_stop = DEFAULT_TAB_LENGTH
    nr_of_custom_tab_stops = len(args)

    for c in sys.stdin.read():
        if c == "\t":
            if nr_of_custom_tab_stops:
                tab_stop = int(args[arg_pos])
                arg_pos += 1
                nr_of_custom_tab_stops -= 1
            elif args:
                tab_stop = 1

            nr_of_spaces = tab_stop - line_pos % tab_stop
            out.write(" " * nr_of_spaces)
            line_pos += nr_of_spaces
        else:
            out.write(c)
            line_pos += 1

            if c == "\n":
                arg_pos = 0
                line_pos = 0
                nr_of_custom_tab_stops = len(args)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# NOTE: The current program works in a similar fashion as expand.
