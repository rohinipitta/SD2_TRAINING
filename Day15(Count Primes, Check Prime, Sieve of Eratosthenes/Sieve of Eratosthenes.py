# Define a function named 'isprime' that finds and prints prime numbers up to 'num'
def isprime(num):
    # Create a boolean list 'prime' to mark numbers as prime or not
    prime = [True] * (num + 1)
    p = 2
    
    # Iterate while the square of 'p' is less than 'num'
    while p * p <= num:
        if prime[p]:
            # Mark multiples of 'p' as non-prime
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    
    # Print the prime numbers
    for p in range(2, num + 1):
        if prime[p]:
            print(p)

# Define the value of 'num'
num = int(input())

# Call the 'isprime' function with 'num' and print the prime numbers
isprime(num)
