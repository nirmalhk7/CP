T= int(input())
for i in range(T):
    N, M= map(int, input().split())
    print(N,M)
    A= list(map(int,input().split()))
    print(A)
    B= list(map(int,input().split()))
    print(B)
    def getLen(arr):
        if(id(A)==id(arr)):
            return N
        else:
            return M
    def otherArray(arr):
        if(id(A)==id(arr)):
            return B
        else:
            return A
    def travel(arr,ptr=0):
        sumValue=0
        while ptr<getLen(arr) and otherArray(arr)[ptr]!=arr[ptr]:
            sumValue+=arr[ptr]
            ptr+=1
            
        return sumValue
        
        
    ans= max(travel(A),travel(B))
    print(ans)