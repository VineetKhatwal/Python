import array

x= array.array('i',[])
print("How many elements in the array")
n = int(input())
for i in range(n):
    print("Enter element ", i+1)
    x.append(int(input()))
print(x)

for i in range(n-1):
	for j in range(n-1-i):
		if x[j] > x[j+1]:
			t = x[j]
			x[j] = x[j+1]
			x[j+1] = t
print(x)

num = int(input("Please enter the number to be searched"))
found = False

for i in range(n):
	if (x[i]==num):
		print("Element found at position", i+1)
		found = True
		break
	
if (found == False):
	print("Element not found")
	
try:
	pos = x.index(num)
	print("Found at pos = ", pos+1)
	
except ValueError:
	print("Element not found")

	
