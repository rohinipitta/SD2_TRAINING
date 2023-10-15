
l = list(map(int, input().split()))

# Take an integer 't' as the target sum
t = int(input())

# Initialize a flag 'c' to 0; it will be used to track whether a valid combination is found
c = 0

# Iterate through all possible combinations of three elements in the list 'l'
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        for k in range(j + 1, len(l)):
            # Check if the sum of the three elements equals the target 't'
            if l[i] + l[j] + l[k] == t:
                c = 1

# Check the value of 'c' to determine if a valid combination was found
if c == 1:
    print("found")
else:
    print("Not found")
