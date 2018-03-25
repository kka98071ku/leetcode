from collections import deque

"""
Question:
    You are given coins of different denominations and a total amount of money.
    Write a function to compute the number of combinations that make up that amount.
    You may assume that you have infinite number of each kind of coin.
"""

# Good, Knapsack, DP, search


def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int

    Analysis:
    This is a variation of the Knapsack problem where the solution space is
    d_0, d_1, ...., d_{n - 1} with d_i >= 0 for coin c_0, ..., c_{n - 1}

    Looking from a search perspective, here we could set state (i, j) as the
    solution to the sub-problem "how many different ways to pick from coin 0, 1,
    ..., i that sum up to j"

    dp[i][j] = dp[i - 1][j]                     # does not pick coins[i] at all
             + dp[i - 1][j - c_i]               # pick one coins[i]
             + dp[i - 1][j - c_i * 2]           # pick two coins[i]
             + ...
             = dp[i - 1][j] + dp[i][j - c_i]    # we could arrive at this step directly

    Notice that we only relies on dp[i - 1][j] from the last step, so we only need
    to keep one row and overwrite it in place.

    The boundary could be dp[_][0] = 1, dp[_][1: amount + 1] = [0, ...., 0]
    The final solution is then dp[_][amount]
    """
    dp = [1] + [0 for _ in range(amount)]
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]
    return dp[-1]


if __name__ == '__main__':
    print(change(5, [1, 2, 5]))
    print(change(3, [2]))
    print(change(10, [10]))
    print(change(500, [1, 2, 5]))
    print(change(5000, [3, 5, 7, 8, 9, 10, 11]))
