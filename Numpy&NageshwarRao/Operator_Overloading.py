print(10+15)

s1 = "Red"
s2 = "Fort"
print(s1+s2)

a = [10,20,30]
b = [-10,-20,-30]
print(a+b)

class Book1:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __gt__(self, other):
        return self.pages > other.pages

class Book2:
    def __init__(self,pages):
        self.pages = pages

    def __sub__(self, other):
        return self.pages - other.pages

    

b1 = Book1(100)
b2 = Book2(150)
print("Total Pages =", b1 + b2)
print("Diff Pages  =", b2 - b1)

if (b1 > b2):
    print("Book1 has more Pages")
else:
    print("Book2 has more Pages")
    
'''
if (b2 > b1):
    print("Book2 has more Pages")
else:
    print("Book1 has more Pages")
'''

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days

class Attendance:

    def __init__(self, name, days):
        self.name = name
        self.days = days

e = Employee("Srini",1000)
a = Attendance("Srini",29)
print("Total Salary ",e*a)

print("---------^^^^^^^^^^^^ Method Overloading ^^^^^^^^^^^^---------")

class MyClass:
    def Sum(self, a= None, b= None, c=None):

        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print("Please enter 2 or more arguments")
        
s = MyClass()
s.Sum(1,2,3)
s.Sum(1,2)
s.Sum(1)
