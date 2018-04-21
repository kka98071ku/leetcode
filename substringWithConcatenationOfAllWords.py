"""
Question:
    https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
"""

# GOOD, sliding window


class WordsBag:
    def __init__(self, words):
        self.words = words
        self.bag = {}

    def init(self):
        self.bag = {}
        for word in self.words:
            if word in self.bag:
                self.bag[word] += 1
            else:
                self.bag[word] = 1

    def has(self, key):
        return key in self.bag

    def remove(self, key):
        if not key in self.bag:
            return
        if self.bag[key] == 1:
            self.bag.pop(key)
        else:
            self.bag[key] -= 1

    def add(self, key):
        if not key in self.bag:
            self.bag[key] = 1
        else:
            self.bag[key] += 1

    def isEmpty(self):
        return len(self.bag) == 0


def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if len(words) == 0:
        return []
    wordLength = len(words[0])
    remainingWords = WordsBag(words)
    res = []

    # this step is important!
    for start in range(wordLength):
        remainingWords.init()
        ptr = start
        matchedWords = 0
        while ptr < len(s):
            test = s[ptr: ptr + wordLength]
            if remainingWords.has(test):
                matchedWords += 1
                remainingWords.remove(test)
                if remainingWords.isEmpty():
                    cursor = ptr - wordLength * (matchedWords - 1)
                    res.append(cursor)

                    # update the state
                    matchedWords -= 1
                    remainingWords.add(s[cursor: cursor + wordLength])
                ptr += wordLength
            else:
                if matchedWords == 0:
                    ptr += wordLength
                else:
                    cursor = ptr - wordLength * matchedWords
                    matchedWords -= 1
                    remainingWords.add(s[cursor: cursor + wordLength])
                    # in this case, we should not move forward but only shrink the window

    return res


if __name__ == '__main__':
    print(findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(findSubstring("wordgoodstudentgoodword", ["word", "student"]))
    print(findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",
                        ["fooo", "barr", "wing", "ding", "wing"]))
    print(findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    print(findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
    print(findSubstring("abababab", ["a", "b", "a"]))
