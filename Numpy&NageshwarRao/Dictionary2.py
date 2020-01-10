print("Number of occurences of characters in a String")
dict1 ={}
str = "Book"
for i in str:
    dict1[i] = dict1.get(i,0) + 1

for k,v in dict1.items():
    print("Key = {} \t {} occurence = {}".format(k,k,v))


print("---------------Converting Lists into Dictionary----------------")
country = ["USA","India","Germany"]
capital = ["Washington","New Delhi","Berlin"]
z = zip(country,capital)
d = dict(z)
print("{:10s} --- {:15s}".format("COUNTRY","CAPITAL"))
print("{:10s} --- {:15s}".format("-------","-------"))
for k in d:
    print("{:10s} --- {:10s}".format(k,d[k]))


print("---------------Converting String into Dictionary----------------")
str = "USA=Washington,India=New Delhi,Germany=Berlin"
lst=[]
for x in str.split(','):
    y = x.split('=')
    print(y)
    lst.append(y)

print(lst)

d = dict(lst)
print(d)

print("------------- Passing Dict to function -----------")

def dict_func(dict):
    for i,j in dict.items():
        print(i,j)
        
dict_func(d)

print("------------- Sorting using Lambda -----------")

color = {"Red":5,"Green":1,"Blue":2,"Black":6}

d1 = sorted(color.items(), key = lambda t : t[0])
print(d1)

d1 = sorted(color.items(), key = lambda x : x[1])
print(d1)
        
dict1 = {}
num = int(input ("How many Players"))
for i in range(num):
    key = input("Please enter player's Name : ")
    value = int(input("Please enter player's Score : "))
    dict1.update({key:value})

print(dict1)



print("------------ Using Loops in Dictionary --------------")
for x in dict1:
    print(x, end = " ")
print()

print("**********-------------********")
for x in dict1.keys():
    print(x, end = " ")
print()

for x in dict1.values():
    print(x, end = " ")
print()

for x in dict1.items():
    print(x, end = " ")
print()

name = input("Please enter the name of the player")

print(dict1.get(name,"Not Found"))
                
