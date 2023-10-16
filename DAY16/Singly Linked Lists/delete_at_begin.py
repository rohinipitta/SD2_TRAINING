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

    def insert_at_beginning(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        
        # Set the new node as the head of the linked list
        new_node.next = self.head
        self.head = new_node

    def delete_at_beginning(self):
        if not self.head:
            # If the linked list is empty, return None
            return None

        # Save the value of the node to be deleted
        deleted_value = self.head.val

        # Update the head to the next node
        self.head = self.head.next

        # Return the deleted value
        return deleted_value

    def display(self):
        # Display the elements in the linked list
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

# Example usage:
l = [2, 4, 6, 8, 9]
sll = SinglyLinkedList()

for i in l:
    # Insert each element at the beginning of the linked list
    sll.insert_at_beginning(i)

# Delete the element at the beginning and print the deleted value
deleted_value = sll.delete_at_beginning()
print("Deleted value at the beginning:", deleted_value)

sll.display()
