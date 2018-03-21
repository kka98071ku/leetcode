def longestPalindromeDP(s):
    """
    :type s: str
    :rtype: str

    Dynamic programming solution space is O(n)
    because we only need to keep track of the
    previous two rows

    input: "abac"
    substring: input[index, index + length + 1]
    length \ index  0   1  2  3
         0          T   T  T  T
         1          F   F  F
         2          T   F
         3          F
    """
    if len(s) <= 1:
        return s
    n = len(s)
    resIdx, resLength = 0, 0
    minusOneLengthTable = [True for _ in range(n)]
    minusTwoLengthTable = [True for _ in range(n)]

    for length in range(1, len(s)):
        currentTable = []
        for startIdx in range(len(s) - length):
            isPalindrome = False
            if (s[startIdx] == s[startIdx + length]):
                isPalindrome = minusTwoLengthTable[startIdx + 1]
            if (isPalindrome):
                resIdx, resLength = startIdx, length
            currentTable.append(isPalindrome)
        minusOneLengthTable, minusTwoLengthTable = currentTable, minusOneLengthTable
        if (resLength < length - 1):
            break

    return s[resIdx: resIdx + resLength + 1]


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str

    Expand around the center.. takes O(1) space
    """
    start, end = 0, 0
    for i in range(0, len(s)):
        (l1, r1) = _expandAroundCenter(s, i, i)
        (l2, r2) = _expandAroundCenter(s, i, i + 1)
        maxLength = max((r1 - l1), (r2 - l2))
        if maxLength > end - start:
            (start, end) = (l1, r1) if r1 - l1 > r2 - l2 else (l2, r2)
    return s[start: end + 1]


def _expandAroundCenter(s, l, r):
    """
    return the valid left index and right index with the longest length
    """
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l = l - 1
        r = r + 1
    return (l + 1, r - 1)


if __name__ == "__main__":
    print(longestPalindrome("a"))
    print(longestPalindrome("aa"))
    print(longestPalindrome("aba"))
    print(longestPalindrome("acba"))
