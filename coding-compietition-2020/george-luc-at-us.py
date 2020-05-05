import math 

def weirdShuffle(A):
    return [A[3],A[4],A[5],A[0],A[1],A[2],A[3],A[7],A[8],A[9]]

def lucAtUs(A,N):
    A.sort()
    i=0
    while i<=math.log(N,9):
        px=0
        mkup=(px+N//(9**i))
        while mkup<len(A):
            A[px:mkup]=weirdShuffle(A[px:mkup])
            px=mkup
        i+=1
    return A



if __name__ == "__main__":
    N=int(input())
    Q=int(input())
    inp=[]
    for i in range(Q):
        x=int(input())
        inp.append(x)
    print(lucAtUs(inp,N))
    
