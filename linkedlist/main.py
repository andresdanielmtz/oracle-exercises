class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data): 
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
         
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def insert_at_index(self, index, data):
        curr_node = self.head # initialize
        new_node = Node(data)

        for i in range(0, index): 
            if curr_node.next is None: # if we reach the end of the list 
                curr_node.next = new_node 
                return 
            curr_node = curr_node.next
        
        new_node.next = curr_node.next
        curr_node.next = new_node # that's it :D 

    def delete_end(self):
        curr_node = self.head 
        while curr_node.next.next is not None: # traverse to the end of the string 
            curr_node = curr_node.next 
        curr_node.next = None

    def insert_beginning(self, data):
        new_node = Node(data) 
        curr_node = self.head 
        if curr_node is None: 
            self.head = new_node 
            return
    
        new_node.next = self.head 
        self.head = new_node

    def print_content(self):
        curr_node = self.head
        while curr_node is not None:
            print(f"Current Node: {curr_node.data}")
            curr_node = curr_node.next 
    
    def reverse_linked_list_memory(self): 
        result = LinkedList() 
        curr_node = self.head 

        while curr_node is not None:
            result.insert_beginning(curr_node.data)
            curr_node = curr_node.next 
        return result 
    
 
if __name__ == "__main__":
    ll = LinkedList()

    ll.insertEnd(1)
    ll.insertEnd(2)
    ll.insertEnd(3)
    ll.insertEnd(4)
    ll.insertEnd(5)
    ll.insert_beginning(0)

    # ll.print_content()
    reverse = ll.reverse_linked_list_memory()
    reverse.print_content()
