
def soln(A,B):
    G={i:[] for i in range(1,A+1)}
    for i in range(len(B)):
        fromval, toval = B[i]
        G[fromval].append(toval)
    color=["white" for i in range(A+1)]

    def checkCycle(position=1):
        color[position]="gray"
        print("Visiting",position)
        ans= 0
        for i in G[position]:
            if(color[i]=="white"):
                ans= checkCycle(i)
            else:
                print("CYCLE",position,i,color)
                return 1
        color[position]="black"
        return ans

    return checkCycle()

if __name__ == "__main__":
    A = 5
    B = [[1, 2],[4, 1],[2, 4],[3, 4],[5, 2],[1, 3]]
    # B = [[1, 2],[2, 3],[3, 4],[4, 5]]
    print(soln(A,B))