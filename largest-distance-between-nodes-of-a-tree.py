
def soln(A):
    arrLens=[]
    def dfs(A,position,color,largeLength=0):
        color[position]="gray"
        print("Node ",position,largeLength)
        hasChildren=False
        for i in range(len(A)):
            if(A[i]==position and color[i]=="white"):
                hasChildren= True
                print("Going to",i)
                if(not hasChildren):
                    arrLens.append(max(largeLength,dfs(A,i,color,largeLength+1)))
                print("Returned BACK",position,hasChildren)
        color[position]="black"
        return largeLength

    dfs(A,0,["white" for i in range(len(A))])
    print(arrLens)
            



if __name__ == "__main__":
    print(soln([-1, 0, 0, 0, 3]))