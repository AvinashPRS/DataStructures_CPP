"""Exercise 7-6: compare two files, printing the first line where they
differ.

run: python3 compare.py file_1.txt file_2.txt
"""
import sys


def main(argv):
    if len(argv) != 3:
        sys.stderr.write("Error: invalid arguments.\n")
        return 1

    program_name = argv[0]
    files = []
    for name in argv[1:]:
        try:
            files.append(open(name, "r"))
        except OSError:
            sys.stderr.write("%s: can't open %s.\n" % (program_name, name))
            return 1

    with files[0] as file_1, files[1] as file_2:
        for line_number, (line_1, line_2) in enumerate(zip(file_1, file_2), 1):
            if line_1 != line_2:
                sys.stdout.write("%s [%d]: %s" % (argv[1], line_number, line_1))
                sys.stdout.write("%s [%d]: %s" % (argv[2], line_number, line_2))
                break
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
