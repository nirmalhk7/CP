
def soln(A,N):
    v=[]
    for i in range(len(A)):
        v.append((A[i][0],A[i][2]))
        v.append((A[i][1],-A[i][2]))
    v.sort()
    sumx, mx=0, 0
    for i in range(2*len(A)):
        sumx+= v[i][1]
        mx = max(mx,sumx)
    return mx


if __name__ == "__main__":
    print(soln([[1,2,100],[2,5,100],[3,4,100]],5))
    pass