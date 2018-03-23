from collections import deque

# GOOD, search, BFS, DP


def coinChangeDP(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int

    f(amount) = min(f(amount - coins[0]), f(amount - coins[1]), ...) + 1 or -1
    errrr, memoized version hits the max stack limit and the iterative version
    exceeds the time limit.
    """
    if amount == 0:
        return 0
    table = []
    maxInt = amount + 1
    # assert(amount >= 0)
    for target in range(1, amount + 1):
        minCount = maxInt
        for coin in coins:
            remain = target - coin
            if remain == 0:
                minCount = 1
            elif remain > 0:
                minCount = min(minCount, table[remain - 1] + 1)
        table.append(minCount)
    return -1 if table[-1] > amount else table[-1]


def coinChange(coins, amount):
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
