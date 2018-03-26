"""
Question:
    Given a binary tree, find the maximum path sum.
    For this problem, a path is defined as any sequence of nodes from
    some starting node to any node in the tree along the parent-child
    connections. The path must contain at least one node and does not
    need to go through the root.

    For example:
    Given the below binary tree,

           1
          / \
         2   3
    Return 6.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def _maxPathSum(node):
    # node != None
    if node.left == None and node.right == None:
        return (node.val, node.val)

    nodePathMaxCandidates = []
    pathThroughRoot = node.val
    nodePathFromRootCandidates = [node.val]

    if node.left:
        leftPathMax, leftPathFromRootMax = _maxPathSum(node.left)
        nodePathMaxCandidates.append(leftPathMax)
        leftPathFromRootMaxOrZero = max(0, leftPathFromRootMax)
        nodePathFromRootCandidates.append(leftPathFromRootMaxOrZero + node.val)
        pathThroughRoot += leftPathFromRootMaxOrZero

    if node.right:
        rightPathMax, rightPathFromRootMax = _maxPathSum(node.right)
        nodePathMaxCandidates.append(rightPathMax)
        rightPathFromRootMaxOrZero = max(0, rightPathFromRootMax)
        nodePathFromRootCandidates.append(rightPathFromRootMaxOrZero + node.val)
        pathThroughRoot += rightPathFromRootMaxOrZero

    nodePathMaxCandidates.append(pathThroughRoot)
    return (max(nodePathMaxCandidates), max(nodePathFromRootCandidates))


def maxPathSum(root):
    if root == None:
        return 0
    result, _ = _maxPathSum(root)
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    root.left = node2
    node3 = TreeNode(3)
    node2.left = node3
    node4 = TreeNode(4)
    node3.left = node4
    node5 = TreeNode(5)
    node4.left = node5
    print(maxPathSum(root))
