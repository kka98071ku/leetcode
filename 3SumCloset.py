"""
Question:
    Given an array S of n integers, find three integers in S such that the sum is closest
    to a given number, target. Return the sum of the three integers. You may assume that
    each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    delta = None
    nums.sort()
    lastStartNumber = None
    for i, start in enumerate(nums):
        if start == lastStartNumber:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            _delta = nums[left] + nums[right] + start - target
            if _delta == 0:
                return target
            if _delta < 0:
                left += 1
            else:
                right -= 1

            if delta == None or abs(delta) > abs(_delta):
                delta = _delta
        lastStartNumber = start
    return target + delta


if __name__ == '__main__':
    # print(threeSumClosest([-1, 2, 1, -4], 1))
    print(threeSumClosest([1, 1, 1, 0], -100))
