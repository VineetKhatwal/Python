def reverse(x): 

    s = str(abs(x))
    
    rev = int(s[::-1])
    if x <  0:
        rev = rev * -1

    if ((rev > 2147483647) or (rev < -2147483648)):
        rev = 0
            
    return rev   


print(reverse(123))
print(reverse(-123))
print(reverse(1534236469))
print(reverse(-1534236469))

