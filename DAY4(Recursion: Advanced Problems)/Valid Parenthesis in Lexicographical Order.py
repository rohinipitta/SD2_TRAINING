class Solution(object):
    def generateParenthesis(self, n):
        l = []  # List to temporarily store parentheses combinations
        res = []  # List to store the final result
        
        def backtrack(opencount=0, closecount=0):
            # Problem Statement 1: If the desired number of open and close parentheses is achieved, add the combination to the result.
            if opencount == closecount == n:
                res.append("".join(l))
            
            # Problem Statement 2: If the open parentheses count is less than 'n', add an open parenthesis.
            if opencount < n:
                l.append('(')
                backtrack(opencount + 1, closecount)
                l.pop()  # Remove the last added parenthesis for backtracking.
            
            # Problem Statement 3: If the close parentheses count is less than the open count, add a close parenthesis.
            if closecount < opencount:
                l.append(')')
                backtrack(opencount, closecount + 1)
                l.pop()  # Remove the last added parenthesis for backtracking.
            
            return res  # Return the list of valid combinations.

        return backtrack()

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    solution = Solution()
    result = solution.generateParenthesis(n)
    print("Generated Parentheses:", result)
