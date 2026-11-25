"""Find the maximum profit from buying and then selling a stock once."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMENTS = 10
MAX_VALUE = 100


def handle_error():
    print("Error occured")
    sys.exit(1)


def find_max_profit(stock_price):
    """
    stock_price: list of stock price values
    Return value: maximum profit possible
    """
    max_profit = 0
    if len(stock_price) <= 1:
        return max_profit

    min_stock_price = stock_price[0]

    for price in stock_price[1:]:
        cur_profit = price - min_stock_price
        if cur_profit > max_profit:
            max_profit = cur_profit
        if price < min_stock_price:
            min_stock_price = price

    return max_profit


def find_brute_force_max_profit(stock_price):
    max_profit = 0
    n = len(stock_price)
    if n <= 1:
        return max_profit

    for i in range(n - 1):
        for j in range(i + 1, n):
            if stock_price[j] > stock_price[i]:
                cur_profit = stock_price[j] - stock_price[i]
                if cur_profit > max_profit:
                    max_profit = cur_profit

    return max_profit


def print_array(a):
    print(" ".join(str(x) for x in a) + " ")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        # Randomly pick the number of elements
        num_elements = 1 + random.randrange(MAX_NUM_ELEMENTS)

        # Add random share values to the array
        a = [random.randrange(MAX_VALUE) for _ in range(num_elements)]

        print("Input : ", end="")
        print_array(a)

        # Find the best profit possible
        result = find_max_profit(a)
        print(f"Maximum profit = {result}")

        # Find the best profit using the brute force approach
        brute_force_result = find_brute_force_max_profit(a)

        # Both results should match
        if result != brute_force_result:
            handle_error()

        print("__________________________________________________")

    print("Test passed")
