"""Exercise 5-12: entab accepting the shorthand -m +n meaning tab stops every
n columns starting at column m (or a list of tab stops).

run: python3 entab.py 4 8 12 16 < file_spaces.txt > file_tabs.txt
"""
import sys

DEFAULT_TAB_LENGTH = 8


def is_arg_list_valid(args):
    for i, arg in enumerate(args):
        if arg[:1] in ("-", "+"):
            if len(args) > 2 or not arg[1:].isdigit():
                return False
            continue
        if not arg.isdigit() or (i > 0 and int(args[i - 1]) > int(arg)):
            return False
    return True


def main(argv):
    args = argv[1:]
    if not is_arg_list_valid(args):
        print("Error: invalid arguments.\n")
        return 1

    custom_tab_stop = 0
    custom_line_pos_start = 0
    tab_stops = []
    for arg in args:
        if arg[0] == "-":
            custom_line_pos_start = int(arg[1:])
        elif arg[0] == "+":
            custom_tab_stop = int(arg[1:])
        else:
            tab_stops.append(int(arg))

    out = sys.stdout
    arg_pos = 0
    line_pos = 0
    tab_stop = DEFAULT_TAB_LENGTH
    nr_of_spaces = 0

    for c in sys.stdin.read():
        line_pos += 1

        if c == " ":
            nr_of_spaces += 1

            if arg_pos < len(tab_stops):
                tab_stop = tab_stops[arg_pos]
            elif custom_tab_stop:
                tab_stop = custom_tab_stop
            elif tab_stops:
                tab_stop = 1

            if ((not custom_line_pos_start and line_pos % tab_stop == 0
                 and nr_of_spaces > 1)
                    or (custom_line_pos_start and nr_of_spaces == tab_stop)
                    or line_pos <= custom_line_pos_start):
                out.write("\t")
                if arg_pos < len(tab_stops):
                    arg_pos += 1
                nr_of_spaces = 0
        else:
            out.write(" " * nr_of_spaces)
            nr_of_spaces = 0

            if c == "\n":
                arg_pos = 0
                line_pos = 0

            out.write(c)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# NOTE: The current program works in a similar fashion as unexpand.
