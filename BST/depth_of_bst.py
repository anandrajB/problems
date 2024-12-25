from typing import Optional


class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = right
        self.right = right


class Solution:

    def depth(self, root: TreeNode):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
