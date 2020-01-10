class Student:
    # Constructor : It is called when creating an instance :: s = Student()
    def __init__(self, n = "Ketan", id = 1, branch = 'CS', year = 3):                 
        self.Name = n
        self.Id = id
        self.Branch = branch
        self.__Year = year

    def talk(self):
        print("My name is", self.Name)
        print("Roll No", self.Id)
        print("Branch", self.Branch)
        print("Year", self._Student__Year)

s = Student()           # 's' contains the memory address of the instance
s.talk()                # This memory address is passed to 'self'.
                        # Thus, self knows the memory address of instance

print("------------------------------")
print("My name is", s.Name)
print("Roll No", s.Id)
print("Branch", s.Branch)
print("Year", s._Student__Year)

print("------------------------------")
s1 = Student("Vineet",2,"ET",4)
s1.talk()

print("--------------------------- INSTANCE VARIABLE --------------------------")

class Sample:

    def __init__(self):
        self.x = 10      # Instance Variable are initialized using a constructor using 'self' parameter
        				 # If we create n instances, we get n copies of instance variable, each independent of one another

    def modify(self):
        self.x = self.x+1

s1 = Sample()
s2 = Sample()

print(s1.x)
print(s2.x)

'''Sample.modify()    # ClassName.method() does not work for Instance Variable
print(s1.x)
print(s2.x)'''

s1.modify()
print(s1.x)
print(s2.x)


print("------------------------ CLASS or STATIC VARIABLE -----------------------")

class Sample:

    x = 10

    @classmethod
    def modify(cls):		# Single copy of class variable is available to all the instances
        cls.x = cls.x+1

s1 = Sample()
s2 = Sample()

print(s1.x)
print(s2.x)

s1.modify()
print(s1.x)
print(s2.x)

Sample.modify()
print(s1.x)
print(s2.x)

s2.modify()
print(s1.x)
print(s2.x)

print("------------------------ NAMESPACE -----------------------")

class Student:

    x = 10

print("---------------  Modifying in Class Namespace -------------")
print(Student.x)
Student.x += 1
print(Student.x)

s1 = Student()
print(s1.x)
s2 = Student()
print(s2.x)

print("---------------  Modifying in Instance Namespace -------------")
      
s1.x += 1
print(s1.x)
print(s2.x)


