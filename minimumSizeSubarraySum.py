"""
Question:
    Given an array of n positive integers and a positive integer s, find the
    minimal length of a contiguous subarray of which the sum ≥ s. If there
    isn't one, return 0 instead.

    For example, given the array [2,3,1,2,4,3] and s = 7,
    the subarray [4,3] has the minimal length under the problem constraint.
"""
# GOOD, Sliding Window, Binary Search gives a (worse) O(Nlog(N)) solution


def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    summation = 0
    minimalLength = 0

    left, right = 0, 0
    while right < len(nums):
        summation += nums[right]
        if summation >= s:
            if minimalLength == 0:
                minimalLength = right - left + 1
            while summation >= s:
                summation -= nums[left]
                left += 1
            minimalLength = min(minimalLength, right - left + 2)

        right += 1
    return minimalLength


if __name__ == '__main__':
    print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2)
    print(minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 2)
