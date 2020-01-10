s = "Welcome to \t python \n world"
print(s)

s = r"Welcome to \t python \n world"
print(s)

print(len(s))
print(s[5])

for i in s:
    print(i, end= " ")
print()

for i in s[::-1]:
    print(i, end= " ")
print()

print("------------USING WHILE LOOP-------------------")
i=0
while(i<len(s)):
      print(s[i], end= " ")
      i= i+1;
print()

i=1
while(i<=len(s)):
    print(s[-i], end= " ")
    i= i+1;
print()

i=len(s)-1
while(i>=0):
      print(s[i], end= " ")
      i= i-1;
print()



print("-------------------------------")
print("--------------- ",s, "------------------")
print(s[0:9:2])
print(s[:4:])
print(s[-4:-2])         # Prints element from -4 to -1
print(s[-1:-4:-1]) 
print(s[-4:-1]) 
print(s[-4:])
print(s[-4::])
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
s="Core Python"
print(s[-1:-4:-1])
print(s[-4:-1])
print(s[1:3]* 3)

# Checking Membership
s1 = "Vineet Khatwal"
s2 = "ina"
if s2 in s1:
    print("Present")
else:
    print("Not Present")

s = "   Vineet Khatwal   "
print(s)
print(s.lstrip())
print(s.rstrip())
print(s.strip())

print("------------------------------------")
s = "This is a book"
n = s.find("is")
print(n+1)

s = ["This", "is","a", "book"]
for i in range(len(s)):
	if ('is' == s[i]):
		print(i+1)

print("------------------------------------")
s = "This is a book"
n = s.find("is",5,10)
print(n+1)

n = s.index("is",5,10)
print(n+1)

found = False
n = len(s)
i=0
while (i < n):
    pos = s.find("is",i,n)
    if pos != -1:
        print("Position = ", pos+1)
        i=pos+1
        found = True
    else:
        i=i+1

if (found==False):
    print("Not found")
    
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

print(s)
n = s.count('is')
print(n)

n = s.count('is',0,len(s))
print(n)

n = s.count('is',5,len(s))
print(n)
    
s1 = 'one'
s2 = 'two'
print(s1,s2)
print(id(s1), id(s2))
s1=s2
print(s1,s2)
print(id(s1), id(s2))

str = "abcd"
print(str[0])
str[0]='A'
print(str[0])
    
    

