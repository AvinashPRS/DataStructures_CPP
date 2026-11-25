"""Exercise 7-3: minprintf handling more of the printf conversions."""
import ctypes
import sys


def minprintf(fmt, *args):
    out = []
    args = list(args)
    i = 0
    while i < len(fmt):
        ch = fmt[i]
        if ch != "%":
            out.append(ch)
            i += 1
            continue

        i += 1
        conv = fmt[i] if i < len(fmt) else ""
        if conv in ("d", "i"):
            out.append("%d" % args.pop(0))
        elif conv == "o":
            out.append("%o" % args.pop(0))
        elif conv in ("x", "X"):
            out.append("%x" % args.pop(0))
        elif conv == "u":
            out.append("%d" % (args.pop(0) & 0xFFFFFFFF))  # unsigned int
        elif conv == "c":
            out.append(chr(args.pop(0)))
        elif conv == "s":
            out.append(str(args.pop(0)))
        elif conv == "f":
            out.append("%f" % args.pop(0))
        elif conv in ("e", "E"):
            out.append("%e" % args.pop(0))
        elif conv in ("g", "G"):
            out.append("%g" % args.pop(0))
        elif conv == "p":
            out.append(hex(args.pop(0)))
        else:
            out.append(conv)
        i += 1

    sys.stdout.write("".join(out))


def main():
    a = ctypes.c_int()
    minprintf("Let's print %d, %i, %o, %x, %X, %u, %c, %e, %E, %g, %G, %f, %p, "
              "and %s.\n",
              2, 3, 8, 16, 16, -1, 97, 0.0025, 0.0023, 0.0025, 0.0023,
              3.14159, ctypes.addressof(a), "hello, world")


if __name__ == "__main__":
    main()
