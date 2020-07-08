
def soln(A):
    result = 0
    for i in range(len(A)):
        print("SVERT",range(1,len(A[0])-1),result)
        print("SHORI",range(1,len(A)-1),result)
        input()
        for j in range(len(A)):
            if(A[i][j]==1):
                print("A["+str(i)+"]["+str(j)+"]=1")
                #  Strictly left/right edges are beaches
                if(j>0):
                    result+= int(A[i][j-1]==0)
                    print(result,"SVERTL",int(A[i][j-1]==0))
                
                if(j<len(A)-1):
                    result+= int(A[i][j+1]==0)
                    print(result,"SVERTR",int(A[i][j+1]==0))
                if(i>0):
                    result+= int(A[i-1][j]==0)
                    print(result,"SHORIT",int(A[i-1][j]==0))

                if(i<len(A)-1):
                    result+= int(A[i+1][j]==0)
                    print(result,"SHORIB",int(A[i+1][j]==0))

                if(i==0 or i==len(A)-1):
                    result+= int(i==0)+int(i==len(A)-1)
                    print(result,"BORDTB",int(i==0 or i==len(A)-1))
                
                if(j==0 or j==len(A[i])-1):
                    result+= int(j==0)+int(j==len(A[i])-1)
                    print(result,"BORDLR",int(j==0 or j==len(A[i])-1))
    return result

def soln2(A):
    result= 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            #print(result,i,j,len(A)-1)
            if(A[i][j]==1):
                # Border Cases
                result+= int(i==0)+ int(i==len(A)-1)
                result+= int(j==0)+ int(j==len(A[i])-1)

                if(j!=0):           result+= int(A[i][j-1]==0 and j!=0)
                if(j!=len(A[i])-1): result+= int(A[i][j+1]==0 and j<len(A[i])-1)
                if(i!=0):           result+= int(A[i-1][j]==0)
                if(i!=len(A)-1):    result+= int(A[i+1][j]==0)
    return result

if __name__ == "__main__":
    print(soln2([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(soln2([[0,1,0,0],[1,1,1,1],[0,1,0,0],[1,1,0,0]]))
    print(soln2([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,1,0]]))
    print(soln2([[1,0]]))
    print(soln2([[1]]))