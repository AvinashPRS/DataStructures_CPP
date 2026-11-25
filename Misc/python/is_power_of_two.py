"""Check whether an unsigned integer is a power of two."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def is_power_of_two(x):
    return x != 0 and (x & (x - 1)) == 0


def main():
    for x in (0, 10, 15):          # not powers of 2
        if is_power_of_two(x):
            handle_error()
    for x in (1, 2, 4, 0x80000000):  # powers of 2
        if not is_power_of_two(x):
            handle_error()
    print("Test passed")


if __name__ == "__main__":
    main()
