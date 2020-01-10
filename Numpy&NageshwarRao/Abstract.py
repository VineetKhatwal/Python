from abc import ABC, abstractmethod

'''
An abstract class should be derived from a meta class ABC which belongs to an
abstract base class abc
'''

class MyClass:
    
    @abstractmethod
    def calculate(self, x):
        pass

class sub1(MyClass):
    def calculate(self, x):
        print("X =", x)

class sub2(MyClass):
    def calculate(self, x):
        print("Square =", x * x)

class sub3(MyClass):
    def calculate(self, x):
        print("Cube =", x * x * x)

obj1 = sub1()
obj1.calculate(5)

obj2 = sub2()
obj2.calculate(5)

obj3 = sub3()
obj3.calculate(5)
              
            
