from collections import deque

def soln(A,B): 
    lenA= len(A)
    if(B>=lenA): return max(A)
    window= deque()
    winlen= 0
    prevmax= -9999999999
    maxarr=[0 for i in range(lenA+1-B)]
    maxarrmarker=0
    for i in range(lenA):
        if(winlen<B):
            window.append(A[i])
            winlen+= 1
        else:
            if(prevmax==-9999999999):
                maxarr[maxarrmarker]=max(window)
                maxarrmarker+=1
            else:
                prevmax= max(window[-1], prevmax)
                maxarr[maxarrmarker]=prevmax
                maxarrmarker+=1 
            window.popleft()
            window.append(A[i])
            if(i+1==len(A)):
                maxarr[maxarrmarker]=max(window[-1],prevmax)
                maxarrmarker+=1
        # print(window)
    return maxarr

def soln3(A,B):
    n=len(A)
    if(B>=n):
        return [max(A)]
    ans=[]
    l=0
    r=B-1
    mi=1
    mv=A[1]
    for i in range(l+1,r+1):
        if(A[i]>mv):
            mi= i
            mv= A[i]
    while r<n:
        if(A[r]>mv): 
            mi= i

def soln2(A,B):
    lenA= len(A)
    if(B>=lenA): return max(A)
    maxarr=[0 for i in range(lenA+1-B)]
    maxarrmarker=0
    for i in range(lenA-B+1):
        window=(A[i:i+B])
        maxarr[maxarrmarker]=max(window)
    return maxarr
if __name__ == "__main__":
    import time
    start= time.time()
    print(soln([1, 3, -1, -3, 5, 3, 6, 7],3))
    print("TIME",time.time()-start)
    start= time.time()
    print(soln2([1, 3, -1, -3, 5, 3, 6, 7],3))
    print("TIME",time.time()-start)
    # print(soln([1, 3, -3, 5, 3, 6, 7],3))
    # print(soln([1],2))