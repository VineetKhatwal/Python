import math
r = float(input("Please enter the radius"))
area = math.pi * r ** 2
print("Area of circle = ", area)
print("Area of circle = {}".format(area))
print("Area of circle = {:7.4f}".format(area))

str = "Yes"
if (str == "Yes"):
    print("Yes")
    print("Thanks")
else:
    print("No")
    print("Thank You")
print("Goodbye")

x = 1
while (x<=10):
    print(x, end= " ")
    x= x+1
print()

print("End", end= " ")
print("End2")

m,n = [int(x) for x in input("Enter the min and max range").split(',')]
x = m
while x>=m and x<=n:
    if(x%2 == 0):
        print(x)
    x=x+1

str = "Hello"
for i in str:
    print(i, end= " ")
print()

for i in range(10,1,-2):
    print(i)

list = [1,2,3,4,5]
sum=0
for i in list:
    sum = sum + i;
print(sum)

i=0
sum = 0
while (i < len(list)):
    sum = sum + list[i]
    i = i+1
print(sum)

for i in range(3):
    for j in range(4):
        print(i,j)

for i in range(1,11):
    for j in range(1,i+1):
        print("* ", end="")
    print()

for i in range(1,11):
    print('* ' * i)

n = 20
for i in range(1,11):
    print(" " * (n-i) + "* " * i)

for i in range(1,11):
    for j in range(1,11):
        print("{:8}".format(i*j), end=" ")
    print()

for i in range(-10,11):
    if (i==8):
        break
    elif (i==5):
        continue
    elif (i<0):
    	pass
    else:
        print(i)

        
        


    
