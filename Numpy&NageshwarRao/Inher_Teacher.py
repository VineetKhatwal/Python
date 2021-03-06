class Teacher:

    def setId(self, id):
        self.id = id

    def getID(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setSalary(self, sal):
        self.sal = sal

    def getSalary(self):
        return self.sal

class Student(Teacher):

    def setMarks(self,marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

print("-------------------  SUPER CLASS ------------------")

t = Teacher()
t.setId(10)
t.setName("Paul")
t.setSalary(10000)

print("{:<10s} = {}".format("ID",t.getID()))
print("{:<10s} = {}".format("Name",t.getName()))
print("{:<10s} = {}".format("Salary",t.getSalary()))

print("--------------------  SUB CLASS -------------------")
s = Student()

s.setId(1)
s.setName("Neha")
s.setMarks(92)

print("{:<10s} = {}".format("ID",s.getID()))
print("{:<10s} = {}".format("Name",s.getName()))
print("{:<10s} = {}".format("Salary",s.getMarks()))
