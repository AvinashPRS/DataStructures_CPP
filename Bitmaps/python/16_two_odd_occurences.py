import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def print_array(a):
    print(" ".join(str(x) for x in a) + " ")


def find_odd_occurences(a):
    """
    a: input list where 2 elements occur odd number of times and the remaining
        occur even number of times
    Return value: the two numbers that occur odd number of times
    """
    all_xor = 0
    for x in a:
        all_xor ^= x

    # Find the first bit in the XOR result that is set to 1. The two odd
    # occuring numbers will differ at this bit position. So if difference
    # is at bit position 3, then mask will be ...00001000
    mask = all_xor & ~(all_xor - 1)

    # Separate out values in list a such that, values that have a 1 at the
    # different bit will be XORed with result[0] and values that have a 0
    # at the different bit will be XORed with result[1]
    result = [0, 0]
    for x in a:
        if x & mask:
            result[0] ^= x
        else:
            result[1] ^= x

    # result[0] and result[1] now contain the two numbers that
    # occur odd number of times
    return result


def test(a, expected_result1, expected_result2):
    print_array(a)

    result = find_odd_occurences(a)

    print(f"The odd occuring elements are {result[0]} and {result[1]}")

    if min(result) != min(expected_result1, expected_result2):
        handle_error()

    if max(result) != max(expected_result1, expected_result2):
        handle_error()

    print("_____________________________________________")


if __name__ == "__main__":
    test([1, 2, 3, 2, 4, 3], 1, 4)

    print("Test passed")
