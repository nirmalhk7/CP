
def soln2(A,B):
    def topoSort(v,visited,stack,prereq):
        visited[v]= True
        print("Set visited",visited[v],"Check adjacent",visited)
        for i in prereq[v]:
            print("Adjacent to",v," is ",i)
            if(visited[i]==False):
                print("Found unvisited adjacent")
                topoSort(i,visited,stack,prereq)
        stack.append(v)
        print("Visited all unvisited",stack)
    if(len(B)==0):
        return [i for i in range(A)]
    visited= [False]*A
    stack= []
    prereq= {}
    prereq = {}
    for i in B:
        if i[1] not in prereq:
            prereq[i[1]]=[]
        if i[0] in prereq:
            prereq[i[0]].append(i[1])
        else:
            prereq[i[0]]= [i[1]]
    print("HSX",prereq,"B",B)
    for i in range(len(B)):
        print("Visiting",B[i][0],visited[B[i][0]])
        if visited[B[i][0]]==False:
            topoSort(B[i][0],visited,stack,prereq)
    return stack

if __name__ == "__main__":
    # print(soln2(4,[[1,0],[3,1],[2,0],[3,2]]))
    # print(soln2(2,[[1,0]]))
    print(soln2(2,[[0,1],[1,0]]))
    # print(soln2(1,[]))