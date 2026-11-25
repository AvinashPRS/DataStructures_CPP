"""
Exercise 7-6. Write a program to compare two files, printing the first line
where they differ.
"""
import sys


class File:
    def __init__(self, name, fptr):
        self.name = name      # file name
        self.fptr = fptr      # file object
        self.line = ""        # currently read line
        self.lineno = 0       # number of read lines
        self.eof = False


def openfile(prog, filename):
    try:
        fptr = open(filename, "r")
    except OSError:
        print(f"{prog}: can't open {filename}", file=sys.stderr)
        sys.exit(1)
    return File(filename, fptr)


def read_line(f):
    line = f.fptr.readline()
    if line:
        f.line = line
        f.lineno += 1
    else:
        f.eof = True


def comparefiles(f1, f2):
    while True:
        read_line(f1)
        read_line(f2)
        if not f1.eof and not f2.eof and f1.line != f2.line:
            break  # lines differ
        if f1.eof or f2.eof:
            break
    if not f1.eof:
        sys.stdout.write(f"\n{f1.name}:{f1.lineno}: {f1.line}")
    if not f2.eof:
        sys.stdout.write(f"\n{f2.name}:{f2.lineno}: {f2.line}")


def main(argv):
    prog = argv[0]
    if len(argv) != 3:
        print(f"Usage: {prog} <file1> <file2>", file=sys.stderr)
        sys.exit(1)
    file_1 = openfile(prog, argv[1])
    file_2 = openfile(prog, argv[2])
    comparefiles(file_1, file_2)
    file_1.fptr.close()
    file_2.fptr.close()


if __name__ == "__main__":
    main(sys.argv)
