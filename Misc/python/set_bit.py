"""Set, reset and toggle a bit."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def set_bit(n, pos):
    return n | (1 << pos)


def reset_bit(n, pos):
    return n & ~(1 << pos) & 0xFFFFFFFF


def toggle_bit(n, pos):
    return n ^ (1 << pos)


def main():
    if set_bit(0xf0, 3) != 0xf8:
        handle_error()
    if reset_bit(0xf8, 3) != 0xf0:
        handle_error()
    if toggle_bit(0xf0, 7) != 0x70:
        handle_error()
    print("Test passed")


if __name__ == "__main__":
    main()
