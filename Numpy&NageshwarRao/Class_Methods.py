class Student:

    def __init__(self, n = "Ketan", m = 100):
        self.name = n
        self.marks = m

    def display(self):
        print("Hi", self.name)
        print("Marks :",self.marks)

    def Calculate(self):
        if (self.marks) >= 80:
            print("Grade : A")
        elif (self.marks) >= 70:
            print("Grade : B")
        elif (self.marks) >= 60:
            print("Grade : C")
        elif (self.marks) >= 50:
            print("Grade : D")
        elif (self.marks) >= 40:
            print("Grade : E")
        else:
            print("Grade : F")
        
n = int(input("How many Students "))
for i in range(n):
    name = input("Please enter Name ")
    marks = int(input("Please enter marks "))

    s = Student(name, marks)
    s.display()
    s.Calculate()
    print("------------------------")

print("----------------- ACCESSOR and MUTATOR methods ----------------")

class Student:

    def setName(self, name):
        self.name = name

    def setMarks(self, marks):
        self.marks = marks

    def getName(self):
        return self.name

    def getMarks(self):
        return self.marks

n = int(input("How many Students "))

for i in range(n):
    s = Student()
    name = input("Please enter Name ")
    s.setName(name)
    marks = int(input("Please enter marks "))
    s.setMarks(marks)
    
    print(s.getName())
    print(s.getMarks())
    print("------------------------")

print("---------------------- CLASS methods ---------------------")

class Bird:

    wings = 2

    @classmethod
    def fly(cls, name):
        # Class variables are refered as cls.variable
        print("{} flies with two {} wings".format(name, cls.wings))

# Class methods are refered as cls.methods
Bird.fly("Sparrow")
Bird.fly("Parrot")

b = Bird()
b.fly("Dove")

print("---------------------- STATIC methods ---------------------")

class MyClass:

    n = 0

    def __init__(self):
        MyClass.n += 1

        
    @staticmethod
    def noOfObject():
        print("No of instances created : ", MyClass.n)

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
MyClass.noOfObject()

