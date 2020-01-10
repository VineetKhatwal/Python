def romanToInt(s):

    convertedValue = 0
    
    i = 0
    
    dictRoman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res = 0

    while (i < len(s)):
        s1 = dictRoman[s[i]]
        if (i+1 < len(s)):
            s2 = dictRoman[s[i+1]]
            if s1 >= s2:
                res = res + s1
            else:
                res = res + s2 - s1
                i = i+1
        else:
            if (i<len(s)):
                res = res + s1
        i = i +1
        
    return res
print(romanToInt("MCDLXXVI"))
print(romanToInt("XXIX"))
print(romanToInt("MCDLXXIX"))
