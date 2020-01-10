# A function to add two numbers
def sum(a,b):
    """ This function finds sum of two numbers """ # Docstring
    print("Sum = ", a+b)

sum(10,25)
sum(34.5,45.6)
sum("Ketan","Khatwal")

print("---------------------------")

# A function to find factorial
def fact(a):
    """ This function finds factorial of a number """ # Docstring
    num = 1
    for i in range(a):
        num = (i+1) * num
        print("Factorial of {} is {}".format(i+1,num))
    return num

f = fact(10)
print("Factorial =", f)

print("---------------------------")

# A function to find if a number is prime
def primeNum(num):
    """ This function finds if a number is prime""" # Docstring
    count = 0
    for i in range(num):
        if (num % (i+1) ==0):
            count = count +1
            
    if (count == 2):
        print("{} is a prime number".format(num))
    else:
        print("{} is not a prime number".format(num))
    

num = int(input("Please enter a number"))
primeNum(num)

print("---------------------------")

# A function to generate n prime numbers
def primeNum(a):
    """ This function finds if a number is prime""" # Docstring
    count = 0
    for i in range(a):
        if (a % (i+1) ==0):
            count = count +1
            
    if (count == 2):
        return True
    else:
        return False
    

def primeGenerator(num):
    i = 2
    count = 1
    while True:
        if (primeNum(i)):
            print(i)
            count=count+1
        i=i+1
        if (count>num):
            break
    

num = int(input("How many prime numbers"))
primeGenerator(num)

# return a,b,c => Values are returned as Tuple
# x,y,z = function()

def sum_sub(a,b):
    c = a+b
    d = a-b
    e = a*b
    f = a/b
    return c,d,e,f

w,x,y,z=sum_sub(10,5)
print(w,x,y,z)
