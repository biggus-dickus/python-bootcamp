#! /usr/bin/env python

import math

# Fill in the Line class methods to accept coordinates as a pair of tuples
# and return the slope and distance of the line.
# li.distance() = 9.433981132056603
# li.slope() = 1.6
class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

        self.x1, self.y1 = self.coor1
        self.x2, self.y2 = self.coor2
    
    def distance(self):
        return math.sqrt(math.pow(self.x2 - self.x1, 2) + math.pow(self.y2 - self.y1, 2))
    
    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())


# Fill in the class
# c = Cylinder(2,3)
# c.volume() = 56.52
# c.surface_area() = 94.2 
class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())


# Create a bank account class
class Account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if Account.is_valid_amount(amount):
            self.balance += amount
            print('You added {} to your balance'.format(amount))

    def withdraw(self, amount):
        if Account.is_valid_amount(amount) and amount <= self.balance:
            self.balance -= amount
            print(f'You withdrew ${amount} and have ${self.balance} left on your balance')
        else:
            print('Funds unavailable!')    

    @staticmethod
    def is_valid_amount(val):
        return not isinstance(val, str) and val > 0

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

acct1 = Account('Jose',100)
print(acct1)
print(acct1.balance)
acct1.deposit(50)

acct1.withdraw(75)
acct1.withdraw(500)
