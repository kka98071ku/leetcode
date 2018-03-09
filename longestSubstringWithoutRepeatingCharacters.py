def longestSubstringWithoutRepeatingCharacters(s):
    """
    :type s: str
    :rtype: int
    """
    if (s == None):
        return 0
    maxLength = 0
    charToIndex = {}
    p1, p2 = 0, 0
    while p2 < len(s):
        currentChar = s[p2]
        if currentChar in charToIndex:
            # sliding window, consider "baaab"
            p1 = max(p1, charToIndex[currentChar] + 1)

        charToIndex[currentChar] = p2
        maxLength = max(maxLength, p2 - p1 + 1)
        p2 = p2 + 1
    return maxLength


if __name__ == "__main__":
    print(longestSubstringWithoutRepeatingCharacters("") == 0)
    print(longestSubstringWithoutRepeatingCharacters("a") == 1)
    print(longestSubstringWithoutRepeatingCharacters("aa") == 1)
    print(longestSubstringWithoutRepeatingCharacters("aab") == 2)
    print(longestSubstringWithoutRepeatingCharacters("aabb") == 2)
    print(longestSubstringWithoutRepeatingCharacters("abba") == 2)
    print(longestSubstringWithoutRepeatingCharacters("abcabcbb") == 3)
    print(longestSubstringWithoutRepeatingCharacters("bbtablud") == 6)
    print(longestSubstringWithoutRepeatingCharacters("gaaqfeqlqky") == 4)
