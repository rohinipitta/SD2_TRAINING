# Define a class called MyHashSet
class MyHashSet:
    def __init__(self):
        # Initialize an empty set when an object is created
        self.s = set()

    def add(self, key: int) -> None:
        # Add the provided key to the set
        self.s.add(key)

    def remove(self, key: int) -> None:
        # Remove the provided key from the set
        self.s.remove(key)

    def contains(self, key: int) -> bool:
        # Check if the provided key exists in the set
        if key in self.s:
            return True
        else:
            return False

# Create an object of the MyHashSet class
obj = MyHashSet()

# Add keys 20 and 800 to the set
obj.add(20)
obj.add(800)

# Remove key 20 from the set
obj.remove(20)

# Check if key 800 exists in the set and store the result
param_3 = obj.contains(800)

# Print the result (param_3), which should be True in this case
print(param_3)
