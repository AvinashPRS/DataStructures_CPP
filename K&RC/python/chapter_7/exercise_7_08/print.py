"""Exercise 7-8: print a set of files, starting each new one on a new page,
with a title and a running page count for each file.

run: python3 print.py ../exercise_7_07/file_1.txt ../exercise_7_07/file_2.txt
"""
import sys

LINES_PER_PAGE = 10
program_name = sys.argv[0]


def print_file(file_name):
    try:
        file_p = open(file_name, "r")
    except OSError:
        sys.stderr.write("%s: can't open %s.\n" % (program_name, file_name))
        sys.exit(1)

    with file_p:
        for line_number, line in enumerate(file_p, 1):
            if (line_number - 1) % LINES_PER_PAGE == 0:
                print("[%s]: page %d" % (file_name,
                                         line_number // LINES_PER_PAGE + 1))
            sys.stdout.write("%d: %s" % (line_number, line))


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Usage: %s [FILE]...\n" % argv[0])
        return 1

    files = argv[1:]
    for i, name in enumerate(files):
        print_file(name)
        if i != len(files) - 1:
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
