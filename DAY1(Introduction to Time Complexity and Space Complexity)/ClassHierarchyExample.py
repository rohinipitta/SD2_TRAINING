# Define the base class Siva
class Siva:
    # Define a method in the base class
    def gold(self):
        print("Hello")

# Define a child class Baby1 that inherits from Siva
class Baby1(Siva):
    # Define a method in Baby1
    def bank(self):
        print("dep 2L")

# Define another child class Baby2 that also inherits from Siva
class Baby2(Siva):
    # Define a method in Baby2
    def jewels(self):
        print("Diamond")

# Define a grandchild class Gbaby that inherits from Baby1
class Gbaby(Baby1):
    # Define a method in Gbaby
    def grand(self):
        print("grand child")

# Create an instance of Gbaby
b1 = Gbaby()

# Call the 'grand' method of Gbaby
b1.grand()

# Call the 'bank' method of Gbaby, inherited from Baby1
b1.bank()

# Create an instance of Baby2
b2 = Baby2()

# Call the 'jewels' method of Baby2
b2.jewels()

# Call the 'gold' method of Baby2, inherited from Siva
b2.gold()
