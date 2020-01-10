f1 = open ("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/Rumi.png",'rb')
f2 = open ("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/New.png",'wb')

bytes = f1.read()
f2.write(bytes)

f1.close()
f2.close()


with open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/With.txt",'w') as f:
    f.write("Python Programming \n")
    f.write("Python is amazing \n")

with open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/With.txt",'r') as f:
    for line in f:
        print(line)
