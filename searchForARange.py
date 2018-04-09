"""
Question:
    Given an array of integers sorted in ascending order, find the starting
    and ending position of a given target value.
    Your algorithm's runtime complexity must be in the order of O(log n).
    If the target is not found in the array, return [-1, -1].

    For example,
    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].
"""
# Binary Search


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) == 0:
        return [-1, -1]

    def binarySearch(start, end, target, left=True):
        if start == end:
            return start if nums[start] == target else -1
        if left:
            mid = (start + end) // 2
            if nums[mid] >= target:
                return binarySearch(start, mid, target, left)
            else:
                return binarySearch(mid + 1, end, target, left)
        else:
            mid = (start + end + 1) // 2
            if nums[mid] <= target:
                return binarySearch(mid, end, target, left)
            else:
                return binarySearch(start, mid - 1, target, left)

    left = binarySearch(0, len(nums) - 1, target, True)
    if left == -1:
        return [-1, -1]
    right = binarySearch(0, len(nums) - 1, target, False)
    return [left, right]


def extremeInsertionIndexIterative(nums, target, left=True):
    start, end = 0, len(nums)
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > target or (left and nums[mid] == target):
            end = mid
        else:
            start = mid + 1
    return start


def searchRangeIterative(nums, target):
    targetRange = [-1, -1]
    left = extremeInsertionIndexIterative(nums, target, True)
    if (left == len(nums) | | nums[left] != target):
        return targetRange
    targetRange[0] = left
    targetRange[1] = extremeInsertionIndexIterative(nums, target, False)
    return targetRange


if __name__ == '__main__':
    print(searchRange([5, 7, 7, 8, 8, 10], 8))
    print(searchRange([5, 7, 7, 8, 8, 10], 7))
    print(searchRange([5], -1))
