"""
Question:
    https://leetcode.com/problems/find-k-closest-elements/description/
"""

# GOOD, Binary Search


def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    low, high = 0, len(arr) - k
    while low < high:
        mid = (low + high) // 2
        if x - arr[mid] > arr[mid + k] - x:  # important!
            low = mid + 1
        else:
            high = mid
    return arr[low: low + k]


if __name__ == '__main__':
    print(findClosestElements([1, 2, 3, 4, 5], 4, -1))
