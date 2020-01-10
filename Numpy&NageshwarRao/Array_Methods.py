from array import *

arr = array('i',[10,20,30,40,50])
print(arr)
arr.append(30)
arr.append(60)
print(arr)
print(arr.count(30))
arr.insert(1,15)
print(arr)
arr.remove(15)
print(arr)
n = arr.pop()
print("Popped Element : ", n)
print(arr)
n = arr.index(30)
print("Index of 30    : ", n)
arr.reverse()
print(arr)
lst = arr.tolist()
print(lst)
print(arr)
lst.append("TEST")
print(lst)

x = array('i',[60,70,80,90,100])
arr.extend(x)
print(x)
print(arr)

a,b,c = [int(x) for x in input("Enter three numbers: ").split()]
print("SUM = ",(a+b+c))
'''
str = input("Enter the marks").split(' ')
marks = [int(num) for num in str]
'''
marks = [int(num) for num in input("Enter the marks").split(' ')]
sum = 0
for i in marks:
    sum = sum+i
n = len(marks)
print("SUM      : ", sum)
print("Average  : ", sum/n)

