class Father:

    def __init__(self, property1=0):
        self.property1 = property1

    def displayProperty(self):
        print("{:20s} = {} ".format("Father's Property",self.property1))

class Child(Father):

    def __init__(self, property1=0, property2=0):
        super().__init__(property1)
        self.property2 = property2
        
    def displayProperty(self):
        super().displayProperty()
        print("{:20s} = {} ".format("Child's Property",self.property2))
        print("{:20s} = {} ".format("Toral Property",self.property1 + self.property2))

f = Father(100000)
f.displayProperty()

c = Child(100000,40000)
c.displayProperty()
#c.totalProperty()

