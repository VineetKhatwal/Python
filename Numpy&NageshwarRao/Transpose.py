from numpy import*

a = matrix('1 2 3; 4 5 6; 7 8 9')
b = matrix('9 8 7; 6 5 4; 3 2 1')
c = a+b
d = a-b
e = a/b
f = a*b
print(a)
print()
print(b)
print()
print(c)
print()
print(d)
print()
print(e)
print()
print(f)
print()

r,c = [int(a) for a in input("Enter Row and Column").split()]
print("Please enter the ", r * c, "elements of the matrix");
str = input();
#a = reshape(matrix(str),(r,c))
a = matrix(str)
print(a)
a = a.reshape(r,c)
print(a)
a=transpose(a)
print(a)


