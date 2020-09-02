
def soln(A):
    def isSafe(board,row,col):
        for i in range(col):
            if board[row][i]==i: return False
        for i,j in 
    def recursive(board,col):
        if(col>=A):
            return True
        
        for i in range(A):
            if isSafe(board,i,col):
                board[i][col]=1

    board = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ] 
    if recursive(board,0)==False:


    pass

if __name__ == "__main__":
    print(soln(4))