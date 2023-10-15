# Define the base class Siva
class Siva:
    def wel(self):
        print("Welcome to the program")

# Define the first child class Baby1
class Baby1:
    def mag_pri(self, n):
        temp = n
        rev = 0
        flag = 0
        while n > 0:
            rem = n % 10
            rev = rev * 10 + rem
            n = n // 10
        for i in range(2, rev):
            if rev % i == 0:
                flag = 1
                break
        if flag == 1:
            print("It is not a magical prime")
        else:
            print("It is a magical prime")

# Define the second child class Baby2
class Baby2:
    def neon_num(self, num):
        for i in range(0, num + 1):
            sq = i * i
            total = 0
            if sq > 9:
                while sq > 0:
                    rem = sq % 10
                    total = total + rem
                    sq = sq // 10
                if total == i:
                    print(i)
            else:
                total = sq
                if total == i:
                    print(i)

# Create an instance of Baby1
b1 = Baby1()
n = int(input("Enter the prime number:"))
b1.mag_pri(n)

# Create an instance of Baby2
b2 = Baby2()
num = int(input("Enter the range to find neon numbers in between:"))
b2.neon_num(num)
