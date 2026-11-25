"""Find the element that occurs an odd number of times (XOR trick)."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def print_array(a):
    print("".join(f"{x} " for x in a))


def find_odd_occurence(a):
    """XOR of all elements: pairs cancel out, leaving the odd one."""
    result = 0
    for x in a:
        result ^= x
    return result


def test():
    a = [1, 8, 4, 8, 2, 1, 4]
    print("Input : ", end="")
    print_array(a)
    result = find_odd_occurence(a)
    print(f"Element that occurs odd number of times = {result}")
    if result != 2:
        handle_error()


def main():
    test()
    print("Test passed ")


if __name__ == "__main__":
    main()
