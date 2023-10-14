# Problem Statement 1: Define a function 'inversion_count' to count the number of inversions in an array.
def inversion_count(arr):
    # Problem Statement 2: Base case - if the array has one or no elements, there are no inversions.
    if len(arr) <= 1:
        return 0
    
    # Problem Statement 3: Split the array into two halves.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    inv_count = 0

    # Problem Statement 4: Recursively count inversions in both halves.
    inv_count += inversion_count(left)
    inv_count += inversion_count(right)

    i = j = k = 0

    # Problem Statement 5: Merge the two halves and count inversions.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            # Problem Statement 6: Count inversions when an element from the right subarray is smaller than an element from the left subarray.
            inv_count += len(left) - i
        k += 1

    # Problem Statement 7: Copy any remaining elements from the left subarray.
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Problem Statement 8: Copy any remaining elements from
