"""
Question:
    https://leetcode.com/problems/wildcard-matching/description/

    This is just the interval scheduling problem
    https://en.wikipedia.org/wiki/Interval_scheduling
"""


def findLongestChain(pairs):
    """
    :type pairs: List[List[int]]
    :rtype: int
    """
    if len(pairs) == 0:
        return 0
    # sort by the "ending time"
    pairs = sorted(pairs, key=lambda x: x[1])
    result = [pairs[0]]
    for i in range(1, len(pairs)):
        # if the current interval does not have overlap with last picked interval,
        # add it to the result
        if pairs[i][0] > result[-1][1]:
            result.append(pairs[i])
    return len(result)


if __name__ == '__main__':
    print(findLongestChain([[4, 6], [4, 5], [3, 4]]))
