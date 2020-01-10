str ="one,two,three,four"
print(str)
print(type(str))
str = str.split(',')            # The pieces are returned as a list
print(str)
print(type(str))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
str = "-".join(str)
print(type(str))
print(str)

str =("one","two","three","four")
print(type(str))
print(str)
str = "-".join(str)
print(type(str))
print(str)

str = "This is Python"
print(str.upper())
print(str.lower())

str = "This is Python"
print(str.swapcase())
print(str.title())
print(str.startswith("This"))
print(str.endswith("Python"))

name = "Ketan"
id = 1
sal = 10000
str = "Hi {}, id: {}, your first sal is {}".format(name,id,sal)
print(str)
str = "Hi {2}, id: {1}, your first sal is {0}".format(name,id,sal)
print(str)
str = "Hi {:<10s}, id: {:>5d}, your first sal is {:^10.2f}".format(name,id,sal)
print(str)
str = "Hi {:*<10s}, id: {:*>5d}, your first sal is {:*^14.2f}".format(name,id,sal)
print(str)

str=["Nainital","Bhimtal","Haldwani","Bhiwani"]
print(type(str))
str=sorted(str)
print(str)

print("------------------------------------")
s = "This is a book"
n = s.find("is")
print(n+1)

s = ["This", "is","a", "book"]
for i in range(len(s)):
    if ('is' == s[i]):
        print(i+1)

print("------------------------------------")
