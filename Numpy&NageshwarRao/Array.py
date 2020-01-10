# Array :   Similar to List:    Faster than List   :    Store only one data type
#           Grow or shrink dynamically
import array

a = array.array('i', [4,6,2])
print(a)
for i in a:
    print(i)

print("--------------------")
arr1 = array.array('d',[1.5,2.5,-3.5,4])
for i in arr1:
    print(i)

print("--------------------")
arr2 = array.array(arr1.typecode,(a * 2 for a in arr1))
for i in arr2:
    print(i)

print("--------------------")
c = array.array('u',['a','b','c','d'])
for i in c:
    print(i)

print("--------------------")
x = array.array('i',[23,45,21,56,43,45,65])
n = len(x)
for i in range(n):
    print(x[i], end=" ")

print()
print("--------------------")
i=0
while(i<n):
    print(x[i],  end=" ")
    i=i+1;

print()
print("---------Y------------")

y = x
print(y)

# Slicing : The below code extracts from index 1 to index 3
y = x[1:4]
print(y)

y = x[2:]
print(y)

y = x[:3]
print(y)

y = x[-4]
print(y)

y = x[-4:]
print(y)

y = x[-4:-1]
print(y)

y = x[0:5:2]
print(y)

for i in x[2:5]:
    print(i)


