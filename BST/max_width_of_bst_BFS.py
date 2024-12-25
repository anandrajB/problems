from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def max_width(self, root: Node):
        if not root:
            return 0

        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            level_length = len(queue)
            _, first_pos = queue[0]  # Get the position of the first node in the level
            _, last_pos = queue[-1]  # Get the position of the last node in the level

            max_width = max(max_width, last_pos - first_pos + 1)

            # Process all nodes at the current level
            for _ in range(level_length):
                node, pos = queue.popleft()
                # Add the children to the queue with their respective positions
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))

        return max_width


# Example usage
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
