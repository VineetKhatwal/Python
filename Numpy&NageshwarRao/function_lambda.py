# lambda argument_list : expression

f = lambda x: x*x      # Don't need return [Implicit Return]
value = f(5)
print(value)
print(f(10))

print('------------------------')
f = lambda x,y: x+y
print(f(5,6))

print('------------------------')
f = lambda x,y: x if x>y else y
print("Greater number is ", f(5,6))

print('---------- FILTER --------------')

# filter(function, sequence)
# filter function is used to filter out the elements of a sequence

def isEven(x):
    if x%2 == 0:
        return True
    else:
        return False
lst =[10,11,12,13,14,15]
list1=list(filter(isEven,lst))
print(list1)

list2=list(filter(lambda x: (x%2==0),lst))
print(list2)

print('---------- MAP --------------')

# map(function, sequence)
# map function acts on each element of the function and changes its values

def square(x):
    return x*x

lst = [1,2,3,4,5]
list1 = list(map(square,lst))
print(list1)

list2 = list(map((lambda x: x*x),lst))
print(list2)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = list(map((lambda x,y : x*y),list1,list2))
print(list3)

print('---------- REDUCE --------------')

# reduce(function, sequence)
# reduce function reduces a sequence of elements into a single value
from functools import *
list1 = [1,2,3,4,5]
list2 = reduce((lambda x,y: x*y),list1)
print(list2)

# To sum numbers from   1 to n
print(reduce(lambda x,y:x+y, range(1,51)))

