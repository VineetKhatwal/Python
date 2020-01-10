def isValidSudoku(self, board):

    list1 = []
    list2 = []
    k =0
    l =0
        
    for i in range(9):
        for j in range(9):
            if ((board[i][j] in list1) or (board[j][i] in list2)):
                return False
            elif (board[i][j].isnumeric() and board[j][i].isnumeric()):
                list1.append(board[i][j])
                list2.append(board[j][i])
            elif (board[i][j].isnumeric()):
                list1.append(board[i][j])
            elif (board[j][i].isnumeric()):
                list2.append(board[j][i])
                    
        list1 = []
        list2 = []
    
    
    while( k < 9):
        l=0
        while( l < 9):
            for i in range(k,k+3):
                for j in range(l, l+3):
                    if (board[i][j] in list1):
                        return False
                    elif (board[i][j].isnumeric()):
                        list1.append(board[i][j])
            list1 = []
                    
            l = l + 3
        k = k + 3
            
    return True
                
        
