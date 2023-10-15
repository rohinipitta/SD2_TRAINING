# Define a function 'find_subsets_with_sum' that finds a subset of non-negative integers from 'nums' with a target sum 'target'.
def find_subsets_with_sum(nums, target):
    n = len(nums)
    # Problem Statement 1: Create a 2D dynamic programming (DP) array to track possible subsets.
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    # Problem Statement 2: Initialize the first row of DP array, where a target sum of 0 is always achievable.
    for i in range(n + 1):
        dp[i][0] = True

    # Problem Statement 3: Fill the DP array to calculate if there exists a subset that sums to 'target'.
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Problem Statement 4: Compare the current element with the target value and set DP accordingly.
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    # Initialize variables for backtracking
    subset = []
    i, j = n, target

    # Problem Statement 5: Backtrack to find the actual subset that sums to 'target'.
    while i > 0 and j > 0:
        if dp[i][j] and not dp[i - 1][j]:
            subset.append(nums[i - 1])
            j -= nums[i - 1]
        i -= 1

    return subset

# Take input for the list of non-negative integers 'nums'
nums = list(map(int, input("Enter the list of non-negative integers separated by spaces: ").split()))

# Take input for the target sum 'target'
target = int(input("Enter the target sum: "))

result = find_subsets_with_sum(nums, target)

# Check the result and print an appropriate message
if result:
    print("Subset with the given sum:", result)
else:
    print("No such subset found.")
