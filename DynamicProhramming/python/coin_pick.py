"""
Given a list of ints, where each entry represents the value of a coin. Two players
take turns picking a coin from either the front or the back. The player with the
largest total wins. Find the largest value the first player can collect, assuming
the second player also plays optimally. A player cannot skip a turn.

Solution:
    Player 1 wants to maximize their collected value, while Player 2 also plays
    optimally and therefore tries to leave Player 1 with the worst remaining situation.
    (Optimal Strategy for a Game problem, recursion + memoization.)

    TC: O(n^2), n: no. of coins
    SC: O(n^2)
"""


def maximize_coin_value_helper(coins, a, b, max_value):
    # if there are no coins left
    if a > b:
        return 0

    # every time player one can pick a coin either from front or back
    if max_value[a][b] == 0:
        # player 1 selects the front coin; player 2 then picks so player 1 gets the min
        front_coin_selected = coins[a] + min(
            maximize_coin_value_helper(coins, a + 1, b - 1, max_value),  # player 2 selects back coin
            maximize_coin_value_helper(coins, a + 2, b, max_value))      # player 2 selects front coin

        # player 1 selects the back coin
        back_coin_selected = coins[b] + min(
            maximize_coin_value_helper(coins, a + 1, b - 1, max_value),  # player 2 selects front coin
            maximize_coin_value_helper(coins, a, b - 2, max_value))      # player 2 selects back coin

        # player 1 will select the max of above
        max_value[a][b] = max(front_coin_selected, back_coin_selected)
    return max_value[a][b]


def maximize_coin_value(coins):
    """finds the maximum value that can be gained if the player starts first"""
    # (a, b) stores the max value for the current range of coins
    max_value = [[0] * len(coins) for _ in range(len(coins))]
    return maximize_coin_value_helper(coins, 0, len(coins) - 1, max_value)


if __name__ == "__main__":
    coins = [10, 25, 5, 1, 10, 5]
    print(maximize_coin_value(coins))
