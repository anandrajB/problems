class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value == self.value:
            return

        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        return value


# Example usage
root = TreeNode(10)
root.left = TreeNode(30)
root.left.left = TreeNode(20)
root.right = TreeNode(20)
root.right.right = TreeNode(40)

ds = root.insert(50)
