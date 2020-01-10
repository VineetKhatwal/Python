f1 = 0
f2 = 1
num = int(input("Please enter the range"))
for i in range(num):
    c = f1+f2
    f1 = f2
    f2 = c
    print(c)


print("------------ SIN Series------------")
x,n = [int(i) for i in input("Enter angle value, no of iterations").split(',')]
r = (x*3.14159)/180
# First Term
t = r
sum = r
print("Iteration= {} \t Sum = {}".format(1,sum))
i=2
for j in range(2,n+1):
    #print(j)
    t = (-1) * t * r *r /(i*(i+1))
    sum = sum +t
    print("Iteration= {} \t Sum = {}".format(j,sum))
    i = i+2
