class MyClass:

    def __init__(self):
        self.x=1
        self.__y=2

    def display(self):
        print(self.x)
        print(self._MyClass__y)

m = MyClass()

print("Accessing variable through Methods")
m.display()

print("Accessing variable through instance")
print(m.x)
print(m._MyClass__y)

print("-----------------------------------------------")

class Loan:

    def __init__(self):
        self.accNo = 10
        self.name = "Srini"
        self.balance = 500000
        self.__loan = 1500000

    def display(self):
        print(self.accNo)
        print(self.name)
        print(self.balance)
        #print(self.loan)
        print(self._Loan__loan)

print("Accessing variable through Methods")
l = Loan()
l.display()

print("Accessing variable through instance")
print(l.accNo)
print(l.name)
print(l.balance)
print(l._Loan__loan)

