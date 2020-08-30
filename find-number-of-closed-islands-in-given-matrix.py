
def soln(N,M,mat):
    visited= [[False for j in range(M)] for i in range(N)]
    def dfs(mat,visited,i,j,n,m):
        if(i<0 or j<0 or i>=n or j>=m or visited[i][j] or not mat[i][j]):
            return
        visited[i][j]= True
        dfs(mat,visited,i+1,j,n,m)
        dfs(mat,visited,i,j+1,n,m)
        dfs(mat,visited,i-1,j,n,m)
        dfs(mat,visited,i,j-1,n,m)
        
    for i in range(1,N-1):
        for j in range(1,M-1):
            if (mat[i][j] and not visited[i][j]):
                dfs(mat,visited,i,j,N,M)
    result = 0
    for i in range(N):
        for j in range(M):
            if(not visited[i][j] and mat[i][j]):
                result+=1
                dfs(mat,visited,i,j,N,M)
    return result

if __name__ == "__main__":
    N=5
    M=8
    mat=[
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1]
    ]
    print(soln(N,M,mat))