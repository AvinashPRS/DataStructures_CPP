"""Exercise 8-1: cat rewritten with the low level system calls read, write,
open and close (os module) instead of the standard library equivalents."""
import os
import sys

BUFFER_SIZE = 1024


def error(fmt, *args):
    sys.stderr.write("Error: " + (fmt % args) + "\n")
    sys.exit(1)


def copy_file(src, dst):
    while True:
        buffer = os.read(src, BUFFER_SIZE)
        if not buffer:
            break
        os.write(dst, buffer)


def main(argv):
    if len(argv) == 1:
        copy_file(0, 1)
    else:
        for name in argv[1:]:
            try:
                fd = os.open(name, os.O_RDONLY)
            except OSError:
                error("Error: could not open the file %s.", name)
            copy_file(fd, 1)
            os.close(fd)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
