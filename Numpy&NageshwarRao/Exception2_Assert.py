try:
    x = int(input("Please enter a number between 5 and 10"))
    assert x>=5 and x<=10
    print("Valid Number")
except AssertionError:
    print("AssertionErrror occured")
    print("Invalid Number")
finally:
    print("Ending the Program")


