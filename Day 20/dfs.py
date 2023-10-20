# Define a function 'fun' that performs DFS on a directed graph
def fun(d, start, vis):
    # Define a nested function 'dfs' to recursively traverse the graph
    def dfs(start, vis):
        vis.add(start)  # Add the current node to the set of visited nodes
        for i in d[start]:
            if i not in vis:  # If the neighbor node is not visited
                dfs(i, vis)  # Recursively visit the neighbor node
        return vis

    return dfs(start, vis)  # Start the DFS from the 'start' node

# Define the directed graph as an adjacency list
d = {1: [2], 2: [3, 5], 3: [5], 4: [2, 3], 5: []}

# Specify the starting node
start = 1

# Create an empty set to store visited nodes
vis = set()

# Call the 'fun' function to perform DFS and print the result (visited nodes)
print(fun(d, start, vis))
