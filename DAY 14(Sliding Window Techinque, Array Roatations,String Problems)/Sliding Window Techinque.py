# Read a list of integers from the input
l = list(map(int, input().split()))

# Read the target sum
t = int(input())

i = 0
j = 0
n = len(l)
s = l[0]

# Initialize variables for indices i and j and the sum s
while i < n and j < n:
    # Check if the current pair of elements sums to t
    if s == t:
        print(l[i], l[j], sep=",")
        break
    elif s > t:
        # If the sum is greater than t, reduce s by removing l[i] and advancing i
        s -= l[i]
        i += 1
    else:
        # If the sum is less than t, increase s by adding l[j] and advancing j
        j += 1
        s += l[j]
else:
    # If the loop completes without finding a pair, print a message
    print("No pair found with the sum", t)
