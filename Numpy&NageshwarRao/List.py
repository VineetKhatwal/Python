student = [1,2,3,4,5]
print(student)

lst = list(range(10))
print(lst)

lst = list(range(0,9))
print(lst)

lst = list(range(0,9,2))
print(lst)

student = []
student.append(10)
student.append("Vineet")
student.append('M')
student.append(57)
student.append(75)
student.append(81)
student.append(78)
student.append(70)
print(student)

print("------------ Indexing ----------------")
print(student[1])

for i in student:
    print(i, end = " ")
print()

print("**********")
for i in range(len(student)):
    print(student[i], end = " ")
print()

print("------------ Slicing ----------------")

print(student[:])
print(student[::])
# print(student[:,:])  => For 2-D array

print(student[0:3])
print(student[0:3:1])
print(student[:3:])

print("------------ Range ----------------")

list1 = list(range(0,10,1))
print(list1)
for i in list1:
    print(i, end=" ")
print()

list1 = list(range(4,9,2))
for i in list1:
    print(i, end=" ")
print()

i = 0
while (i<len(list1)):
    print(list1[i], end= " ")
    i=i+1
print()

print("------------ Updating the List  ----------------")
list1 = list(range(0,10,1))
print(list1)

print("-----Appending-----")

list1.append(10)
print(list1)


list1[0]=10
list1[1:3]=12,13
print(list1)


print("-----Deleting-----")

del list1[1]            # Deleted the element at the index
print(list1)

# del list1[15]         Out of index error

print("-----Removing-----")

list1.remove(9)         # Remove the element specified
print(list1)

# list1.remove(19)      Element not in list : Value Error

print("-----Reversal-----")

list1.reverse()
print(list1)

i = len(list1)
while(i>0):
    print(list1[i-1], end= " ")
    i=i-1
print()

for i in list1[::-1]:
    print(i, end= " ")
print()

print("-----Concatenation-----")
print(list1 + list1)

print("-----Repetition-----")
print(list1 * 3)

print("-----Membership-----")
print(9 in list1)
print(8 in list1)

print("-----Alias-----: Shallow Copy")
list2 = list1
print(list1)
print(list2)
list1.append(7)
print(list1)
print(list2)

print("-----Cloning-----: Deep Copy")
list3 = list1[:]
print(list1)
print(list3)
list1.append(25)
print(list1)
print(list3)

print("-----Copying-----: Deep Copy")
list4= list1.copy()
print(list1)
print(list4)
del list1[3]
print(list1)
print(list4)

print("----------- LIST METHODS ------------")
list1.insert(2,45)
print(list1)
print(list1.index(45))
list1.append(7)
print(list1)
print(list1.count(7))
list1.remove(7)              # Removes the first occurence
print(list1)
print(list1.count(7))
print("-----------------")
print(list1.pop())
print(list1)
print(list4)
print("----- Extended List -----")
list1.extend(list4)
print(list1)
list4.sort()
print(list4)
list4.reverse()
print(list4)
print(min(list4))
print(max(list4))

print("----------- Finding Maximum ------------")
list1.append(-43)
list1.append(7)
print(list1)
max = 0
min = 0
for i in list1:
    if i > max:
        max = i
    if i < min:
        min = i
print(max)
print(min)

print(list1.count(7))
num = 7
count =0
for i in list1:
    if i == num:
        count += 1
print(count)

print("---------- INTERSECTION --------")
print(list3)
print(list4)
set1=set(list3)
set2=set(list4)
set3=set1.intersection(set2)
print(set3)





