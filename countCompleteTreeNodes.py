"""
Question:
    Given a complete binary tree, count the number of nodes.

    Definition of a complete binary tree from Wikipedia:
    In a complete binary tree every level, except possibly the last, is completely
    filled, and all nodes in the last level are as far left as possible. It can
    have between 1 and 2h nodes inclusive at the last level h.
"""

# GOOD, complete binary tree
# #{nodes of a full binary tree} = (1 << height ) - 1


def countNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    left, right = root.left, root.right
    height_left, height_right = 0, 0
    while left:
        left = left.left
        height_left += 1
    while right:
        right = right.left
        height_right += 1
    if height_left == height_right:
        return (1 << height_left) + countNodes(root.right)
    else:
        return (1 << height_right) + countNodes(root.left)
