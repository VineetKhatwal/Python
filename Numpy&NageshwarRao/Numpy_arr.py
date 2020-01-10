'''
import numpy

a = numpy.array([1,2,3,4,5])
print(a)
'''

from numpy import *

a = array([1,2,3,4,5])
print(a)
a[2] =100
print(a)

for i in a:
    print(i, end= " ")
print()

b = array(['a','b','c','d','d'])
for i in b:
    print(i, end= " ")  
print()

c = array(['Ketan','Neha','Vineet'], dtype = str)  # dtype = str : Important for string
for i in c:
    print(i, end= " ")
print()

d = linspace(0,10,5)
print(d)

e = logspace(0,10,5)
print(e)

f = arange(0,10,2)
for i in f:
    print(i, end= " ")
print()

g= zeros(5,int)
print(g)

h= ones(5,int)
print(h)

print("---------------------------")
print(a+2*a)
print(2*a - a)
print(sin(a))
print(sqrt(a))
print(prod(a))
print(sum(a))
print(min(a))
print(max(a))
print(mean(a))
print(median(a))
print(average(a))
print(power(a,2))

print("---------------------------")
a = array([1,5,2,3,4,6,1])
print(a)
a1 = unique(a)
print(a1)
print(sort(a))

a = array([1,2,3,4,5])
b = array([0,2,2,7,5])

print("--- Comparing Arrays ---")
print(a==b)
print(a>b)
print(a<b)
print(any(a<b))
print(all(a<b))
print(logical_and(a>=1, a<=4))
print(logical_or(a>=1, a<=4))

c = where(a>b,a,b)
print(c)

c = nonzero(b)
print(c)          # Returns the Index where b[i] value in not 0
print(b[c])

print("----------- ALIAS -------------")
g = a               # share same memory location, g is not a new array. Gives a new name to array a
print(a)
print(g)
g[0] = 99
print(a)
print(g)

print("----------- VIEW -------------")
g=a.view()          # share different memory location : Shallow Copy
print(a)
print(g)
g[0] = 1
print(a)
print(g)

print("----------- COPY -------------")
g=a.copy()          # share different memory location : Deep Copy
print(a)
print(g)
g[0] = 99
print(a)
print(g)

print("----------- SLICING -------------")
print(a)
print(a[:])
print(a[::])
print(a[1:])
print(a[1:4])
print(a[:4])
print(a[0:4:2])
print(a[-4])
print(a[-4:])
print(a[-4:-1])
print(a[-1:-4:-1])
print(a[-2:-4:-1])
