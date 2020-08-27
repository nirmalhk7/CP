

def soln(A):
    # We take parameters i,j to uniquely identify any subproblem.
    # State depends on the same parameters
    A1d=[max(A[0][i],A[1][i]) for i in range(len(A[0]))]
    assert len(A[0])==len(A1d)
    inclusive= A1d[0]
    exclusive= 0
    for i in range(1,len(A1d)):
        ex_new= max(exclusive,inclusive)
        inclusive= exclusive+A1d[i]
    return max(inclusive,exclusive)

def soln2(grid):
    incl = max(grid[0][0], grid[1][0])  
    excl = 0  
    for i in range(1, len(grid[0])) : 
        excl_new = max(excl, incl) 
        incl = excl + max(grid[0][i], grid[1][i])  
        excl = excl_new 
    return max(excl, incl)  

if __name__ == "__main__":
    print(soln([[1,2,3,4],[2,3,4,5]]))
    print(soln2([[1,2,3,4],[2,3,4,5]]))
    pass