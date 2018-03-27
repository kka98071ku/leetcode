"""
Question:
    Design an algorithm to serialize and deserialize a binary tree.
"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrderSerialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str

    Requirement is that the traversal used in "serialize" step
    should be the same as the one used in "deserialize" step

    Pre-order traversal with ',' as the delimiter and '' as
    a None node.
    """
    if root == None:
        return ''
    serialized = []

    def _preOrderTraverse(node, result):
        if node == None:
            result.append('')
        else:
            result.append(str(node.val))
            _preOrderTraverse(node.left, result)
            _preOrderTraverse(node.right, result)

    _preOrderTraverse(root, serialized)
    return ','.join(serialized)


def preOrderDeserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    values = data.split(',')
    if values == []:
        return None

    def _buildTree(array, nodeIdx):
        if array[nodeIdx] == '':
            return (None, nodeIdx + 1)
        # Can switch to iterator
        node = TreeNode(int(array[nodeIdx]))
        node.left, nextIdx = _buildTree(array, nodeIdx + 1)
        node.right, nextIdx = _buildTree(array, nextIdx)
        return (node, nextIdx)

    root, _ = _buildTree(values, 0)
    return root


def bfsSerialize(root):
    if root == None:
        return ''
    serialized = []
    queue = deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        if node == None:
            serialized.append('')
            continue
        serialized.append(str(node.val))
        queue.append(node.left)
        queue.append(node.right)
    return ','.join(serialized)


def bfsDeserialize(data):
    values = data.split(',')
    if len(values) == 0:
        return None
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    while i < len(values):
        left = values[i]
        right = values[i + 1]
        node = queue.popleft()
        if left != '':
            node.left = TreeNode(int(left))
            queue.append(node.left)
        if right != '':
            node.right = TreeNode(int(right))
            queue.append(node.right)
        i += 2
    return root


if __name__ == '__main__':
    print(bfsDeserialize('1,2,3,,,4,5,6'))
