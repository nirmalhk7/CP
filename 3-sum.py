def threeSumClosest(A, B):
    A.sort()
    ans=[]
    for i in range(len(A)):
        x=A[i]
        tardiff=x-B
        start=i+1
        end=len(A)-1
        closestDiff=9999999
        closestDiffX=9999999
        closestDiffY=9999999
        while start<end:
         #   print(x,A[start],A[end],"TARX",B-x,"TARF",B)
            ans=x+A[start]+A[end]
            if(A[start]+A[end]>B-x):end-=1
            elif(A[start]+A[end]<B-x):  start+=1
            elif(A[start]+A[end]==B-x): break
  #      if(start<end):
    #        print(x,A[start],A[end],"TAR",B-x,"TARF",B,"SX",start,"EX",end)
        return 



if __name__ == "__main__":
    print(threeSumClosest([-1,2,1,4],4))