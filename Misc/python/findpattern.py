"""
Exercise 7-7. Modify the pattern finding program of Chapter 5 to take its
input from a set of named files or, if no files are named as arguments, from
the standard input. Should the file name be printed when a matching line is
found?

Answer: only when files are named as arguments.

Usage: findpattern.py [-xn] PATTERN [FILE...]
    -x  print lines that do NOT match
    -n  print line numbers

(The C file contains a duplicated, pasted-in copy of itself; this is the
single intended program. It also passed the *next* file name when printing
matches; here the current file name is printed.)
"""
import sys

MAXLEN = 1000


def load_file(prog, file_name):
    try:
        return open(file_name, "r")
    except OSError:
        print(f"{prog}: can't open {file_name}", file=sys.stderr)
        sys.exit(1)


def find_pattern(fp, file_name, pattern, except_, number):
    found = 0
    for lineno, line in enumerate(fp, start=1):
        if (pattern in line) != except_:
            out = ""
            if file_name:
                out += f"{file_name}:"
            if number:
                out += f"{lineno}:"
            sys.stdout.write(out + line)
            found += 1
    return found


def main(argv):
    prog = argv[0]
    except_ = number = False
    found = 0
    args = argv[1:]
    while args and args[0].startswith("-"):
        for c in args[0][1:]:
            if c == "x":
                except_ = True
            elif c == "n":
                number = True
            else:
                print(f"{prog}: illegal option {c}", file=sys.stderr)
                return -1
        args = args[1:]

    if not args:
        print(f"Usage: {prog} [-xn] PATTERN [FILE...]", file=sys.stderr)
    elif len(args) == 1:  # input from stdin
        found += find_pattern(sys.stdin, None, args[0], except_, number)
    else:                 # input from a set of files
        pattern = args[0]
        for name in args[1:]:
            with load_file(prog, name) as f:
                found += find_pattern(f, name, pattern, except_, number)
    return found


if __name__ == "__main__":
    sys.exit(min(main(sys.argv), 255))
