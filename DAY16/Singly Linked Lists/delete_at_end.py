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

    def delete_at_end(self):
        # Check if the linked list is empty
        if not self.head:
            return

        # If the list contains only one element, set the head to None
        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            # Traverse to the element just before the last element
            current = current.next

        # Remove the last element from the list
        current.next = None

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
    # Insert each element at the end of the linked list
    sll.insert_at_end(i)

# Delete the last element in the linked list
sll.delete_at_end()

sll.display()
