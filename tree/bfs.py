from collections import deque  # Import deque for efficient queue operations


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printTree(self):
        print(self.data)


root = Node(0)
root.left = Node(1)
# root.left.left = Node(3)
root.left.right = Node(4)

root.right = Node(2)


def bfs(tree):
    visited = []
    queue = deque([tree])  # first node

    while queue:
        val = queue.popleft()

        if val not in visited:
            visited.append(val)
            print(val.data, sep=" ")

            # this is only for trees in which they have left and right
            # you could use it with a graph by checking all the neighbors of the node you're currently in and adding them to the queue if they hadnt been visited.
            if val.left and val.left not in visited:
                queue.append(val.left)
            if val.right and val.right not in visited:
                queue.append(val.right)


bfs(root)
