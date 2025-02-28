from main import Node, LinkedList

ll = LinkedList() 
ll.insertEnd(1)
ll.insertEnd(2)
ll.insertEnd(2)
ll.insertEnd(3)
ll.insertEnd(3)
ll.insertEnd(3)
ll.insertEnd(4)

curr = ll.head 
result = LinkedList() 
elems = []

while curr is not None:
    if curr.data not in elems:
        elems.append(curr.data)
        result.insertEnd(curr.data) 
    curr = curr.next 
print(elems)