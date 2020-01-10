import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        c2 = c-1
        list = [] 
        for i in range(r):
            for j in range(c2,-1,-1):
                list.append(matrix[j][i])
                
        for i in range(r):
            for j in range(c):
                matrix[i][j]= list.pop(0)
        
        print(matrix)
        
