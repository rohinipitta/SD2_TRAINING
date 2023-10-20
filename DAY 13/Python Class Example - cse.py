# Define a class named cse
class cse:
    # Constructor (__init__) that takes an argument 'a'
    def __init__(self, a):
        # Print a message with the value of 'a' when an object is created
        print("hi", a)

    # A method 'fun' that takes 'self' and 'b' as arguments
    def fun(self, b):
        # Print a message with the value of 'b'
        print("hello", b)

# Create an object 'o' of the class 'cse' with the argument '2'
o = cse(2)

# Call the 'fun' method on object 'o' with the argument '12'
o.fun(12)


-----------------------------------------------------------------------------------------------------------
# Define a class named cse
class cse:
    # Constructor (__init__) that takes an argument 'a'
    def __init__(self, a):
        # Store the value of 'a' as an instance variable
        self.a = a

    # A method 'fun' that takes 'self' as an argument (note: 'b' is missing)
    def fun(b):
        # Print a message with the value of 'a' from 'b'
        print("hello", b.a)

# Create an object 'o' of the class 'cse' with the argument '2'
o = cse(2)

# Call the 'fun' method on object 'o' (Note: 'b' is missing here, causing an error)
o.fun()
