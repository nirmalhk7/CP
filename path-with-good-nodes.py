
def soln(A, B, C):
    from collections import deque
    adj={}
    for i in range(len(B)):
        try:
            adj[B[i][0]].append(B[i][1])
        except:
            adj[B[i][0]]=[B[i][1]]
        try:
            adj[B[i][1]].append(B[i][0])
        except:
            adj[B[i][1]]=[B[i][0]]
    print(adj)
    visited=[False for i in range(len(A)+1)]
    good= [0 for i in range(len(A)+1)]
    ans= 0
    good[1]= A[0]
    queue= deque();
    while(queue):
        node= queue[0]
        queue.popleft()
        visited[node]= True
        previousSize= len(queue)
        for i in adj[node]:
            if(not visited[i]): queue.append(i)
            good[i]= good[node]+A[i-1]
        if(previousSize==len(queue) and good[node]<=C): ans+=1
    return ans
        

if __name__ == "__main__":
    A = [0, 1, 0, 1, 1, 1]
    B = [[1, 2],[1, 5],[1, 6],[2, 3],[2, 4]]
    C = 1
    print(soln(A,B,C))
