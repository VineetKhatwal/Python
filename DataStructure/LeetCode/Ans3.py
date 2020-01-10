import math


def lengthOfLongestSubstring(s):
    count = 0
    maxCount = 0
    q = []
    for i in s:
        if i not in q:
            count = count+1
            print("Counter1",count)
            q.append(i)
        else:
            ind = q.index(i)
            for j in range(ind+1):
                if (len(q) > 0):
                    q.pop(0)
                    count = count-1
                    print("Counter2",count)
            q.append(i)
            count = count+1
            print("Counter3",count)
            print(q)
            
        maxCount=max(maxCount,count)

    return(maxCount)

print(lengthOfLongestSubstring("bbbbb"))
#lengthOfLongestSubstring("bcbb")
