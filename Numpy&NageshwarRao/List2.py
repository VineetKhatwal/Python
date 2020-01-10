a = [50,10]
a.sort()
print(a)
b = [3,5,1,a]
print(b)
'''b.sort()
print(b)'''

print("--------------------- Nested List ---------------------")
a = [40,50]
b = [10,20,30,a]
print(b)
print(a in b)
c = [60,70]
b.append(c)
print(b)

print("--------------------- Lists as Matrix ---------------------")
mat = [[1,2,3],[4,5,6],[7,8,9]]
print("Using for")
for i in mat:
    print(i)

print()

print("Using for with range and len")
for i in range(len(mat)):
    print(mat[i])

print()
print("Using for with index")

for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end=" ")
    print()

print("Adding the matrix - The wrong way")
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[10,20,30],[40,50,60],[70,80,90]]

mat3 = mat1 + mat2

for i in range(len(mat3)):
    for j in range(len(mat3[i])):
        print(mat3[i][j], end=" ")
    print()

print("Adding the matrix - The correct way")
mat4 = [3 * [0] for i in range(3)]
for i in range(3):
    for j in range(3):
        mat4[i][j] = mat1[i][j] + mat2[i][j]

for i in range(len(mat4)):
    for j in range(len(mat4[i])):
        print(mat4[i][j], end=" ")
    print()

emp = []
n = int(input("How many employee"))
for i in range(n):
    print("Please enter Id : ")
    emp.append(int(input()))
    print("Please enter Name : ")
    emp.append(input())
    print("Please enter Salary : ")
    emp.append(int(input()))

print(emp)

id = int(input("Please enter the employee id"))

for i in range(len(emp)):
    if id==emp[i]:
        print("Id = {}, Name ={}, Salary ={}".format(emp[i],emp[i+1],emp[i+2]))
