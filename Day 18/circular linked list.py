# Define a class 'node' to represent a node in the circular linked list
class node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

# Define a class 'cll' to represent the circular linked list
class cll:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert a node at the beginning of the circular linked list
    def insertatbeg(self, data):
        if self.head == None:
            self.head = node(data)
            self.tail = self.head
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            new = node(data)
            new.next = self.head
            self.head.prev = new
            self.head = new
            self.tail.next = self.head
            self.head.prev = self.tail

    # Insert a node at the end of the circular linked list
    def insertatend(self, data):
        if self.head == None:
            self.head = node(data)
            self.tail = self.head
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            new = node(data)
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head
            self.head.prev = self.tail

    # Delete a node from the beginning of the circular linked list
    def deleteatbeg(self):
        if self.head == None:
            return
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head

    # Delete a node from the end of the circular linked list
    def deleteend(self):
        if self.head == None:
            return
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail

    # Print the circular linked list
    def printing(self):
        print(self.head.val, end="->")
        temp = self.head.next
        while temp != self.head:
            print(temp.val, end="->")
            temp = temp.next

# Initialize two lists 'l' and 'm'
l = [2, 4, 6, 7, 9]
m = [5, 1, 3, 8]

# Create a circular linked list 'o'
o = cll()

# Insert elements from list 'm' at the beginning of the circular linked list
for i in m:
    o.insertatbeg(i)

# Print the circular linked list after inserting elements from 'm'
o.printing()
print()

# Insert elements from list 'l' at the end of the circular linked list
for j in l:
    o.insertatend(j)

# Print the circular linked list after inserting elements from 'l'
o.printing()
print()

# Delete a node from the beginning of the circular linked list
o.deleteatbeg()

# Print the circular linked list after deleting from the beginning
o.printing()
print()

# Delete a node from the end of the circular linked list
o.deleteend()

# Print the circular linked list after deleting from the end
o.printing()
