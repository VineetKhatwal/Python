''' A decotrator is a function that accepts a function as a paramater and
returns a function
Takes the result of a function, modifies it and returns it
Does the additional processing by a fuction'''

print ("--------------- DECOR ---------------")
def decor(fun):
    def inner():
        value = fun()
        #print("Val =",value)
        return value + 2
    #print("Inner =",inner)
    return inner

def num():
    return 10

print(num())
result = decor(num)
print(result())

print ("--------------- @ DECOR ---------------")

@decor
def num2():
    return 10
print(num2())

print ("--------------- 2 DECOR ---------------")
def decor(fun):
    def inner():
        value = fun()
        return value +2
    return inner

def decor1(fun):
    def inner():
        value = fun()
        return value * 2
    return inner

def num():
    return 10

print(num())
result1 = decor(num)
print(result1())
result2 = decor(decor1(num))
print(result2())
result3 = decor1(decor(num))
print(result3())


print ("--------------- @ 2 DECOR ---------------")

@decor
@decor1
def num2():
    return 10
print(num2())

@decor1
@decor
def num3():
    return 10
print(num3())
