def commonPrefix(strs):

    result = ""
        
    if not strs:
        return result
    
    l=len(strs)
        
    strs.sort()
    minLen = min(len(strs[0]),len(strs[l-1]))
        
    for i in range(minLen):
        if (strs[0][i] == strs[l-1][i]):
            result += strs[0][i]
        else:
            break

    return result
                   

arr = ["aac","ab"]
print(commonPrefix(arr))

arr = ["dog","racecar","car"]
print(commonPrefix(arr))

arr = []
print(commonPrefix(arr))

arr = [""]
print(commonPrefix(arr))
