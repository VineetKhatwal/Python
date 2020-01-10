f = open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/File.txt",'w')
str = input("Please enter your name")
f.write(str)
f.close()


f = open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/File.txt",'r')
str = f.read()
print(str)
f.close()


f = open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/File_New.txt",'w')
print("Please enter your text with @ at the end")
while str != '@':
    str = input("Please enter your text")
    if str != '@':
        print(str)
        f.write(str + "\n")
f.close()

f = open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/File_New.txt",'r')
str = f.read()
print(str)
f.close()
