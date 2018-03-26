"""
Question:
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    Note: The solution set must not contain duplicate triplets.
    For example, given array S = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
"""

# Common question


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    results = []
    if len(nums) == 0:
        return results
    lastStartNumber = None
    for i, start in enumerate(nums):
        if start == lastStartNumber:
            continue
        # solve problem for two sum
        left, right = i + 1, len(nums) - 1
        lastLeftSol, lastRightSol = None, None
        while left < right:
            twoSum = nums[left] + nums[right]
            if twoSum == -start and \
                    not (lastLeftSol == nums[left] and lastRightSol == nums[right]):
                results.append([start, nums[left], nums[right]])
                lastLeftSol, lastRightSol = nums[left], nums[right]
            if twoSum >= -start:
                right -= 1
            if twoSum <= -start:
                left += 1
        lastStartNumber = start
    return results


if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([-1]))
    print(threeSum([-2, 0, 0, 2, 2]))
