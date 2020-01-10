import sys, os

fname = input("Please enter file name")
fname = "/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/" + fname

if os.path.isfile(fname):
    f = open(fname,'a+')
else:
    print("File not found")
    sys.exit()
    

#f = open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/File_New.txt",'a+')
print("Please enter your text with @ at the end")
while str != '@':
    str = input("Please enter your text")
    if str != '@':
        f.write(str + "\n")

f.seek(0,0)

print("-----------File Contents---------")
str = f.read()
print(str)
f.close()
