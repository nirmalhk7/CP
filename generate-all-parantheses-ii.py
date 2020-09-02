
def soln(A):
    answer= []
    def recursive(headCount=0,tailCount=0,opx=""):
        if(headCount<A):
            recursive(headCount+1,tailCount,opx+"(")
        if(tailCount<A and tailCount<headCount):
            recursive(headCount,tailCount+1,opx+")")
        if(headCount>=A and tailCount>=A):
            answer.append(opx)
    recursive()
    return answer
    pass
if __name__ == "__main__":
    print(soln(4))