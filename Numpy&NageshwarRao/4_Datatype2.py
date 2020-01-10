''' Bytes : Range : 0-255 +ve and -ve
Can't change value once assigned : It will throw error
'''

ele = [10, 20, 30, 40, 50]
print(type(ele))
x = bytes(ele)
print(x[0])
print(type(x))
for i in x:
    print (i)

'''
x[0] = 67    # Throws Error

for i in x:
    print (i)

'''

''' bytearray : similar to bytes but can be modified
'''
print('-------')

y = bytearray(ele)
for i in y:
    print (i)

y[0] = 67

for i in y:
    print (i)


# List : Similar to Array : Can grow dynamically : Can store different data type
# : List can be modified

list = [10, -20, "Ketan", 'Vineet', 10]
print('-------')
print(list)
print('-------')
print(list[1:3])
print('-------')
print(list[2:])
print('-------')
print(list[-2])
print('-------')
print(list * 2)
list[1] = 200
print('-------')
print(list)
list.append(34)
print(list)
'''list.add(44)			# list.add => Throws error
print(list)'''
list.remove(34)
print(list)

print("*********  ^^^^^^^^^^^^ ***********")
for i in list:
	print (i)
# Tuple : Similar to List : Tuples can't be modified

print("--------- TUPLE ------------")

tpl = (10, -20, "Ketan", 'Vineet')
print(type(tpl))
print('-------')
print(tpl)
print('-------')
print(tpl[1:3])
print('-------')
print(tpl[2:])
print('-------')
print(tpl[-2])
print('-------')
print(tpl * 2)
#tpl[1] = 200      # Tuple should not be modified
print('-------')
print(tpl)

print("----------- RANGE -----------")
r = range(23,45,3)
print(r)
for i in r:
    print (i,end=" ")
print()
    
r = range(1,10)
print(r)
for i in r:
    print (i, end=" ")
print()

# SET : Unordered list of element : Can't have duplicate : Set and Frozen Datatype
# Doesn't support assignment s[2] = 5 : Throws error 

print("-----------  SET --------------")
s = {1,2,3,4,5,1,2}
print(s)

ch = set("Hello")
print(ch)

print(list)
s = set(list)       # Duplicate from list are removed
print(s)

# print(s[2:])      # Can't rertieve elements using indexing

s.update([3,"TEST",1000])    # To update a set
print(s)

s.remove(3)    
print(s)

s.add("TESTER")
print(s)

# Frozen set is similar to set Datatype but cant be modified

''' MAP : Holds key - value pair
'''
print("-----------  MAP --------------")

d = {10:'Kamal',11:'Pranav',12:'Amol'}
print(d)
print(d[10])
d[10]='Hitesh'
print(d[10])
print(d.keys())
print(d.values())
print(d.items())
del(d[12])
print(d)

a = 15
print(type(a))
a=15.5
print(type(a))
a= "Vineet"
print(type(a))
a ='e'
print(type(a))
print(type(s))
print(type(list))
print(type(tpl))
print(type(d))
print(a[0].isupper())

# CONSTANT : Not available in Pyhton. Declare is upper case to define its constant

TEST = 45
print(TEST)
TEST = 56
print(TEST)

num = -10
print (num)
print (-num)

x= 100
y = 200
print(x and y)
print(y and x)

print(x or y)
print(y or x)

print(not x)
print(not y)

