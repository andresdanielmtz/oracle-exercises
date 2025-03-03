class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # singular node

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        if self.head == None:  # ?? if the linked list is empty, the head is the new one
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def add_at_end(self, data):
        head = self.head
        new_node = Node(data)
        if head is None:
            self.head = new_node
        while head.next:
            head = head.next
        head.next = new_node
