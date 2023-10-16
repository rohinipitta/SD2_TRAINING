# Define a Node class for the elements in the doubly linked list
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

# Define a DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        # Initialize an empty doubly linked list with head and tail nodes
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        
        # Handle the case when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Update the new node's next pointer to the current head
            new_node.next = self.head
            # Update the current head's previous pointer to the new node
            self.head.prev = new_node
            # Update the head to the new node
            self.head = new_node

    def display(self):
        # Display the elements in the doubly linked list
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

# Example usage:
l = list(map(int,input().split()))
dll = DoublyLinkedList()

for i in l:
    # Insert each element at the beginning of the doubly linked list
    dll.insert_at_beginning(i)

dll.display()
