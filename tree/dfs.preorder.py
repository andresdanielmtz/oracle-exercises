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


def dfs_recursive(root):
    print(root.data)
    if root.left:
        dfs_recursive(root.left)
    if root.right:
        dfs_recursive(root.right)


def dfsPreorder(root):
    
    dfs_recursive(root)

dfsPreorder(root)
