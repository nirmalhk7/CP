from collections import deque

def soln(A,B,C,D,E,F):
    def canGo(adjacentPts,adjacentCanGo,endPts=[E,F],rad=D,start=[A,B]):
        pass
    q= deque((0,0))
    visited= [[False]*(B+1) for i in range(A+1)]
    visited[0][0]= True
    while not len(q):
        x1, y1= q[0]
        if(visited[A][B]): return "YES"
        if(x1+1)<=A and not visited[x1+1][y1] and canGo([x1,y1],[x1+1,y1]):
            visited[x1+1][y1]= True
            q.append(x1+1,y1)
        if(x1-1)<=A and not visited[x1-1][y1] and canGo([x1,y1],[x1-1,y1]):
            visited[x1-1][y1]= True
            q.append(x1-1,y1)
        if(y1+1)<=B and not visited[x1][y1+1] and canGo([x1,y1],[x1,y1+1]):
            visited[x1+1][y1]= True
            q.append(x1,y1+1)
        if(y1-1)<=B and not visited[x1][y1-1] and canGo([x1,y1],[x1,y1-1]):
            visited[x1][y1-1]= True
            q.append(x1,y1-1)
        
        

if __name__ == "__main__":
    print(soln(2,3,1,1,[2],[3]))