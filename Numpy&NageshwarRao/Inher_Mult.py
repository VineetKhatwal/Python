class Father:

    def displayHeight(self):
        print("Height = 6 feet")

class Mother:

    def eyesColor(self):
        print("Eyes Color = Brown")

class Child(Father, Mother):
    def __init__(self):
        self.wt = 65

    def displayWeight(self):
        print("Weight =",self.wt)

c = Child()
c.displayWeight()
c.displayHeight()
c.eyesColor()

print("------------ Problem with Multiple Inheritance --------------")

class A:
    def __init__(self):
        self.a = 'a'
        print("A =",self.a)
        
class B:
    def __init__(self):
        self.b = 'b'
        print("B =",self.b)

class C(A,B):
    def __init__(self):
        super().__init__()
        self.c = 'c'
        print("C =",self.c)

obj = C()


print("------------ Resolving Problem with Multiple Inheritance --------------")

class A:
    def __init__(self):
        
        self.a = 'a'
        print("A =",self.a)
        super().__init__()
        
        
class B:
    def __init__(self):
        
        self.b = 'b'
        print("B =",self.b)
        super().__init__()
        
        
class C(A,B):
    def __init__(self):
        super().__init__()
        self.c = 'c'
        print("C =",self.c)

obj = C()


    

    

        


