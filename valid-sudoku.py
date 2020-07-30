
def soln(A):
    def checkRowforElement(elementRow,elementCol,rowNum):
        for i in range(9):
            if(A[rowNum][i]==A[elementRow][elementCol] and i!=elementCol and A[rowNum][i]!='.'):
                print("ROW",A[rowNum][i],A[elementRow][elementCol])
                return False
        return True
    def checkColumnforElement(elementRow,elementCol,colNum):
        for i in range(9):
            if(A[i][colNum]==A[elementRow][elementCol] and i!=elementRow and A[i][colNum]!='.'):
                print("COL",A[i][colNum],A[elementRow][elementCol])
                return False
        return True
    
    def checkGridforElement(elementRow,elementCol,gridNum):
        for i in range(1,4):
            for j in range(1,4):
                rowID=(i-1)+gridNum*3
                colID=(i-1)+gridNum
                if(A[rowID][colID]==A[elementRow][elementCol]):
                    print("GRI",A[i][j],A[elementRow][elementCol])
                    return False
    grid_hsx={}
    for i in range(9):
        for j in range(9):
            if(not checkRowforElement(i,j,i)):
                print("ROWCHECK")
                return False
            if(not checkColumnforElement(i,j,j)):
                print("COLCHECK")
                return False
    return True
if __name__ == "__main__":
    print(soln(["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
))