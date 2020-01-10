print("Creating list with square of first ten numbers")
squares = []
for x in range(1,11):
    squares.append(x*x)
print(squares)

squares = [x*x for x in range(1,11)]
print(squares)

print("Creating list with even square of first ten numbers")

squares = []
for x in range(1,11):
    if (x*x % 2 ==0):
        squares.append(x*x)
print(squares)

squares =[x*x for x in range(1,11) if x%2 == 0]
print(squares)

print("Adding each element of two lists to a third list")
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = []

for i in a:
    for j in b:
        c.append(i+j)

print(c)
