tup=(10,20,30,"Vineet",'t',89.8)
print(type(tup))
print(tup)

print("--------------- Tuple without braces ---------------")
tup = 1,2,3,4,5
print(type(tup))
print(tup)

print("--------------- Converting list into tuple ---------------")
list1 = [1,2,3,4,5]
print(type(list1))
print(list1)
tup = tuple(list1)
print(type(tup))
print(tup)


print("--------------- Using range ---------------")
tup = tuple(range(5,15,2))
print(tup)

print("--------------- Using Indexing ---------------")
print(tup[1])
print(tup[2])
print(tup[-1])
print(tup[-2])

for i in tup[::-1]:
    print(i, end=" ")
print()

print("--------------- Using Slicing ---------------")
print(tup[::])
print(tup[:])
print(tup[1:5])
print(tup[-4:-1])
print(tup[-1:-4:-1])
print(tup[-1:-4:-2])
print(tup[::2])
print(tup[::-2])

print("--------------- Operations on Tuples ---------------")
print(len(tup))
print(tup * 2)
tup = tup * 2
print(tup)
# tup.append(10)            : Error
tup2 = (98,99,100)
tup = tup + tup2
print(tup)
print(99 in tup)
print(max(tup))
print(min(tup))
print(tup.count(11))
print(tup.index(11))
print(sorted(tup))

print("--------------- Inserting Element in a Tuple ---------------")

x = (0,1,2,4,5,6,7,8,9)
print(x)
y= x[0:3]
print(y)
z = (3,)
y = y+z
print(y)
x= y +x[3::]
print(x)

x = x[0:3] + (100,) + x[3:]
print(x)

print("--------------- Modifying Elements of a Tuple ---------------")
x = (0,1,2,3,4,5,6,7,8,9)
print(x)
y= x[0:3]
print(y)
z = (33,)
y = y+z
print(y)
x= y +x[4::]
print(x)

x = x[0:3] + (100,) + x[4:]
print(x)

print("--------------- Deleting Elements of a Tuple ---------------")
x = (0,1,2,3,4,5,6,7,8,9)
print(x)
y= x[0:3]
print(y)
x= y +x[4::]
print(x)

x = x[0:3] + x[4:]
print(x)

print("-------------------------------------------------------------")

tup3=(1,2,3,4,tup2)
print(tup3)
#print(sorted(tup3))
