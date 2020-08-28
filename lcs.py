
def soln(A,B):
    brain={}
    def recursive(Am,Bm):
        ans= None
        try: 
            ans= brain[str(Am-1)+A[Am-1]+"-"+str(Bm-1)+B[Bm-1]]
        except:
            if(Am==0 or Bm==0):
                ans= 0
            elif(A[Am-1]==B[Bm-1]):
                ans= 1+recursive(Am-1,Bm-1)
                return ans
            else:
                ans= max(recursive(Am,Bm-1),recursive(Am-1,Bm))
            brain[str(Am-1)+A[Am-1]+"-"+str(Bm-1)+B[Bm-1]]=ans
        return ans
    x= recursive(len(A),len(B))
    return x

def ans(X,Y):
    def lcs(m, n): 
        if m == 0 or n == 0: 
            return 0; 
        elif X[m-1] == Y[n-1]: 
            return 1 + lcs(m-1, n-1); 
        else: 
            return max(lcs(m, n-1), lcs(m-1, n)); 
    return lcs(len(X),len(Y))

if __name__ == "__main__":
    X="AGGTAB"
    Y="GXTXAYB"
    import time
    start= time.time()
    my= soln(X,Y)
    mytime= time.time()-start
    start= time.time()
    ans= ans(X,Y)
    anstime= time.time()-start
    
    assert my==ans
    print(my,ans,anstime-mytime)
    pass