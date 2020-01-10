from numpy import *

arr = array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print()
a = matrix(arr)
print(a)
print()

a= matrix([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print()

a='1 2;3 4;5 6'
print(a)
print()
a= matrix(a)
print(a)
print()
a= matrix('1 2;3 4;5 6')
print(a)
print()

d=diagonal(a)
print(d)
print()

print(a.max())   # For 2 D Array
# print(max(a))

print(a.min())

print(a.sum())
print(sum(a))

print(a.mean())

a= matrix([[110,2,3],[4,55,6],[7,8,99]])
a=sort(a)               # Sorts row wise
print(a)
a=sort(a,axis=0)        # Sorts column wise
print(a)
a=transpose(a)
print(a)







