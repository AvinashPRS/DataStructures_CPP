"""Exercise 7-2: print arbitrary input in a sensible way: non-graphic (non
ASCII) bytes in octal (-o) or hexadecimal (-x), and fold long lines.

run: python3 print.py -x < test.txt
"""
import sys

MAX_LINE_LEN = 80
OFFSET = 10


def main(argv):
    if len(argv) != 2 or argv[1] not in ("-o", "-x"):
        print("Error: invalid arguments.")
        return 1
    octal = argv[1] == "-o"

    out = sys.stdout
    col_pos = 1
    for byte in sys.stdin.buffer.read():
        if byte <= 127:
            c = chr(byte)
            if c == "\n":
                c = " "
            out.write(c)
            col_pos += 1
        else:
            c = None
            text = ("\\%o" if octal else "\\%x") % byte
            out.write(text)
            col_pos += len(text) - 1

        if col_pos >= MAX_LINE_LEN - OFFSET and c in (" ", "\t"):
            col_pos = 1
            out.write("\n")
    out.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
