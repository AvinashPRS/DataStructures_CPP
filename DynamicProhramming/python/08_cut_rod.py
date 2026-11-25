"""Rod cutting: maximize the value obtained by cutting a rod into pieces."""
import random
import sys

MAX_NUM_TESTS = 100
MAX_LENGTH = 10
MAX_VALUE = 10


def handle_error():
    print("Error occured ")
    sys.exit(1)


def print_pieces(first_cut, total_length):
    """Helper function for printing out the sizes of the individual pieces"""
    print("The rod piece lengths are : ", end="")
    cur_length = total_length
    while cur_length > 0 and first_cut[cur_length] > 0:
        print(first_cut[cur_length], end=" ")
        cur_length -= first_cut[cur_length]
    print()


def cut_rod(price, total_length):
    """
    price: price[i] gives the price of a rod of length i. price[0] is 0
    total_length: the total length of the rod given to us. Should be >= 1
    Return value: the best value that can be fetched from the rod
    """
    best_value = [0] * (total_length + 1)

    # first_cut[i] indicates the length of the first piece when we cut the rod
    # of length i. Needed to print out where we should cut to get the best value
    first_cut = [0] * (total_length + 1)

    for cur_length in range(1, total_length + 1):
        # The length of the first piece after the cut can range from 1 to cur_length
        for i in range(1, cur_length + 1):
            if price[i] + best_value[cur_length - i] > best_value[cur_length]:
                best_value[cur_length] = price[i] + best_value[cur_length - i]
                first_cut[cur_length] = i

    print_pieces(first_cut, total_length)
    return best_value[total_length]


def cut_rod_recursive(price, cur_length):
    if cur_length <= 0:
        return 0

    best_value = price[cur_length]
    for i in range(1, cur_length):
        best_value = max(best_value, price[i] + cut_rod_recursive(price, cur_length - i))
    return best_value


def print_array(price):
    print("Length: " + " ".join(str(i) for i in range(len(price))) + " ")
    print("Price : " + " ".join(str(p) for p in price) + " ")


def test():
    # Randomly decide the length and fill in the prices
    length = 1 + random.randrange(MAX_LENGTH)
    price = [0] + [random.randrange(MAX_VALUE) for _ in range(length)]

    print_array(price)

    # Find the result using an efficient technique
    result = cut_rod(price, length)
    print(f"Max value = {result} ")

    # Find the result using the recursive technique; the two results should match
    if result != cut_rod_recursive(price, length):
        handle_error()

    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
