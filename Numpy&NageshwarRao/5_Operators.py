list = [10, -20, "Ketan", 'Vineet', 10]
for i in list:
	print(i)

print("--------------------------")

map = {10:'Kamal',11:'Pranav',12:'Amol',13:"Kunal"}

for number in map:
	print(number,map[number])
	
a = 34
print("Memory Location  =" , id(a))
b = 34
print("Memory Location  =" , id(b))

print("'is' operator is used to compare whether two objects are same or not")

if (a is b):
	print("Same Identity")
else:
	print("Not Same")
	
a=[1,2,3,4]
b=[1,2,3,4]

if (a is b):
	print("Memory Location  =" , id(a), " ", id(b))
	print("Same Identity")
else:
	print("Memory Location  =" , id(a), " ", id(b))
	print("Not Same")
	
if (a == b):
	print("Memory Location  =" , id(a), " ", id(b))
	print("Same Identity")
else:
	print("Memory Location  =" , id(a), " ", id(b))
	print("Not Same")
	
print("City name ="+"Nainital")			# '+' will not have space between 'City name =' and 'Nainital'
print("City name =","Nainital")			# ',' will have space between 'City name =' and 'Nainital'
a=2
b=4
print(a,b)
print(a,b, sep="_")

print("Hello")
print("Vineet Khatwal")

print("Hello", end=' ')
print("Vineet Khatwal")