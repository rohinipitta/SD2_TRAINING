# Define a recursive function 'check' that takes an array 'a', a target sum 't', and the current array size 'n'
def check(a, t, n):
    # Problem Statement 1: If the target sum is 0, we have found a solution.
    if t == 0:
        return True
    # Problem Statement 2: If we have exhausted all elements in the array and still haven't reached the target sum, no solution exists.
    if n == 0:
        return False
    # Problem Statement 3: If the current element is greater than the target sum, we can't include it in the solution.
    if a[n - 1] > t:
        return check(a, t, n - 1)
    
    # Recursive call to explore two possibilities:
    # 1. Include the current element in the solution and reduce the target sum and array size.
    # 2. Exclude the current element from the solution and only reduce the array size.
    return check(a, t - a[n - 1], n - 1) or check(a, t, n - 1)

# Take input for the array 'a'
a = list(map(int, input("Enter the array elements separated by spaces: ").split()))

# Take input for the target sum 't'
t = int(input("Enter the target sum: "))

# Call the 'check' function to determine if a solution exists
ans = check(a, t, len(a))

# Check the result and print an appropriate message
if ans:
    print("Solution found")
else:
    print("Not found")
