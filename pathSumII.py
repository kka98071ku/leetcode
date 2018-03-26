"""
Question:
    Given a binary tree and a sum, find all root-to-leaf paths where each path's
    sum equals the given sum.

    For example:
    Given the below binary tree and sum = 22,
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
    return
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
"""


def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    paths = []

    def _dfs(root, s, path):
        if root == None:
            return
        if root.left == None and root.right == None:
            if root.val == s:
                _path = path[:]
                _path.append(root.val)
                paths.append(_path)
        else:
            path.append(root.val)
            _dfs(root.left, s - root.val, path)
            _dfs(root.right, s - root.val, path)
            path.pop()

    _dfs(root, sum, [])
    return paths
