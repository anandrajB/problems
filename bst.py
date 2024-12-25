class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_tree():
    value = int(input("Enter value (-1 for no node): "))
    if value == -1:
        return None
    node = TreeNode(value)
    print(f"Creating left child of {value}")
    node.left = create_tree()
    print(f"Creating right child of {value}")
    node.right = create_tree()
    return node


create_tree()
