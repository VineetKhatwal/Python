# assign function to a variable
def display(str):
    return "Hi " + str

x = display("Vineet")
print(x)

'''----------------------------------------------------------'''
# define a function inside a function
def display(str):
    def message():
        return "Hi "

    result = message() + str
    return result

x = display("Vineet")
print(x)

'''----------------------------------------------------------'''
# Passing a function as a parameter to another function
def display(msg):
    return "Hi " + msg

def message(str):
    return str

print(display(message("Vineet")))

'''----------------------------------------------------------'''
# A function that returns another function
def display():
    def message():
        return "END"
    return message

fun = display()
print(fun())

'''----------------------------------------------------------'''

print("------------ Pass by OBJECT REFERENCE ---------------")

'''-------------------------------------------------------------------------
In python, values are passed to function by Object Reference.

If the object is mutable, the modified value are available outside the function
List and Dictionaries are mutable

If the object is immutable, the modified value are not vailable outside the function
Integer, Float, String and tuples are immutable
-------------------------------------------------------------------------'''

def modify(x):
    x= 15                  # Integer objects are immutable
    print(x,id(x))

x = 10
modify(x)
print(x,id(x))

"--------------------------------------------------------------------"

def modify(x):
    x.append(5)          # List objects are mutable
    print(x,id(x))

x = [1,2,3,4]
modify(x)
print(x,id(x))

"--------------------------------------------------------------------"
''' If we create a new list inside the function, it is not available outside the function'''

def modify(x):
    x = [5,6,7,8]        # List objects are mutable
    print(x,id(x))

x = [1,2,3,4]
modify(x)
print(x,id(x))

print("---------------- Keyword Argument ----------------")

def grocery(item="Flour", price=12):        # Default Argument
    print(item, price)

grocery(price=10.0, item="Maggi")
grocery(item="Oil", price=100.0)
grocery(price=10.0)
grocery(item="Oil")
grocery()

print("---------------- Variable Length Argument ----------------")

def add(farg, * args):
    sum = 0
    for i in args:
        sum = sum + i
    print(farg+sum)

add(5,10)
add(5,10,15,20)

print("---------------- Local and Global Variable ----------------")

a=10
b=20
c=30
d=0
def func():
    a=11
    d=1
    global c
    print("A =",a)
    print("B =",b)
    print("C =",c)
    x = globals()['d']
    print("X =",x)
    print("D =",d)
    
func()
print("------------------")
print("A =",a)
print("B =",b)
print("C =",c)
print("D =",d)

print("-----------------------------------------------")

def sumAvg(lst):
    sum = 0
    count =0
    for i in lst:
        sum = sum+i
        count = count+1
    return sum, sum/count
        

print("Enter the numbers seperated by commas")
lst = [int(x) for x in input().split(',')]
x,y = sumAvg(lst)
print("Sum  = ",x)
print("Avg  = ",y)


print("---------------RECURSION--------------------")

def rec(n):
    if (n==1):
        return 1
    else:
        return n * rec(n-1)

for i in range(1,11):
    print("Factorial of {} is {}".format(i,rec(i)))
