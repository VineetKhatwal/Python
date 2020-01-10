import sys, os

fname = input("Please enter file name")
fname = "/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/" + fname

if os.path.isfile(fname):
    f = open(fname,'r')
else:
    print("File not found")
    sys.exit()

cl = cw = cc = 0

for line in f:
    cl += 1
    cc += len(line)
    words = line.split()
    #print(words)
    cw += len(words)

print("Lines =",cl)
print("Words =",cw)
print("Characters =",cc)
    
