"""
Question:
    Find the contiguous subarray within an array (containing at
    least one number) which has the largest sum.
    https://leetcode.com/problems/maximum-subarray/description/

    wiki:
    https://en.wikipedia.org/wiki/Maximum_subarray_problem

    followup:

"""
import functools


def maxSubArrayDP(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxEndingHere = maxSoFar = nums[0]
    for i in range(1, len(nums)):
        maxEndingHere = max(maxEndingHere + nums[i], nums[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar


def maxDivideAndConquer(nums):
    # compute the cumulative sum
    sums = []
    for num in nums:
        sums.append(num if len(sums) == 0 else sums[-1] + num)

    def loop(l, r):
        if l == r:
            return (nums[l], sums[l], sums[l])
        else:
            mid = (l + r) // 2
            resLeft, minPrefixLeft, maxPrefixLeft = loop(l, mid)
            resRight,  minPrefixRight, maxPrefixRight = loop(mid + 1, r)
            minPrefix = min(minPrefixLeft, minPrefixRight)
            maxPrefix = max(maxPrefixLeft, maxPrefixRight)
            # Solution overlapping both the left and the right part
            # can be computed as follows.
            resCenter = maxPrefixRight - minPrefixLeft
            res = max(resLeft, resCenter, resRight, maxPrefix)
            return (res, minPrefix, maxPrefix)
    res, _, _ = loop(0, len(nums) - 1)
    return res


if __name__ == '__main__':
    print(maxDivideAndConquer([1, 2]))
