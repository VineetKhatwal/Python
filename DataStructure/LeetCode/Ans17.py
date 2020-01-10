# Python3 implementation of the approach

from collections import deque
import itertools 
 
def letterCombinations(number): 
  
 
    map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    if not number:
        return None
    
    list1 = []
    res = [] 

    for i in number:
        list1.append(map[int(i)])

    combinations = []

    res = list(itertools.product(*list1))
    final = []
    for i in range(len(res)):
        temp = ""
        for j in range(len(res[i])):
            temp = temp + res[i][j]
        final.append(temp)
    print(final)
# Driver program 
number = [] 
  
letterCombinations(number)
