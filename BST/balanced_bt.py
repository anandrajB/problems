from typing import Optional


class Treee:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[Treee]) -> bool:
        return bool((self.height(root) >= 0))

    def height(self, root):
        if not root:
            return 0
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        if l_height < 0 or r_height < 0 or abs(l_height - r_height) > 1:
            return -1
        return 1 + max(l_height, r_height)
