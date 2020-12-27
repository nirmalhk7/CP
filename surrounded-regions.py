# Medium Difficulty: Couldnt do. Incompleted Status.
def soln(board):
    brow=len(board)
    if(brow>=3): 
        bcol=len(board[0])
        if(bcol>=3):
            def isOnBorder(i,j):
                return i==brow-1 or j==bcol-1
            def connectedToBorderZero(i,j):
                if(0<i<brow and 0<j<bcol):
                    if(board[i][j]=='X'):
                        return False
                    if(isOnBorder(i,j) and board[i][j]=='O'):
                        return True
                    else:
                        return connectedToBorderZero(i-1,j) or connectedToBorderZero(i+1,j) or connectedToBorderZero(i,j-1) or connectedToBorderZero(i,j+1)
                return False
            for i in range(1,brow-1):
                for j in range(1,bcol-1):
                    if(board[i][j]=='O'):
                        print(board[i][j],i,j)
                        top= board[i-1][j]=='O' and isOnBorder(i-1,j)
                        bottom= board[i+1][j]=='O' and isOnBorder(i+1,j)
                        left= board[i][j-1]=='O' and isOnBorder(i,j-1)
                        right= board[i][j+1]=='O' and isOnBorder(i,j+1)
                        if(not(top or bottom or left or right)):
                            board[i][j]='X'
                        print(board[i][j],connectedToBorderZero(i,j))
            return board
# print(soln([["X", "X", "X", "X"], ["X", "O", "O", "X"],
#             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
print(soln([["O","X","X","O","X"],
            ["X","O","O","X","O"],
            ["X","O","X","O","X"],
            ["O","X","O","O","O"],
            ["X","X","O","X","O"]]
))
