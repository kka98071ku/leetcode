"""
Question:
    Given a string S, we can transform every letter individually to be
    lowercase or uppercase to create another string.  Return a list of
    all possible strings we could create.

    Examples:
        Input: S = "a1b2"
        Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

        Input: S = "3z4"
        Output: ["3z4", "3Z4"]

        Input: S = "12345"
        Output: ["12345"]

    S will be a string with length at most 12.
    S will consist only of letters or digits.
"""


def letterCasePermutation(S):
    res = ['']
    for s in S:
        if s.isalpha():
            res = [i + j for i in res for j in [s.upper(), s.lower()]]
        else:
            res = [i + s for i in res]
    return res


class Node:
    def __init__(self, x):
        self.val = x
        self.children = []


def letterCasePermutationSlow(S):
    """
    :type S: str
    :rtype: List[str]

    LOL, I wrote such a complicated solution just to save copy pasting but
    apparently python's built-in list comprehension is WAY FASTER!!
    """
    n = len(S)
    if n == 0:
        return ['']
    dummyHead = Node('')
    childrenPtrs = [dummyHead.children]

    for s in S:
        if s in '1234567890':
            node = Node(s)
            for ptr in childrenPtrs:
                ptr.append(node)
            childrenPtrs = [node.children]
        else:
            node1 = Node(s.lower())
            node2 = Node(s.upper())
            for ptr in childrenPtrs:
                ptr.append(node1)
                ptr.append(node2)
            childrenPtrs = [node1.children, node2.children]

    results = []

    def _dfs(node, path):
        path.append(node)
        if node.children == []:
            results.append(''.join(map(lambda x: x.val, path)))
        else:
            for child in node.children:
                _dfs(child, path)
        path.pop()

    _dfs(dummyHead, [])
    return results


if __name__ == '__main__':
    print(letterCasePermutationSlow("a1b2"))
