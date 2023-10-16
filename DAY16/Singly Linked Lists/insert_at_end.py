# Define a Node class for the elements in the linked list
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

# Define a SinglyLinkedList class
class SinglyLinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head node
        self.head = None

    def insert_at_end(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        
        if not self.head:
            # If the linked list is empty, set the new node as the head
            self.head = new_node
        else:
            current = self.head
            while current.next:
                # Traverse to the end of the list
                current = current.next
            current.next = new_node
            # Add the new node at the end

    def display(self):
        # Display the elements in the linked list
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

# Example usage:
l = list(map(int,input().split()))
sll = SinglyLinkedList()

for i in l:
    # Insert each element at the end of the linked list
    sll.insert_at_end(i)

sll.display()
