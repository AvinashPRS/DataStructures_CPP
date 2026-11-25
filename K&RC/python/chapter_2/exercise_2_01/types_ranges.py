"""Exercise 2-1: determine the ranges of char, short, int and long variables.

Python integers have arbitrary precision, so the ranges of the corresponding
C types are computed from their sizes (as reported by ctypes) instead.
"""
import ctypes

CHAR_BIT = 8


def signed_range(ctype):
    bits = ctypes.sizeof(ctype) * CHAR_BIT
    return -(1 << (bits - 1)), (1 << (bits - 1)) - 1


def unsigned_max(ctype):
    return (1 << (ctypes.sizeof(ctype) * CHAR_BIT)) - 1


def section(title, name, signed_t, unsigned_t):
    smin, smax = signed_range(signed_t)
    print(title)
    if name == "char":
        print("bits: %d" % CHAR_BIT)
        print("unsigned char max: %d" % unsigned_max(unsigned_t))
        print("signed char min: %d" % smin)
        print("signed char max: %d" % smax)
    else:
        print("unsigned %s max: %d" % (name, unsigned_max(unsigned_t)))
        print("signed %s min: %d" % (name, smin))
        print("signed %s max: %d" % (name, smax))
    print()


def main():
    section("#################### CHAR #####################", "char",
            ctypes.c_byte, ctypes.c_ubyte)
    section("##################### INT #####################", "int",
            ctypes.c_int, ctypes.c_uint)
    section("################## SHORT INT ##################", "short int",
            ctypes.c_short, ctypes.c_ushort)
    section("################## LONG INT ###################", "long int",
            ctypes.c_long, ctypes.c_ulong)
    section("################ LONG LONG INT #################",
            "long long int", ctypes.c_longlong, ctypes.c_ulonglong)


if __name__ == "__main__":
    main()

# NOTE: In C the limits.h header contains the machine dependent constants for
# type sizes. Python's ints never overflow, so ctypes is used to query them.
