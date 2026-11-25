"""Minimum number of coins needed to make an amount."""
import sys

MAX_INT_VALUE = 0x7FFFFFFF


def handle_error():
    print("Error occured ")
    sys.exit(1)


def find_min_coins(denom, final_amount):
    """
    denom: list having the coin denominations. Should have atleast 1 element
    final_amount: amount for which change has to be obtained
    Return value: Minimum number of coins needed to represent final_amount
    """
    # min_num_coins[amt] stores the minimum number of coins for an amount
    min_num_coins = [0] * (final_amount + 1)
    # chosen_denom[amt] stores the coin denomination chosen for an amount
    chosen_denom = [0] * (final_amount + 1)

    for cur_amt in range(1, final_amount + 1):
        min_num_coins[cur_amt] = MAX_INT_VALUE
        for d in denom:
            if d <= cur_amt:
                smaller_amt = cur_amt - d
                if 1 + min_num_coins[smaller_amt] < min_num_coins[cur_amt]:
                    min_num_coins[cur_amt] = 1 + min_num_coins[smaller_amt]
                    chosen_denom[cur_amt] = d

    result = min_num_coins[final_amount]
    print(f"Minimum number of coins = {result}")

    # print the chosen denominations to get the final amount
    cur_amt = final_amount
    while cur_amt > 0:
        print(chosen_denom[cur_amt], end=" ")
        cur_amt -= chosen_denom[cur_amt]
    print(f" = {final_amount}")

    return result


def print_array(a):
    print(" ".join(str(x) for x in a) + " ")


def run_test(denom, total_amount, expected):
    print("Coin denominations : ", end="")
    print_array(denom)
    print(f"Total amount needed = {total_amount}")

    if find_min_coins(denom, total_amount) != expected:
        handle_error()

    print("_____________________________________________")


if __name__ == "__main__":
    run_test([1, 2, 3, 4, 5], 13, 3)
    run_test([1, 2, 3, 4], 17, 5)
    run_test([1, 5, 10, 25, 50], 30, 2)
    run_test([1, 3, 4, 5], 7, 2)
    print("Test passed")
