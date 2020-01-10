class Father:

    def __init__(self):
        self.property = 80000.0

    def display(self):
        print("{:20s} = {} ".format("Property",self.property))

f = Father()
f.display()

class Son1(Father):       
    # Overriding Super Class Method
    
    def display(self):
        print("{:20s} = {} ".format("Inherited Property",self.property))

s1 = Son1()
s1.display()


class Son2(Father):

     # Overriding Super Class constructor
     
     def __init__(self):        
        self.property = 10000.0

s2 = Son2()
s2.display()

class Son(Father):

    # We don't want to write anything in this class
    
    pass

s = Son()
s.display()
