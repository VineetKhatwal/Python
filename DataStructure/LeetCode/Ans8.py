def myAtoi(str):

    str = str.strip(" ")
        
    if (not str[0].isnumeric() and str[0] not in['-','+']):
        return 0
    
    count = 0
    for i in range(len(str)):
        if (str[i].isnumeric() or str[i] in['-','+', '.']):
            count += 1
        
    str = str[0:count]
    
    if (int(str) < -2147483648):
        str = "-2147483648"

    if (int(str) > 2147483647):
        str = "2147483647"
        
    return str

print(myAtoi("42"))
print(myAtoi("    42"))
print(myAtoi("-42"))
print(myAtoi("+42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))

print(myAtoi("-2147483649"))
print(myAtoi("-2147483648"))
print(myAtoi("-2147483647"))

print(myAtoi("2147483646"))
print(myAtoi("2147483647"))
print(myAtoi("2147483648"))


