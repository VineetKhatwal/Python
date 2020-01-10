import sys

class Emp:

    print("Passing members of One Class to another Class")
    
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID      =",self.id)
        print("Name    =",self.name)
        print("Salar   =",self.salary)

class MyClass:

    @staticmethod
    def myMethod(e):
        e.salary += 1000
        e.display()

e = Emp(1,"Ketan",10000)
e.display()
print("#####################")
MyClass.myMethod(e)

print("--------------------------------------")
class Bank:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawal(self, amount):
        if (amount > self.balance):
            print("Withdrawal amount is greater than balance - Can't withdraw")
        else:
            self.balance -= amount
        return self.balance

name = input("Please enter the name")
b = Bank(name)

while(True):
    print('d - Deposit : w- Withdrawal, e - EXIT')

    choice = input('Your Choice ')

    if choice== 'e' or choice == "E":
        sys.exit()

    amt = int(input("Please enter the amount "))

    if choice == 'd' or choice == "D":
        print("Balance after deposit :",b.deposit(amt))

    if choice == 'w' or choice == "W":
        print("Balance after withdrawal :",b.withdrawal(amt))
