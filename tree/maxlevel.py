'''
dfs
'''

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
    visited = []
    queue = deque([root]) # start with root 
    maxlevel = 0 
    index = 1 
    while queue:
        value = queue.popleft()
        

        if value and value not in visited:
            visited.append(value)
            
            index += 1
            if value.left: 
                queue.append(value.left)
                index += 1
            if value.right:
                queue.append(value.right)       

    print(f"max val: {maxlevel}")

dfs(root)