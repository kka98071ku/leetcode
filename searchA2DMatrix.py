"""
Question:
    [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    https://leetcode.com/problems/search-a-2d-matrix/description/

Discussion:
    We could also flatten the matrix into a sorted array and do binary search directly.
    However, it might suffer from large integer multiplication for m * n.....
"""

# GOOD, Binary Search


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    # find the one row above the targeted row, hens `high = len(matrix)`
    low, high = 0, len(matrix)
    while low < high:
        mid = (low + high) // 2
        if matrix[mid][0] == target:
            return True
        if matrix[mid][0] > target:
            high = mid
        else:
            low = mid + 1
    # all rows are too big
    if low == 0 or matrix[low - 1][0] > target:
        return False
    row = matrix[low - 1]

    # do regular binary search, hens `right = len(row) - 1`
    left, right = 0, len(row) - 1
    while left < right:
        mid = (left + right) // 2
        if row[mid] == target:
            return True
        if row[mid] > target:
            right = mid
        else:
            left = mid + 1
    return row[left] == target


if __name__ == '__main__':
    # print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))
    print(searchMatrix([[1, 3]], 3))
