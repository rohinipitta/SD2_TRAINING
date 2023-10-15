# Problem Statement 1: Take input for the size of the square matrix 'n'.
n = int(input())

# Initialize an empty square matrix 'sq' of size 'n x n'.
sq = [[0] * n for i in range(n)]

# Initialize the number to be placed in the matrix.
num = 1

# Problem Statement 2: Calculate the starting positions for 'i' and 'j'.
i = n // 2
j = n - 1

# Problem Statement 3: Start filling the square matrix.
while num <= (n * n):
    # Problem Statement 4: Handle the case when 'i' and 'j' are out of bounds.
    if i < 0 and j == n:
        i = 0
        j = n - 2
    else:
        # Problem Statement 5: Handle the case when 'i' goes out of bounds.
        if i < 0:
            i = n - 1
        # Problem Statement 6: Handle the case when 'j' goes out of bounds.
        if j == n:
            j = 0
        # Problem Statement 7: Skip positions in the matrix that are already filled.
        if sq[i][j] != 0:
            i = i + 1
            j = j - 2
            continue
    # Problem Statement 8: Place the current 'num' in the matrix and increment 'num'.
    sq[i][j] = num
    num = num + 1
    # Update 'i' and 'j' for the next position.
    i = i - 1
    j = j + 1

# Problem Statement 9: Print the square matrix.
for row in sq:
    print(",".join(map(str, row)))
