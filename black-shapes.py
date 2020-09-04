
def soln(A):
    possibilities=[]
    possibilitiesCount=0 
    visitedX={}
    r= len(A)
    c= len(A[0])

    def checkFeasible(A,i,j,answer=[]):
        if(r>i>=0 and c>j>=0):
            if(A[i][j]=="X" and (i,j) not in visitedX):
                # print("Checking Neighbors for A",i,j,A[i][j])
                visitedX[(i,j)]=True
                answer.append((i,j))
                checkFeasible(A,i-1,j,answer)
                checkFeasible(A,i+1,j,answer)
                checkFeasible(A,i,j-1,answer)
                checkFeasible(A,i,j+1,answer)
                # print(answer,"VAL")
                return answer
        return None

    for i in range(r):
        for j in range(c):
            val= checkFeasible(A,i,j)
            # input("Checking A["+str(i)+"]["+str(j)+"]="+str(A[i][j]))
            if(val):
                # print(val)
                possibilitiesCount+=1
                del val
    return possibilitiesCount

if __name__ == "__main__":
    A = ["OOOXOOO","OOXXOXO","OXOOOXO"  ]
    print(soln(A))