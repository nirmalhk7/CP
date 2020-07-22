
def soln(board,word):
    def getAdjacent(board,i,j):
        arx= {}
        if i>0:
            arx[(board[i-1][j])]=True
        if j>0:
            arx[(board[i][j-1])]=True
        if i<=len(board)-2:
            arx[(board[i+1][j])]=True
        if j<=len(board[0])-2:
            arx[(board[i][j+1])]=True
        arx['used']=False
        return arx
    wordhsx= {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] not in wordhsx:
                wordhsx[board[i][j]]= getAdjacent(board,i,j)
            else:
                wordhsx[board[i][j]].update(getAdjacent(board,i,j))
    # print(wordhsx)
    for i in range(0,len(word)-1):
        # print(i,word[i],word[i+1],"1",word[i] not in wordhsx)
        # print(i,word[i],word[i+1],"2",word[i+1] not in wordhsx)
        # print(i,word[i],word[i+1],"3",word[i+1] not in wordhsx[word[i]])
        if word[i] not in wordhsx or word[i+1] not in wordhsx:
            # print("Letter not in")
            return False
        elif word[i+1] not in wordhsx[word[i]]:
            # print("Letter not in dict",word[i],word[i+1],wordhsx[word[i]])
            return False
        elif wordhsx[word[i]]['used']==True or wordhsx[word[i+1]]['used']==True:
            print("Reepated",word[i])
            return False
        else:
            # print("True",word[i],word[i+1],wordhsx[word[i]])
            wordhsx[word[i]]['used']=True
    return True
    # return wordhsx

if __name__ == "__main__":
    board =[['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']]
    print(soln(board,"ABCCED"))
    # print(soln(board,"ABCB"))