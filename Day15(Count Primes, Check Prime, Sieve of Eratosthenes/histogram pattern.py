# Read a list of integers from the input
l = list(map(int, input().split()))

# Find the length of the list
n = len(l)

# Find the maximum value in the list
mxm = max(l)

# Loop from 'mxm' down to 1
for i in range(mxm, 0, -1):
    # Print the current height 'i' with two characters of space
    print(f"{i:2d} | ", end="")

    # For each element 'j' in the list
    for j in l:
        # If 'j' is greater than or equal to 'i', print 'x', otherwise, print a space
        if j >= i:
            print("x", end=" ")
        else:
            print(" ", end=" ")

    # Print a new line to start a new row
    print()
