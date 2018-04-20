"""
Question:
    https://leetcode.com/problems/wildcard-matching/description/
"""

# GOOD, DP


def isMatch(s, p):
    i, j, iStar, jStar = 0, 0, -1, -1
    while i < len(s):
        if j < len(p) and p[j] == '*':
            iStar, jStar = i, j
            # match '*' with empty string
            i -= 1
        else:
            if j == len(p) or (p[j] != '?' and p[j] != s[i]):
                # mismatch happens, try to use '*' to match 1 more char
                if iStar >= 0:
                    i = iStar
                    j = jStar
                    iStar += 1
                else:
                    return False
        i += 1
        j += 1

    while j < len(p) and p[j] == '*':
        j += 1
    return j == len(p)


def isMatchDP(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    if len(p) == 0:
        return len(s) == 0
    # boundary: use an empty pattern to match an empty string, always 'True'
    prev = [True]
    for pp in p:
        # boundary: use a non-empty pattern to match an empty string
        prev.append(prev[-1] and pp == '*')
    for i in range(len(s)):
        # boundary: use an empty pattern to match a non-empty string, always 'False'
        curr = [False]
        for j in range(len(p)):
            match = False
            if p[j] == '*':
                # there are three cases for '*'
                #   1. skip, do not match: dp[i][j] = dp[i][j - 1]
                #   2. match the current charactor: dp[i][j] = dp[i - 1][j - 1]
                #   3. match the current and more: dp[i][j] = dp[i - 1][j]
                match = prev[j] or prev[j + 1] or curr[j]
            else:
                match = (p[j] == s[i] or p[j] == '?') and prev[j]
            curr.append(match)
        prev = curr
    return prev[-1]


if __name__ == '__main__':
    print(isMatch("aa", "a") == False)
    print(isMatch("aa", "aa") == True)
    print(isMatch("aaa", "aa") == False)
    print(isMatch("aa", "*") == True)
    print(isMatch("aa", "a*") == True)
    print(isMatch("ab", "?*") == True)
    print(isMatch("aab", "c*a*b") == False)
