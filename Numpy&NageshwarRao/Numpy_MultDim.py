from numpy import *

print("--------- 1D - Array ---------")
arr1D = array([1,2,3,4,5,6])
print(arr1D)

print("--------- 2D - Array ---------")
arr2D = array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
print(arr2D)

print("--------- 3D - Array ---------")
arr3D = array([[[1,2,3],[2,3,4],[3,4,5]],
               [[2,3,4],[3,4,5],[4,5,6]]])
print(arr3D)

print("--------- NDIM tells the array dimension ---------")
print(arr1D.ndim)
print(arr2D.ndim)
print(arr3D.ndim)

print("--------- SHAPE ---------")
print(arr1D.shape)
print(arr2D.shape)
print(arr3D.shape)

arr2D.shape =(3,4)
print(arr2D)
arr2D.shape =(2,6)
print(arr2D)
arr2D.shape =(6,2)
print(arr2D)

print("--------- SIZE ---------")
print(arr1D.size, arr2D.size, arr3D.size)

print("--------- DTYPE ---------")
print(arr1D.dtype, arr2D.dtype, arr3D.dtype)

print("--------- NBYTE ---------")
print(arr1D.nbytes, arr2D.nbytes, arr3D.nbytes)

print("--------- RESHAPE ---------")
print(arr1D)
arr1D = arr1D.reshape(3,2)
print(arr1D)
print(arr2D)

print("--------- FLATTEN ---------")
arr3D = arr3D.flatten()
print(arr3D)
arr3D = arr3D.reshape(6,3)
print(arr3D)
arr3D = arr3D.reshape(3,2,3)
print(arr3D)

print("--------- INDEXING in mult dim array ---------")
arr1D = array([1,2,3,4,5,6,7,8])
for i in range(len(arr1D)):
    print(arr1D[i], end =" ")
print()

print("--------  2D Array ---------")

arr2D = array([[1,2,3,4],[5,6,7,8]])
print(len(arr2D))

for i in range(len(arr2D)):
    print(arr2D[i])

print("--------  2D Array New ---------")
for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        print(arr2D[i][j], end = " ")
    print()

print("--------  3D Array ---------")
arr3D = array([[[1,2,3],[2,3,4],[3,4,5]],
               [[2,3,4],[3,4,5],[4,5,6]]])

for i in range(len(arr3D)):
    for j in range(len(arr3D[i])):
        for k in range(len(arr3D[i][j])):
            print(arr3D[i][j][k], end = " ")
        print()
    print()

arr2D = arr2D.reshape(4,2)
print(arr2D)
print("--------- SLICING -----------")
print("------- 2D --------")
print(arr2D[::])
print(arr2D[:])
print(arr2D[:,:])
print("------- 1D --------")
print(arr1D[::])
print(arr1D[:])
#print(arr1D[:,:])    For two dimensional matrix only

print("^^^^^^^^^^^^^^^^^^^^")

print(arr2D[0:])
print()
print(arr2D[2:])
print()
print(arr2D[3:])

print("----- Displaying one row --------")
print(arr2D[0,:])
print(arr2D[3,:])

print("----- Displaying one column --------")
print(arr2D[:,0])           # Displays as a Row
print(arr2D[:,1])

print("----- Displaying one Cell --------")
print(arr2D[1,1])
print(arr2D[3,0])

a = arange(11,36,1)
print(a)
a = a.reshape(5,5)
print(a)

print()
print("########################################")
a = arange(11,36,1).reshape(5,5)
print(a)
print()
print(a[1,:])
print()
print(a[:,1])
print()
print(a[2,2])
print()
print(a[0:2])
print()
print(a[0:2,0:3])
print()
print(a[2:4,3:])
print()
print(a[2:,2:])

