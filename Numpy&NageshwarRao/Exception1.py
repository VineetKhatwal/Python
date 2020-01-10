try:
    a,b = [int(x) for x in input("Please enter two numbers").split()]
    c = a/b
    print("{}/{} = {}".format(a,b,c))
except ZeroDivisionError:
    print("ZeroDivisionError occured")
    print("a = {}, b= {}".format(a,b))
finally:
    print("Ending the Program")


