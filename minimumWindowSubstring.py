"""
Question:
    https://leetcode.com/problems/minimum-window-substring/description/
    Given a string S and a string T, find the minimum window in S which
    will contain all the characters in T in complexity O(n).

    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"
"""


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    def addToBag(key, bag):
        if key in bag:
            bag[key] += 1
        else:
            bag[key] = 1

    if t == '':
        return ''

    targetBag, currentBag, keysToMatch = {}, {}, set(t)
    for tt in t:
        addToBag(tt, targetBag)

    left, right = 0, 0
    result = [0, len(s)]

    for right in range(len(s)):
        if s[right] in targetBag:
            addToBag(s[right], currentBag)
            if currentBag[s[right]] >= targetBag[s[right]] and s[right] in keysToMatch:
                keysToMatch.remove(s[right])
            if len(keysToMatch) == 0:
                while left <= right:
                    key = s[left]
                    if not key in currentBag:
                        left += 1
                    elif key in currentBag and currentBag[key] > targetBag[key]:
                        currentBag[key] -= 1
                        left += 1
                    else:
                        break
                # update result
                if right - left < result[1] - result[0]:
                    result = [left, right]

    return '' if result[1] == len(s) else s[result[0]: result[1] + 1]


if __name__ == '__main__':
    # print(minWindow('ADOBECODEBANC', 'ABC'))
    # print(minWindow('a', 'a'))
    # print(minWindow('a', 'aa'))
    # print(minWindow('aa', 'aa'))
    print(minWindow('aab', 'aab'))
    # print(minWindow('coobdafceeaxab', 'abc'))
