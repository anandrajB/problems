class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def max_width(self, node):
        h = self.height(node)
        max_width = 0
        for i in range(1, h + 1):
            width = self.width(node, i)
            if width > max_width:
                max_width = width
        return max_width

    def width(self, node: Node, level):
        if not node:
            return 0
        if level == 1:
            return 1
        return self.width(node.left, level - 1) + self.width(node.right, level - 1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

solution = Solution()
print(solution.max_width(root))
