

def soln(A):
    def getCommonAround(i):
        count= 0
        k= 1
        print("HERE",i,range(k,len(A)-1-k))
        while i in range(k,len(A)-k):
            print("COMPARE",A[i-k],A[i+k])
            input()
            if(A[i-k]==A[i+k]):
                count+=1
                k+=1
            else: break
        return count
    midpoint={}
    for i in range(len(A)-1):
        if(A[i-1]==A[i+1]):
            midpoint[i]=0
    midpoint[len(A)-1]=0
    # print(midpoint)
    maxValue=(-1,-1)
    for key in midpoint:
        print("CHECK",key)
        midpoint[key]=getCommonAround(key)
        maxValue=(key,max(midpoint[key],maxValue[1]))
    print(maxValue)

    return midpoint

def soln2(A):
    def isPalindrome(A,i,j):
        c=0
        while i<j:
            if(A[i]!=A[j]):
                return False
            i+=1
            j-=1
        return True
    i,c,j=0,0,len(A)-1
    while i<j:
        if(A[i]==A[j] and isPalindrome(A,i,j)):
            return c
        i+=1
        c+=1
    return c
            
if __name__ == "__main__":
    # print(soln("abede"))
    # print(soln("aabb"))
    print(soln2("babedeedee"))
    # print(soln("nirmal"))