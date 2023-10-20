# Define a class named 'Node' to represent a node in a binary tree
class Node:
    def __init__(self, data):
        self.val = data  # Initialize the node's value
        self.left = None  # Initialize the left child to None
        self.right = None  # Initialize the right child to None

# Create the root node with a value of 1
root = Node(1)

# Create left and right child nodes for the root
root.left = Node(2)
root.right = Node(3)

# Initialize an empty queue 'q' to perform level-order traversal
q = []

# Add the root node to the queue
q.append(root)

# Perform level-order traversal
while q:
    # Dequeue the front node from the queue
    a = q.pop(0)

    # Print the value of the dequeued node
    print(a.val)

    # Enqueue the left child if it exists
    if a.left:
        q.append(a.left)

    # Enqueue the right child if it exists
    if a.right:
        q.append(a.right)
