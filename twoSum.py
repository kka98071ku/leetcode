def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {};
    for idx, val in enumerate(nums):
        residue = target - val
        if residue in seen:
            return [seen[residue], idx]
        else:
            seen[val] = idx
    return [];

if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))
