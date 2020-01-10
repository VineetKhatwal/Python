class Person:

    def __init__(self, name="Test",dd=1, mm=1, yy=1990):
        self.name= name
        self.db = self.Dob(dd,mm,yy)

    def display(self):
        print("Name :", self.name)

    class Dob:

        def __init__(self, dd=1, mm=1, yy=1990):
            self.dd = dd
            self.mm = mm
            self.yy = yy

        def display(self):
            print("DOB = {} / {} / {}".format(self.dd,self.mm,self.yy))

p = Person()
p.display()

x = p.db
x.display()



p = Person("Ketan",14,12,1997)
p.display()

x = p.db
x.display()
