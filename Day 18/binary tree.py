# Define a class named 'Node' to represent a node in a binary tree
class Node:
    def __init__(self, data):
        self.val = data  # Initialize the node's value
        self.left = None  # Initialize the left child to None
        self.right = None  # Initialize the right child to None

# Define a recursive function to perform depth-first traversal (preorder, inorder, postorder)
def printing(root):
    if root == None:
        return
    print(root.val)  # Preorder (root, left, right)
    printing(root.left)
    # print(root.val)  # Inorder (left, root, right)
    printing(root.right)
    # print(root.val)  # Postorder (left, right, root)

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

# Perform depth-first traversal using the 'printing' function
printing(root)

# Initialize a queue 'q' for level-order traversal
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
