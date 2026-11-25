import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def print_array(a):
    print(" ".join(str(x) for x in a) + " ")


def find_odd_occurence(a):
    """
    a: list of numbers, where one element occurs odd number of times
         while remaining elements occur even number of times
    Return value: element that occurs odd number of times
    """
    # XOR all the elements
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


if __name__ == "__main__":
    test()

    print("Test passed ")
