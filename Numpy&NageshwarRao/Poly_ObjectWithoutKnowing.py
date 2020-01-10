class Duck:

    def talk(self):
        print("Quack - Quack")

class Human:
    
    def talk(self):
        print("Human talks")

class Dog:
    
    def bark(self):
        print("Bow Bow")

'''
call_talk method receives an onject (of any type) and calls the talk() method
of the class it belongs to.
'''

def call_talk(obj):
    if hasattr(obj, 'talk'):
        obj.talk()
    elif hasattr(obj, 'bark'):
        obj.bark()
    else:
        print("Wrong Object Passed")
        
x = Duck()
call_talk(x)

y = Human()
call_talk(y)

z = Dog()
call_talk(z)

