"""
Question:
    https://leetcode.com/problems/dungeon-game/description/

start from the last cell:
    dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
"""
# DP


def calculateMinimumHP(dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    m = len(dungeon)
    n = len(dungeon[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[-1][-1] = max(1, -dungeon[-1][-1] + 1)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                continue
            candidates = []
            if i < m - 1:
                candidates.append(dp[i + 1][j])
            if j < n - 1:
                candidates.append(dp[i][j + 1])
            dp[i][j] = max(1, min(candidates) - dungeon[i][j])
    return dp[0][0]


if __name__ == "__main__":
    print(calculateMinimumHP([[-3, 5]]))
    print(calculateMinimumHP([[-3], [-7]]))
    print(calculateMinimumHP([[2, 1], [1, -1]]))
    print(calculateMinimumHP([[0, -3]]))
