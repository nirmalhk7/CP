
def soln(A,B):
    from collections import deque
    move=[-1 for i in range(101)]
    visited=[0 for i in range(101)]
    for i in range(len(A)): move[A[i][0]]=A[i][1]
    for i in range(len(B)): move[B[i][0]]=B[i][1]
    q= deque([[1,0]]);
    print(move)
    while len(q):
        p= q[0]
        print("P",p,min(101,p[0]+7),len(visited))
        q.popleft()
        if(p[0]==100): break
        for i in (p[0]+1,min(101,p[0]+7)):
            if(visited[i]==0):
                visited[i]=1
                rx=[None,p[1]+1]
                if(move[i]!=-1):
                    rx[0]=move[i]
                else:
                    rx[0]= i
                q.append(rx)
                print(rx,q,i)
        if(p[0]==100):
            return p[1]
        else: 
            return -1

if __name__ == "__main__":
    A = [[32, 62],[42, 68],[12, 98]]
    B = [[95, 13],[97, 25],[93, 37],[79, 27],[75, 19],[49, 47],[67, 17]]
    print(soln(A,B))