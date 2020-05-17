import operator

def twoSum(A,B):
    subA=None
    A.sort()
    Aless=[]
    ans=[]
    for i in range(len(A)):
        if A[i]<B:
            Aless.append(A[i])
    A=Aless
    for i in range(len(A)):
        if(i!=len(A)-1):
            if(A[i]+A[i+1]>B):
                continue
            for j in range(i+1,len(A)):
             #   print("Evaluating ",A[i],A[j])
                if(A[i]+A[j]==B):
              #      print("Found 1["+str(i)+"]="+str(A[i])+" 2["+str(j)+"]="+str(A[j]))
                    ans.append([i,j])
                    j=len(A)
    return ans

if __name__ == "__main__":
    print(twoSum([4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8],-3))