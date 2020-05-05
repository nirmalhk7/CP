
def isGameOver(A):
    for i in range(len(A)):
        if(A[i]!=0):
            return False
    return True

def findWinner(A,N):
    dookuPlay=True
    #print("XJX")
    while not isGameOver(A):
        nzC=0
        # Last step of game
        for i in range(len(A)):
            if(A[i]==0):
                nzC+=1
            if(nzC>1):
                break
        if(nzC==1):
            #print("LAST ELEMENT ",dookuPlay)
            if(dookuPlay): return "1"
            else: return "0"
        A.sort()
        M=A[len(A)-1]//2+1
       # print(dookuPlay," Ai ",A[len(A)-1]," M ",M)
        A[len(A)-1]=A[len(A)-1]%M
        dookuPlay=not dookuPlay
    if(not dookuPlay): return "1"
    else: return "0"
    



if __name__ == "__main__":
    T=int(input())
    ans=""
    for i in range(T):
        N=int(input())
        A=list(map(int, input().split()))
        ans+=findWinner(A,N)
    print(ans)
