
def maxset(A):
    x=[]
    maxval=0
    ans=[]
    ansval=-99999999
    for i in range(len(A)):
        print("ANSVAL ",ans,ansval)
        if(A[i]>=0):
            x.append(A[i])
            maxval=maxval+A[i]
            print("Appending "+str(A[i])," MaxiValue "+str(maxval),x)
        if((A[i]<0 or i==len(A)-1) and x!=[]):
            # Compare
            print("COMPARE ",maxval,x,ans,ansval)
            if(maxval>ansval):
                ansval=maxval
                ans=x.copy()
                print("C1",ans,ansval)
            elif(maxval==ansval and len(ans)<len(x)):
                ansval=maxval
                ans=x.copy()
                print("C2",ans,ansval)
            elif(maxval==ansval and ans[0]<x[0]):
                ansval=maxval
                ans=x.copy()
                print("C3",ans,ansval)
            x.clear()
            maxval=0
    print("ANS",ans)
    return ans

if __name__ == "__main__":
    A=[10, -1, 2, 3, -4, 100]
    B=[1, 2, 5, -7, 2, 3]
    C=[ 0, 0, -1, 0 ]
    print("ANSWER",maxset(B))
    