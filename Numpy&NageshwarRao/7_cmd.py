import sys

sum = int(sys.argv[1]) + int(sys.argv[2])
print ("Sum = ", sum)
args = sys.argv
print("The command line arguments are")
for a in args:
    print(a)
    
