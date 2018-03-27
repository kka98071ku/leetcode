"""
Question:
    A robot is located at the top-left corner of a m x n grid
    (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time.
    The robot is trying to reach the bottom-right corner of the grid
    (marked 'Finish' in the diagram below).

    How many possible unique paths are there?
"""

# DP


def uniquePathsSlightlyOptimized(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int

    The iteration below shows that we only need the n-th element
    from the previous step. Hens there is no point of having two rows --
    we could overwrite the previous row.
    """
    row = [1 for _ in range(n)]
    for i in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]


def uniquePathsDumbDP(m, n):
    """
    unique(m, n) = unique(m - 1, n) + unique(m, n - 1)
    """
    row = [1 for _ in range(n)]
    for i in range(1, m):
        currentRow = [1]
        for j in range(1, n):
            currentRow.append(row[j] + currentRow[-1])
        row = currentRow
    return row[-1]
