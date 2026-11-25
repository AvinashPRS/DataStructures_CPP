import sys

MASK32 = 0xFFFFFFFF


def handle_error():
    print("Error occured ")
    sys.exit(1)


def set_bit(n, pos):
    return (n | (1 << pos)) & MASK32


def reset_bit(n, pos):
    return (n & ~(1 << pos)) & MASK32


def toggle_bit(n, pos):
    return (n ^ (1 << pos)) & MASK32


if __name__ == "__main__":
    if set_bit(0xF0, 3) != 0xF8:
        handle_error()

    if reset_bit(0xF8, 3) != 0xF0:
        handle_error()

    if toggle_bit(0xF0, 7) != 0x70:
        handle_error()

    print("Test passed")
