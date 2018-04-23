"""
Question:
    https://leetcode.com/problems/minimum-window-substring/description/
    Given a string S and a string T, find the minimum window in S which
    will contain all the characters in T in complexity O(n).

    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"
"""

# GOOD, sliding window

import collections


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if t == '':
        return ''

    # the key point of the problem is to figure out what
    # state variables are necessary.
    need, missingCount = collections.Counter(t), len(t)
    left, right = 0, 0
    result = [0, len(s)]

    for right, char in enumerate(s):
        if char in need:
            # This step is pretty smart
            missingCount -= (need[char] > 0)
            need[char] -= 1
            if not missingCount:
                while left <= right:
                    key = s[left]
                    if not key in need:
                        left += 1
                    elif key in need and need[key] < 0:
                        need[key] += 1
                        left += 1
                    else:
                        break
                # update result
                if right - left < result[1] - result[0]:
                    result = [left, right]

    return '' if result[1] == len(s) else s[result[0]: result[1] + 1]


if __name__ == '__main__':
    print(minWindow('ADOBECODEBANC', 'ABC'))
    print(minWindow('a', 'a'))
    print(minWindow('a', 'aa'))
    print(minWindow('aa', 'aa'))
    print(minWindow('aab', 'aab'))
    print(minWindow('coobdafceeaxab', 'abc'))
