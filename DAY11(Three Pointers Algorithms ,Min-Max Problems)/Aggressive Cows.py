def can_i_place_My_Cows(arr, min_dist, cows):
    last = arr[0]  # Initialize the last position as the first element in 'arr'
    count = 1      # Initialize the count of cows placed to 1
    for i in range(1, len(arr)):  # Loop through the elements of 'arr' starting from the second element
        if abs(last - arr[i]) >= min_dist:  # Check if the distance between the last and current position is greater than or equal to 'min_dist'
            count += 1  # If the condition is met, increment the count of cows placed
            last = arr[i]  # Update the last position to the current position
    if count >= cows:  # Check if the count of cows placed is greater than or equal to the required 'cows'
        return True    # If it is, return True
    else:
        return False   # Otherwise, return False

# This function finds the maximum possible minimum distance to place 'cows' cows in 'arr'.
def solve(arr, cows):
    limit = max(arr) - min(arr)  # Calculate the maximum possible range for placement
    for i in range(1, limit + 1):  # Iterate through possible minimum distances from 1 to 'limit'
        if can_i_place_My_Cows(arr, i, cows) == True:  # Check if 'cows' can be placed with the current 'i' as the minimum distance
            continue
        else:
            return i - 1  # If it's not possible, return the previous minimum distance (i-1)

arr = list(map(int,input().split())) 
cows = int(input())
result = solve(arr, cows)  # Call the 'solve' function to find the maximum possible minimum distance
print(result)  # Print the result, which is the maximum minimum distance to place 'cows' cows
