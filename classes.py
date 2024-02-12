#1
class StringProcessor:
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input("Enter a string: ")
    
    def printString(self):
        print(self.string.upper())
processor = StringProcessor()

processor.string = "Hello World"

processor.printString()

#2
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self) 
        self.length = length
    
    def area(self):
        return self.length ** 2
    
square = Square(4)

square.area()

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)  
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 6)

rectangle.area()

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return (self.x, self.y)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

point1 = Point(0, 0)
point2 = Point(3, 4)

print("Initial position of point1:", point1.show())

point1.move(2, 3)
print("New position of point1:", point1.show())

distance = point1.dist(point2)
print("Distance between point1 and point2:", distance)

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of {amount} was successful. New balance is {self.balance}."
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Withdrawal denied due to insufficient funds."
        else:
            self.balance -= amount
            return f"Withdrawal of {amount} was successful. New balance is {self.balance}."

account = Account("John Doe", 100)

print(account.deposit(50))
print(account.deposit(150))

print(account.withdraw(50))
print(account.withdraw(300))  

print(f"Final balance is {account.balance}.")

#6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 5, 7, 11, 13, 4, 6, 8, 9, 10, 12]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

prime_numbers


