"""
Given coins of denominations 1, 5, 10, 25, 50, 100. Find the minimum no. of coins for making change
for a given amount.

Input: list of denominations, amount
Output: int

Solution:
    Using greedy approach select the highest possible denomination every time.
    TC: O(n)
"""


def min_change_cmb(coins, amount):
    """Finds the number of coins for getting change in min number of coins."""
    coin_num = 0

    # traverse the denominations from largest to smallest
    for coin in reversed(coins):
        if amount == 0:
            break

        coin_num += amount // coin
        amount %= coin

    return coin_num


if __name__ == "__main__":
    coins = [1, 5, 10, 25, 50, 100]
    amount = 40
    print(min_change_cmb(coins, amount))
