"""
BFS by counting through each level. : )
"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.left.left.left = Node(5)

# get maximum level


def dfs(root):
    queue = deque([root])  # start with root
    index = 0
    while queue:
        for _ in range(0, len(queue)):  # for each element in queue
            value = queue.popleft()

            if value.left:
                queue.append(value.left)
            if value.right:
                queue.append(value.right)
        index += 1
    print(f"max val: {index}")


dfs(root)
