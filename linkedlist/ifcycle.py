class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
ll.next.next.next.next = ll.next # just as an example 

slow = ll
fast = ll.next 

while slow is not None:
    if slow == fast:
        print("they met")
        break
    slow = slow.next
    fast = fast.next.next
print("they didn't met")


    