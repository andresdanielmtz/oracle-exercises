class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_data(self):
        print(self.data)


root = Node(0)
root.left = Node(1)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(2)


def dfs(root):
    visited = []
    stack = [root]
    while stack:
        val = stack.pop()

        if val not in visited:
            visited.append(visited)
            print(val.data)

            # we put right and left in that order since we might want to access the left node first, but since its level dependant it doesnt really matter either way.

            if val.right and val.right not in visited:
                stack.append(val.right)
            if val.left and val.left not in visited:
                stack.append(val.left)


dfs(root)
