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

    def insert_at_end(self, data):
        # Create a new node with the given data
        new_node = Node(data)

        if self.head is None:
            # If the list is empty, set the new node as both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Update the new node's previous pointer to the current tail
            new_node.prev = self.tail
            # Update the current tail's next pointer to the new node
            self.tail.next = new_node
            # Update the tail to the new node
            self.tail = new_node

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
    # Insert each element at the end of the doubly linked list
    dll.insert_at_end(i)

# Display the doubly linked list
dll.display()
