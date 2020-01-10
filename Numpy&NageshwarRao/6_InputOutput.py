x = 10
print("X = %i" % x)
y = 20
print("X = %5i Y = %8i" % (x,y))
print("X = %5i Y = %5i" %(x,y))

name = "Neha Parmar"
print("Name = %s" % name)
print("Name = %20s" % name)				# RIGHT Aligned
print("Name = %-20s" % name + "_")			# LEFT Aligned
print("Name = %c, %c" % (name[0] , name[5]))
print("Name = %s" % (name[0:6]))

a = 123.123456789
print("Number = %f" %a)
print("Number = %.4f" %a)
print("Number = %5.5f" %a)

# USING REPLACEMENT FIELD
n1, n2, n3 = 1,2,3
print('number1={0}'.format(n1))
print('number1={0}, number2={1}, number3={2}'.format(n1,n2,n3))
print('number1={}, number2={}, number3={}'.format(n1,n2,n3))
print('number1={2}, number2={1}, number3={0}'.format(n1,n2,n3))

str = input()
print("Hello %s " % str)

str = input ("Please enter you name")
print("Hello %s " % str)

str = input("Enter a number")
x = int(str)
print("Number = %i"  % x)

x = int(input("Enter a number"))
print("Number = %i"  % x)

x = int(input("Enter a number"))
y = int(input("Enter a number"))
print("Numbers = ",  x,y,sep=",")
print("Numbers = %i %s %i " % (x,",",y))
print("Numbers = {} , {} ".format(x,y))

print("-------------------")
print("The sum of", x,"and", y,"is =", (x+y)); 
print('The sum of {} and {} is = {}'.format(x,y,x+y))
print('The product of {} and {} is = {}'.format(x,y,x*y))
print('The sum of {0} and {1} is = {2} and the product of {0} and {1} is = {3}'.format(x,y,x+y,x*y))

# Accepting more tha one input

x,y,z = [int(x) for x in input("Please enter three numbers").split()]
print("Sum = {}".format(x+y+z))

a,b,c = [int(x) for x in input("Enter three numbers: ").split()]
print("Sum = {}".format(a+b+c))