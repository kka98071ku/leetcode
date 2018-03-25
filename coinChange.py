from collections import deque

"""
Question:
    You are given coins of different denominations and a total amount of money amount.
    Write a function to compute the fewest number of coins that you need to make up that
    amount. If that amount of money cannot be made up by any combination of the coins,
    return -1.

Analysis:
    A variation of Knapsack problem.... We could set the state as (i, j) to represent the
    solution to the sub-problem "Given coin c_0, ..., c_i and target amount j, what's the
    fewest number of coins to make up the amount"

    dp[i][j] = min( dp[i - 1][j],          # does not pick coin[i]
                    dp[i][j - c_i] + 1 )   # picks at least one coin[i]

    The boundary could be dp[_][0] = 0, dp[_][1: amount + 1] = INFINITY
"""

# GOOD, search, BFS, DP, Knapsack


def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    maxInt = amount + 1
    dp = [0] + [maxInt for _ in range(amount)]

    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return -1 if dp[-1] == maxInt else dp[-1]


def _coinChange(coins, amount):
    """
    Convert this to a BFS search problem saves more space and faster
    """
    if amount == 0:
        return 0
    queue = deque([(amount, 0)])
    visited = [False for _ in range(amount + 1)]
    visited[0] = True
    while len(queue) > 0:
        (target, count) = queue.popleft()
        for coin in coins:
            if target == coin:
                return count + 1
            elif target > coin and visited[target - coin] == False:
                visited[target - coin] = True
                queue.append((target - coin, count + 1))
    return -1


if __name__ == "__main__":
    print(coinChange([1, 2, 5], 11))
    print(coinChange([2], 3))
    print(coinChange([1], 0))
    print(coinChange([1], 1))
    print(coinChange([3, 7, 405, 436], 8839))
    print(coinChange([84, 457, 478, 309, 350, 349, 422, 469, 100, 432, 188], 6993))
